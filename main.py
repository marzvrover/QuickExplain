from bottle import request, response, route, run
import llm
import json

current_model = "wizardlm-13b-v1"

@route('/', method='GET')
def index():
    return "hello, world"

@route('/', method='POST')
def quick_explain():
    model = llm.get_model(current_model)
    generated_response =  model.prompt(
        buildMessageList(request.json),
        system="Explain the very last message, using the previous messages to optionally add context, to me like I am five",)
    response.content_type = 'application/json'
    responseObject = {
        "id": "QuickExplain",
        "model": current_model,
        "choices": [{
            "message": {
                "role": "assistant",
                "content": str(generated_response)
            },
        }]
    }
    print(buildMessageList(request.json))
    print(generated_response)
    return json.dumps(responseObject)

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
    return str.join("--\n", messages)

run(host='localhost', port=8080, debug=True)
