import flask
from flask_bootstrap import Bootstrap
import string

app = flask.Flask(__name__)
bootstrap = Bootstrap(app)

dit = "."
dah = "-"

code_dict = {
    "a": f"{dit}{dah} ",
    "b": f"{dah}{dit}{dit}{dit} ",
    "c": f"{dah}{dit}{dah}{dit} ",
    "d": f"{dah}{dit}{dit} ",
    "e": f"{dit} ",
    "f": f"{dit}{dit}{dah}{dit} ",
    "g": f"{dah}{dah}{dit} ",
    "h": f"{dit}{dit}{dit}{dit} ",
    "i": f"{dit}{dit} ",
    "j": f"{dit}{dah}{dah}{dah} ",
    "k": f"{dah}{dit}{dah} ",
    "l": f"{dit}{dah}{dit}{dit} ",
    "m": f"{dah}{dah} ",
    "n": f"{dah}{dit} ",
    "o": f"{dah}{dah}{dah} ",
    "p": f"{dit}{dah}{dah}{dit} ",
    "q": f"{dah}{dah}{dit}{dah} ",
    "r": f"{dit}{dah}{dit} ",
    "s": f"{dit}{dit}{dit} ",
    "t": f"{dah} ",
    "u": f"{dit}{dit}{dah} ",
    "v": f"{dit}{dit}{dit}{dah} ",
    "w": f"{dit}{dah}{dah} ",
    "x": f"{dah}{dit}{dit}{dah} ",
    "y": f"{dah}{dit}{dah}{dah} ",
    "z": f"{dah}{dah}{dit}{dit} ",
    " ": "/",
}

# need to add, 0-9 and also punctuation which I didn't know could be converted to Morse code

def convert(message):
    clean_message = message.translate(str.maketrans("", "", string.punctuation))  # delete all punctuation from string
    morse_code = ""
    for char in clean_message:
        if char != "\r" and char != "\n":
            morse_code = morse_code + code_dict[char]
    return morse_code


@app.route("/", methods=["POST", "GET"])
def home():
    if flask.request.method == "POST":
        message = flask.request.form['convert-text'].lower()
        morse_code = convert(message)
        return flask.render_template("index.html", morse_code=morse_code)
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
