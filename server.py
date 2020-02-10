from flask import Flask, Response, request
import requests

from commandhandler import *

app = Flask(__name__)


TOKEN = '1008102529:AAEUP_EsZdSN1D47Pa5hA1OPKi03bPIGeos'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://9b10e77f.ngrok.io/message'.format(TOKEN)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/sanity')
def sanity():return "Server is running"

@app.route('/message', methods=["POST"])
def handle_message():
    try:
        print("message:")

        fromuser=request.get_json()['message']['text']
        print(fromuser)
        print("from:")
        print(request.get_json()['message']['chat'])

        tosendback =messageparser(fromuser)

        chat_id = request.get_json()['message']['chat']['id']
        res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                       .format(TOKEN, chat_id, tosendback))
        print (res)
    except:
        print("eception provoked")
    return Response("success")

if __name__ == '__main__':
    app.run(port=5008)
