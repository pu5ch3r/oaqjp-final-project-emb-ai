from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    return emotions

@app.route("/")
def home():
    return render_template("index.html")