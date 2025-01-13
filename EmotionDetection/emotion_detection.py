import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header) 
    
    #turns response into json dict
    formatted_response = json.loads(response.text)
    #retrieves requested content as list
    emopred = formatted_response['emotionPredictions']
    #puts the i of emotion from emopred into emolist
    emolist = [i["emotion"] for i in emopred]
    #initialize emotion dict
    emos = {}
    #stores iterables from emolist into emos dict
    for i in emolist:
        emos.update(i)
    #initialize vars for dominant emotion and its value
    emodom = ""
    emodomval = 0.0
    #iterates through key value pairs in emos dict
    for k,v in emos.items():
        if v > emodomval:
            emodomval = v
            emodom = k
    #appends dominant_emotion and its result to emos dict
    emos.update({'dominant_emotion' : emodom})
    #returns emotions and their scores, along with dominant_emotion
    
    #make sure this is emos!
    return emos




# python3.11
# from EmotionDetection.emotion_detection import emotion_detector
# emotion_detector("I love this new technology.")
# emotion_detector("I am so happy I am doing this.")
# emotion_detector("I hate working long hours.")
# python3.11 test_emotion_detection.py .
# emotion_detector("I am glad this happened.")

# cd oaqjp-final-project-emb-ai