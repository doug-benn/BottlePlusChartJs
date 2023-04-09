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
    print("Hello World!", file=sys.stderr)
    return "Hello World!"


@app.post("/demo")
def demo():
    data = request.json

    js_string = """data = {data};"""

    with open("data.js", "w", encoding="utf-8") as jsonFile:
        jsonFile.write(js_string.format(data=json.dumps(data)))

    return


@app.post("/")
def post_index():
    newData = request.json
    # If the data is "Wrapped" then it will need "unwrapping"

    with open("data.js", "r", encoding="utf-8") as jsonFile:
        data = jsonFile.read()
        data = data[7:]
        data = data[:-1]
        data = json.loads(data)

    for x in range(len(data)):
        if data[x]["Language"] == newData["Language"] and data[x]["Type"] == newData["Type"]:
            data[x] = newData
            newData = ""
            break

    if newData:
        data.append(newData)

    js_string = """data = {data};"""

    with open("data.js", "w", encoding="utf-8") as jsonFile:
        jsonFile.write(js_string.format(data=json.dumps(data)))

    return


if __name__ == "__main__":
    run(app, host="localhost", port=8080, server="gevent", debug=True)


# @app.route("/", methods=["POST"])
# def andon():
#     if request.remote_addr == "172.25.32.36" and request.data.decode()[9:20] == "BuildItemId":
#         print("Andon Alarm")
#         newData = read_data(request.json)

#         with open("data.json", "r") as jsonFile:
#             data = json.load(jsonFile)

#         for x in range(len(data)):
#             if data[x]["StationId"] == newData["StationId"] and data[x]["EventName"] == newData["EventName"]:
#                 data[x] = newData
#                 newData = ""
#                 break

#         if newData:
#             data.append(newData)

#         with open("data.json", "w") as jsonFile:
#             json.dump(data, jsonFile)

#         return jsonify(success=True)

#     else:
#         print("Not PINpoint")
#         return "Unauthorized", 401
