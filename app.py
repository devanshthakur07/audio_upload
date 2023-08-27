from mutagen.mp3 import MP3
from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime, timedelta
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['audio_dashboard']
uploads_collection = db['uploads']


def seconds_to_minutes(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02}:{remaining_seconds:02}"


@app.route('/', methods=['GET', 'POST'])
def index():
    user = "User1"  # Initialize the user variable with a default value
    if request.method == 'POST':
        files = request.files.getlist('file')
        total_duration = 0

        for file in files:
            filename = file.filename
            file_extension = os.path.splitext(filename)[1]
            udate = datetime.now()
            op = '%s/%s/%s' % (udate.month, udate.day, udate.year)
            
            audio = MP3(file)
            audio_duration = audio.info.length

            total_duration += audio_duration

            upload_data = {
                'filename': filename,
                'user': user,
                'upload_date': op,
                'duration': seconds_to_minutes(int(audio_duration))
            }
            uploads_collection.insert_one(upload_data)

            file.save(os.path.join('static/uploads', filename))

        if total_duration > 600:
            warning = "Total duration of files exceeds 10 minutes!"

    uploads = uploads_collection.find({'user': user})

    return render_template('index.html', uploads=uploads)

if __name__ == '__main__':
    app.run(debug=True)
