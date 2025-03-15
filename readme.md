# Video Downloader
A simple tool to download videos or music from YouTube using YT_DLP and Flask 😀

## Prerequisites
* Create a ".env" file on the root of the project with the following variable
    * "DOWNLOAD_DIRECTORY=/directory/to/download/files" (without quotes)
* Create a virtual environment (if you don't have one)
    * python -m venv venv
* Activate the virtual environment
    * ``` $ source venv/bin/activate ```
* Install the requirements.txt
    * pip install -r requirements.txt
* Start Flask
    * ``` $ python main.py ```
* The server will start automatically on port 5000