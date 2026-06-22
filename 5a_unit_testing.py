
from EmotionDetection.emotion_detection import emotion_detector

def test_emotion_detector_cases():
    
    result_1 = emotion_detector("I am glad this happened")
    assert result_1['dominant_emotion'] == 'joy', f"Attendu: joy, Reçu: {result_1['dominant_emotion']}"

    result_2 = emotion_detector("I am really mad about this")
    assert result_2['dominant_emotion'] == 'anger', f"Attendu: anger, Reçu: {result_2['dominant_emotion']}"
        
    result_3 = emotion_detector("I feel disgusted just hearing about this")
    assert result_3['dominant_emotion'] == 'disgust', f"Attendu: disgust, Reçu: {result_3['dominant_emotion']}"   
    
    result_4 = emotion_detector("I am so sad about this")
    assert result_4['dominant_emotion'] == 'sadness', f"Attendu: sadness, Reçu: {result_4['dominant_emotion']}"
        
    result_5 = emotion_detector("I am really afraid that this will happen")
    assert result_5['dominant_emotion'] == 'fear', f"Attendu: fear, Reçu: {result_5['dominant_emotion']}"

    print("all test succes")
if __name__ == '__main__':
    test_emotion_detector_cases()
