from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text_to_analyze)

    # Process result (you should replace this with actual processing)
    if result:
        emotions = result
        dominant_emotion = emotions['dominant_emotion']
        response_message = (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, and "
            f"'sadness': {emotions['sadness']}. The dominant emotion is {dominant_emotion}."
        )
        return jsonify({"message": response_message}), 200
    else:
        return jsonify({"error": "Error processing the text"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
