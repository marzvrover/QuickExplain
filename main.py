from bottle import route, run
import llm

@route('/')
def index():
    return "hello, world"

run(host='localhost', port=8080)
