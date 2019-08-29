from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นางสาวสิริกร โพธิ์งาม เลขที่ 22 ชั้น ม.4/5"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    #user = decoded["events"][0]['replyToken']
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    #userText = decoded["events"][0]['message']['text']
    userText = decoded['queryResult']['intent']['displayName']
    #sendText(user,userText)
    if (userText == 'สวัสดี') :
        sendText(user,'ดีด้วย')
    elif (userText == 'ไปนะ') :
        sendText(user,'ไปตายที่ไหนก็ไป')
    elif (userText == 'รักนะคะ') :
        sendText(user,'รักเหมือนกันค่ะ')
    elif (userText == 'คิดถึงนะ') :
        sendText(user,'คิดถึงมากกว่า')
    elif (userText == 'คุณท้องฟ้า') :
        sendText(user,'ว่าไงคะ? คุณดวงจันทร์')
    elif (userText == 'คุณท้องฟ้ารักคุณดวงจันทร์ไหมคะ') :
        sendText(user,'รักสิคะ คุณท้องฟ้ารักคุณดวงจันทร์ที่สุดเลยค่ะ')
    elif (userText == 'คุณดวงจันทร์รักคุณท้องฟ้ามากเลยค่ะ') :
        sendText(user,'คุณดวงจันทร์รักคุณท้องฟ้ามากแค่ไหนคะ')
    elif (userText == 'คุณดวงจันทร์รักคุณท้องฟ้ามากๆๆๆๆเลยค่ะ') :
        sendText(user,'คุณท้องฟ้าก็รักคุณดวงจันทร์มากกเหมือนกันค่าา')
    elif (userText == ':)') :
        sendText(user,':)')
    elif (userText == ';)') :
        sendText(user,';)')
    else :
        sendText(user,'ว่าไงนะ')
    
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
