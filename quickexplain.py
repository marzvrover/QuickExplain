#!/usr/bin/env python3
""" A simple HTTP server that uses an LLM to explain complex topics. """

import json
import os
import time

import llm

from bottle import request, response, route, run

DEBUG = os.environ.get("QUICKEXPLAIN_DEBUG", "false").lower() == "true"
MODEL = os.environ.get("QUICKEXPLAIN_MODEL", "wizardlm-13b-v1")
# estimating tokens as 4 characters each
TOKEN_LIMIT = os.environ.get("QUICKEXPLAIN_TOKEN_LIMIT", 2048)

@route('/', method='GET')
def index():
    """Return a friendly HTTP greeting."""
    return "hello, world"

@route('/', method='POST')
def quick_explain():
    """Return a simple explanation of the last message in the thread."""
    message_history = build_message_list(request.json)
    if DEBUG:
        print(message_history)

    prompt = """
You are QuickExplain, an expierenced teacher helping people understand complex topics.
Do not greet, just explain the topic.
Explain the very last message, using the previous messages to optionally add context, to me like I am five
"""

    model = llm.get_model(MODEL)
    generated_response =  str(model.prompt(
        message_history,
        system=prompt,))
    if DEBUG:
        print(generated_response)

    response_object = {
        "id": "QuickExplain",
        "created": int(time.time()),
        "model": MODEL,
        "choices": [{
            "index": 0,
            "delta": {
                "content": generated_response,
            },
        }]
        }

    response.content_type = 'application/json'
    response.status = 200
    return "data: " + json.dumps(response_object) + "\r\n\r\n"

@route('/oauth/callback')
def oauth_callback():
    """Do nothing with the OAuth callback, for now. Just return a 200."""
    print("received oauth callback")
    response.content_type = 'application/json'
    response.status = 200
    return '{ "ok": true }'

def build_message_list(message_history):
    """Build a list of messages from the input object."""
    messages = map(lambda message: message["content"], message_history["messages"])
    # only take the last TOKEN_LIMIT*4 characters
    return "\n--\n".join(messages)[-TOKEN_LIMIT*4:]

run(host='localhost', port=8080, debug=DEBUG)
