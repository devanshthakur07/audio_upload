# Audio Upload Dashboard

The Audio Upload Dashboard is a web application that allows users to upload audio files, view their uploaded files, and play them directly from the dashboard. The application provides a simple user interface where users can manage their uploaded audio files.

## Features

- Upload single or multiple audio files.
- View uploaded files in a tabular form.
- Play uploaded audio files directly from the dashboard.
- Receive a warning if the total duration of uploaded files exceeds 10 minutes.

## Prerequisites

- Python 3.x
- Flask
- pymongo
- mutagen

## Installation

1. Clone the repository
   
   git clone https://github.com/devanshthakur07/audio_upload.git
   cd audio_upload
   
2. Install the required Python packages using pip
   
   pip install Flask pymongo mutagen

3. Run the application
   
   python app.py

The application will be accessible at http://127.0.0.1:5000/ in your web browser.

## Usage
Open your web browser and navigate to http://127.0.0.1:5000/.
Use the file upload form to select and upload audio files.
Uploaded files will be displayed in a table with their filename, upload date, and duration.
Click the "Play" button to listen to the uploaded audio files.
If the total duration of uploaded files exceeds 10 minutes, a warning will be displayed.
Project Structure
app.py: The main Flask application that handles routing and logic.
templates/index.html: The HTML template for the dashboard.
static/uploads/: The directory where uploaded audio files are saved.
