import os
import secrets
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from parse_dot_env import parse_dot_env
from transcriptparser import TranscriptParser
import argparse

UPLOAD_FOLDER = "./resources/uploads"
ALLOWED_EXTENSIONS = {"pdf"}
env_vars = parse_dot_env()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
app.add_url_rule("/transcript/<name>", endpoint="transcript", build_only=True)
app.secret_key = secrets.token_urlsafe(32)
parser = TranscriptParser(os.getenv("OPENAI_API_KEY", env_vars.get("OPENAI_API_KEY")))


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def upload_transcript():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No selected file")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("transcript", name=filename))
    return render_template("index.html")


@app.route("/transcript/<name>")
def display_transcript(name):
    transcript_path = os.path.join(app.config["UPLOAD_FOLDER"], name)
    return parser.query(transcript_path)


if __name__ == "__main__":
    host = os.getenv("TRANSRIPT_HOST", "127.0.0.1")
    port = os.getenv("TRANSRIPT_PORT", 5000)
    assert port.isnumeric(), "port must be numeric"
    port = int(port)
    app.run(host=host, port=port, debug=True)
