import json
import sys

from bottle import Bottle, abort, error, get, post, request, response, run
from gevent import monkey

monkey.patch_all()

app = Bottle()


@app.route("/error")
def error():
    abort(404, "Not Found")


@app.get("/")
def index():
    return "Hello World!"


@app.post("/")
def post_index():
    data = request.json

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(data, file=sys.stderr)
    return


if __name__ == "__main__":
    run(app, host="localhost", port=8080, server="gevent", debug=True, reloader=True)
