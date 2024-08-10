import requests
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

        response_data = response.json()

        # Error handling for empty responses or missing text field
        if 'emotionPredictions' not in response_data:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        emotions = response_data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        result = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
        return result
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            return {'error': str(http_err)}
    except Exception as err:
        return {'error': str(err)}
