from flask import Flask, Response
import time

app = Flask("curl_commands")

#######################################################################

RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLO = "\x1b["
RESET = "\x1b[0m"

#######################################################################

INDEX_FRAMES = ["( o.o )", "( ^.^ )", "( -.- )"]  # swap for real ASCII art

def generate():
    clear = "\x1b[2J"       # clear screen
    home = "\x1b[H"         # move cursor to top-left
    yield clear
    while True:
        for frame in INDEX_FRAMES:
            yield home + frame + "\n"
            time.sleep(0.3)

@app.route("/")
def index():
    return Response(generate(), mimetype="text/plain")


#######################################################################

LOVE_FRAMES = ["<|", "<3"]

def generate_love():
    clear = "\x1b[2J"
    home = "\x1b[H"
    yield clear
    while True:
        for frame in LOVE_FRAMES:
            yield home + frame + "\n"
            time.sleep(0.3)


@app.route("/love")
def love():
    return Response(generate_love(), mimetype="text/plain")

#######################################################################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
