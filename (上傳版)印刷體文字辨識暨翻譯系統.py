import requests

subscription_key_OCR="放入您的電腦視覺資源金鑰" 
endpoint="放入您的電腦視覺資源端點網址" 
ocr_url=endpoint+"vision/v3.0/ocr"
image_url="放入您想要辨識的文字圖片(url)網址" #放入您想要辨識的文字圖片(url)網址
headers={'Ocp-Apim-Subscription-Key':subscription_key_OCR}
params={'language':'unk'}
data_OCR={'url':image_url}
response_OCR=requests.post(ocr_url,headers=headers,params=params,json=data_OCR)
analysis=response_OCR.json()
if analysis["regions"]==[]:
    print("無法辨識文字!無法提供翻譯!")
else:
    n=len(analysis["regions"][0]["lines"])
    regions=[]
    for i in range(0,n):
        m=len(analysis["regions"][0]["lines"][i]["words"])
        for j in range(0,m):
            regions.append(analysis["regions"][0]["lines"][i]["words"][j]["text"])
    StrA = " ".join(regions)
    print("辨識內容:%s"%StrA)
    subscription_key_Translator="放入您的翻譯資源金鑰" 
    trans_base_url="#放入您的翻譯資源端點網址" 
    trans_url=trans_base_url+'translate?api-version=3.0'
    headers={'Ocp-Apim-Subscription-Key':subscription_key_Translator}
    params='&to=放入您想翻譯的語言' 
    texts=StrA
    data_Translator=[{'text':texts}]
    response_Translator=requests.post(trans_url,headers=headers,params=params,json=data_Translator)
    result=response_Translator.json()
    print('翻譯結果:'+result[0]['translations'][0]['text'])