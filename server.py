import json
import sys

from bottle import Bottle, abort, error, get, post, request, response, run

app = Bottle()


@app.route("/error")
def error():
    abort(404, "Not Found")


@app.route("/hello")
def hello():
    return "Hi %s!" % request.params["name"]


@app.get("/")
def index():
    return "Hello World!"


@app.post("/")
def post_index():
    data = request.json

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(request.json, file=sys.stderr)
    return


if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True, reloader=True)
