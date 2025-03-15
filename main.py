from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="static", static_url_path="/")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download_url", methods=["POST"])
def download_url():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)