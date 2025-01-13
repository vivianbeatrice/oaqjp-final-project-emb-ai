from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #test for joy
        result_1 = emotion_detector('I am glad this happened.')
        self.assertEqual(result_1, 'joy')

        #test for anger
        result_2 = emotion_detector('I am really mad about this.')
        self.assertEqual(result_2, 'anger')

        #test for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this.')
        self.assertEqual(result_3, 'disgust')

        #test for sadness
        result_4 = emotion_detector('I am so sad about this.')
        self.assertEqual(result_4, 'sadness')

        #test for fear
        result_5 = emotion_detector('I am really afraid that this will happen.')
        self.assertEqual(result_5, 'fear')

unittest.main()



# python3.11 test_emotion_detection.py