from flask import Flask, render_template, request, jsonify, redirect
from modules.downloader import downloader
import threading

app = Flask(__name__, static_folder="static", static_url_path="/")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download_url", methods=["POST"])
def download_url():

    #Creates a dict with the correct format to use in download_url
    url_to_download = {
        "url" : request.form["url"],
        "format" : request.form["format"],
        "quality" : request.form["video_quality"]
    }
    if "isPlaylist" in request.form:
        url_to_download["is_playlist"] = True

    # downloader(url_to_download)

    # Create a thread for downloading in background
    download_thread = threading.Thread(
        target=downloader,
        args=(url_to_download,)
    )
    download_thread.start()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)