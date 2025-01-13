from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route("/emotionDetector")
def emotiondetector():
    return emos