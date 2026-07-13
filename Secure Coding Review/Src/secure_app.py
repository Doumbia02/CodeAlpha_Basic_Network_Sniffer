"""
SecureNotes - remediated version.
Fixes applied for every finding in the audit report (see SECURITY_REVIEW.docx).
"""

import os
import secrets
import sqlite3
from functools import wraps

from flask import Flask, request, redirect, make_response, abort, session
from markupsafe import escape
from werkzeug.security import generate_password_hash, check_password_hash
import requests

app = Flask(__name__)

# FIX (VULN 1): secret loaded from environment, never committed to source
app.secret_key = os.environ["FLASK_SECRET_KEY"]

DB_PATH = os.environ.get("NOTES_DB_PATH", "notes.db")
UPLOAD_ROOT = os.path.abspath("uploads")

# FIX (VULN 9): allow-list of hosts the server is permitted to fetch from
ALLOWED_AVATAR_HOSTS = {"avatars.trusted-cdn.example.com"}


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, "
        "username TEXT UNIQUE, password_hash TEXT, is_admin INTEGER DEFAULT 0)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, "
        "user_id INTEGER, title TEXT, body TEXT)"
    )
    conn.commit()
    conn.close()


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            abort(401)
        return fn(*args, **kwargs)
    return wrapper


# FIX (VULN 2 + 3): parameterized query + salted password hash (PBKDF2/werkzeug)
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = get_db()
    cur = conn.execute(
        "SELECT id, password_hash, is_admin FROM users WHERE username = ?",
        (username,),
    )
    row = cur.fetchone()
    conn.close()

    if row is None or not check_password_hash(row[1], password):
        # constant-shape response; do not reveal whether username exists
        return "Invalid credentials", 401

    # FIX (VULN 4): cryptographically secure session token, plus secure cookie flags
    session.clear()
    session["user_id"] = row[0]
    session["is_admin"] = bool(row[2])
    resp = make_response(redirect("/dashboard"))
    resp.set_cookie(
        "session_token",
        secrets.token_urlsafe(32),
        httponly=True,
        secure=True,
        samesite="Lax",
    )
    return resp


# FIX (VULN 5): rely on Jinja2 auto-escaping instead of building HTML by hand
@app.route("/search")
def search():
    q = request.args.get("q", "")
    from flask import render_template_string
    return render_template_string("<h1>Results for: {{ q }}</h1>", q=q)


# FIX (VULN 6): no shell, argument passed as a discrete list, input validated
@app.route("/ping")
@login_required
def ping():
    import ipaddress
    import subprocess

    host = request.args.get("host", "")
    try:
        ipaddress.ip_address(host)  # only accept a literal, valid IP address
    except ValueError:
        return "Invalid host", 400

    result = subprocess.run(
        ["/bin/ping", "-c", "1", host], shell=False, capture_output=True, timeout=5
    )
    return result.stdout


# FIX (VULN 7): resolve and confirm the path stays inside UPLOAD_ROOT
@app.route("/download")
@login_required
def download():
    filename = request.args.get("file", "")
    candidate = os.path.abspath(os.path.join(UPLOAD_ROOT, filename))
    if not candidate.startswith(UPLOAD_ROOT + os.sep):
        abort(403)
    if not os.path.isfile(candidate):
        abort(404)
    with open(candidate, "rb") as f:
        return f.read()


# FIX (VULN 8): use a safe, schema-restricted format (JSON) instead of pickle
@app.route("/import_note", methods=["POST"])
@login_required
def import_note():
    note = request.get_json(force=False, silent=True)
    if not note or "title" not in note:
        return "Invalid payload", 400
    return {"title": str(note["title"])[:200]}


# FIX (VULN 9 continued): allow-list check before making the outbound request
@app.route("/fetch_avatar")
@login_required
def fetch_avatar():
    from urllib.parse import urlparse

    url = request.args.get("url", "")
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_AVATAR_HOSTS:
        abort(400)
    resp = requests.get(url, timeout=5)
    return resp.content


# FIX (VULN 10): ownership check before returning a note (fixes IDOR)
@app.route("/notes/<int:note_id>")
@login_required
def get_note(note_id):
    conn = get_db()
    cur = conn.execute(
        "SELECT title, body, user_id FROM notes WHERE id = ?", (note_id,)
    )
    row = cur.fetchone()
    conn.close()
    if row is None:
        abort(404)
    if row[2] != session["user_id"] and not session.get("is_admin"):
        abort(403)
    return {"title": escape(row[0]), "body": escape(row[1])}


if __name__ == "__main__":
    init_db()
    # FIX (VULN 11): debug off, bind to loopback; use a real WSGI server in prod
    app.run(host="127.0.0.1", port=5000, debug=False)
