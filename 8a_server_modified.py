"""
Flask server module for the Emotion Detection application.
Provides routes to render the user interface and to analyze
input text using the Watson NLP local library.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """
    Retrieves text from request arguments, executes emotion detection,
    and returns a formatted string response or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Texte invalide ! Veuillez réessayer !"

    return (
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} et "
        f"'sadness': {response['sadness']}. "
        f"L'émotion dominante est {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main HTML index page for the user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
