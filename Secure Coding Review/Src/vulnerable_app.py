"""
SecureNotes - a small Flask app for storing user notes and profile files.
This file intentionally contains realistic, common vulnerabilities for the
purposes of a secure-coding review (Task 3). DO NOT deploy as-is.
"""

import os
import sqlite3
import subprocess
import pickle
import hashlib
import random

from flask import Flask, request, render_template_string, redirect, make_response
import requests

app = Flask(__name__)

# --- VULN 1: hardcoded secret key committed to source control ---
app.secret_key = "s3cr3t-key-2024"

DB_PATH = "notes.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, "
        "username TEXT, password TEXT, is_admin INTEGER)"
    )
    conn.execute(
        "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, "
        "user_id INTEGER, title TEXT, body TEXT)"
    )
    conn.commit()
    conn.close()


# --- VULN 2: SQL Injection (string-formatted query) ---
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Weak hash for password comparison
    hashed = hashlib.md5(password.encode()).hexdigest()  # VULN 3: weak hash (MD5)

    conn = get_db()
    query = "SELECT id, is_admin FROM users WHERE username = '%s' AND password = '%s'" % (
        username,
        hashed,
    )
    cur = conn.execute(query)  # VULN 2 continued: injectable query
    row = cur.fetchone()
    conn.close()

    if row:
        resp = make_response(redirect("/dashboard"))
        # --- VULN 4: session/auth token is predictable ---
        token = str(random.randint(100000, 999999))  # insecure PRNG for a security token
        resp.set_cookie("session_token", token)
        return resp
    return "Invalid credentials", 401


# --- VULN 5: Reflected XSS via render_template_string with raw user input ---
@app.route("/search")
def search():
    q = request.args.get("q", "")
    template = "<h1>Results for: " + q + "</h1>"
    return render_template_string(template)


# --- VULN 6: OS command injection ---
@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    result = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
    return result.stdout


# --- VULN 7: Path traversal / arbitrary file read ---
@app.route("/download")
def download():
    filename = request.args.get("file")
    path = os.path.join("uploads", filename)
    with open(path, "rb") as f:
        data = f.read()
    return data


# --- VULN 8: Insecure deserialization ---
@app.route("/import_note", methods=["POST"])
def import_note():
    blob = request.data
    note = pickle.loads(blob)  # arbitrary code execution if blob is attacker-controlled
    return {"title": note.get("title")}


# --- VULN 9: Server-Side Request Forgery (SSRF) ---
@app.route("/fetch_avatar")
def fetch_avatar():
    url = request.args.get("url")
    resp = requests.get(url)  # no allow-list, can reach internal network / metadata service
    return resp.content


# --- VULN 10: Broken access control (IDOR) ---
@app.route("/notes/<note_id>")
def get_note(note_id):
    conn = get_db()
    # any authenticated (or even unauthenticated) user can read any note by guessing IDs
    cur = conn.execute("SELECT title, body FROM notes WHERE id = ?", (note_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"title": row[0], "body": row[1]}
    return "Not found", 404


if __name__ == "__main__":
    init_db()
    # --- VULN 11: debug mode enabled in what looks like a prod entrypoint ---
    app.run(host="0.0.0.0", port=5000, debug=True)
