import eel
import ujson

eel.init("static")


@eel.expose
def send_data():
    with open("./static/data.json", "r", encoding="utf-8") as jsonFile:
        data = ujson.load(jsonFile)
    return data


def closing():
    print("The page has been closed")
    # exit()


eel.start("index.html", mode="chrome", shutdown_delay=60)  # close_callback=closing(), shutdown_delay=100
