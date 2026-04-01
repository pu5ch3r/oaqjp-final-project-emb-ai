import requests
import json

EMOTION_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    input = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(EMOTION_URL, json=input, headers=HEADERS)

    json_response = json.loads(response.text)
    json_emotions = dict(json_response["emotionPredictions"][0]["emotion"])

    anger = json_emotions["anger"]
    disgust = json_emotions["disgust"]
    fear = json_emotions["fear"]
    joy = json_emotions["joy"]
    sadness = json_emotions["sadness"]

    dict_emotions = {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness}
    dominant_emotion = max(dict_emotions, key=dict_emotions.get)
    dict_emotions["dominant_emotion"] = dominant_emotion

    return dict_emotions