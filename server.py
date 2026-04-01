'''
   detecting emotions for user provided strings
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotions():
    '''
       handling user specific input and calling the emotion detector
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze != "":
        emotions = emotion_detector(text_to_analyze)

        if emotions["dominant_emotion"] is not None:
            return emotions
    return {"message": "Invalid text! Please try again!"}

@app.route("/")
def home():
    '''
        returning the static home page
    '''
    return render_template("index.html")
