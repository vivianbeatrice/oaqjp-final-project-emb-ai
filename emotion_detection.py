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

    #need to pull keys & values from emolist into emokeys & emovalues, then zip into emodict
    #are the below lists correct?
    emokeys = list(i.keys() for i in emolist)
    emovalues = list([i.values() for i in emolist])

 

    #return test


# python3.11
# from emotion_detection import emotion_detector
# emotion_detector("I love this new technology.")

