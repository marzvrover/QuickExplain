from bottle import request, response, route, run
from gevent import monkey; monkey.patch_all()
import llm
import json
import time

DEBUG = True
MODEL = "wizardlm-13b-v1"
TOKEN_LIMIT = 2048 # estimating tokens as 4 characters each

@route('/', method='GET')
def index():
    return "hello, world"

@route('/', method='POST')
def quick_explain():
    messageHistory = buildMessageList(request.json)
    if DEBUG:
        print(messageHistory)

    model = llm.get_model(MODEL)
    generatedResponse =  str(model.prompt(
        messageHistory,
        system="Explain the very last message, using the previous messages to optionally add context, to me like I am five",))
    if DEBUG:
        print(generatedResponse)

    responseObject = {
        "id": "QuickExplain",
        "created": int(time.time()),
        "model": MODEL,
        "choices": [{
            "index": 0,
            "delta": {
                "content": generatedResponse,
            },
        }]
        }

    response.content_type = 'application/json'
    response.status = 200
    return "data: " + json.dumps(responseObject) + "\r\n\r\n"

# Do nothing with the OAuth callback, for now. Just return a 200.
@route('/oauth/callback')
def oauth_callback():
    print("received oauth callback")
    response.content_type = 'application/json'
    response.status = 200
    return '{ "ok": true }'

def buildMessageList(input):
    messages = []
    for message in input["messages"]:
        messages.append(message["content"])
    messagesAsString = str.join("\n--\n", messages)
    # only take the last TOKEN_LIMIT*4 characters
    return messagesAsString[-TOKEN_LIMIT*4:]

run(host='localhost', port=8080, debug=DEBUG)
