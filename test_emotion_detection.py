import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def check_emotion(self, text, expected_emotion):
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], expected_emotion, f"Expected {expected_emotion} but got {result['dominant_emotion']}")

    def test_joy(self):
        self.check_emotion("I am glad this happened", "joy")

    def test_anger(self):
        self.check_emotion("I am really mad about this", "anger")

    def test_disgust(self):
        self.check_emotion("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self.check_emotion("I am so sad about this", "sadness")

    def test_fear(self):
        self.check_emotion("I am really afraid that this will happen", "fear")

if __name__ == '__main__':
    unittest.main()
