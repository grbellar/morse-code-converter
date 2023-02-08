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
    "1": f"{dit}{dah}{dah}{dah}{dah}",
    "2": f"{dit}{dit}{dah}{dah}{dah}",
    "3": f"{dit}{dit}{dit}{dah}{dah}",
    "4": f"{dit}{dit}{dit}{dit}{dah}",
    "5": f"{dit}{dit}{dit}{dit}{dit}",
    "6": f"{dah}{dit}{dit}{dit}{dit}",
    "7": f"{dah}{dah}{dit}{dit}{dit}",
    "8": f"{dah}{dah}{dah}{dit}{dit}",
    "9": f"{dah}{dah}{dah}{dah}{dit}",
    "0": f"{dah}{dah}{dah}{dah}{dah}",
    ",": f"{dah}{dah}{dit}{dit}{dah}{dah}",
    ".": f"{dit}{dah}{dit}{dah}{dit}{dah}",
    "?": f"{dit}{dit}{dah}{dah}{dit}{dit}",
    ";": f"{dah}{dit}{dah}{dit}{dah}{dit}",
    ":": f"{dah}{dah}{dah}{dit}{dit}{dit}",
    "/": f"{dah}{dit}{dit}{dah}{dit}",
    "-": f"{dah}{dit}{dit}{dit}{dit}{dah}",
    "'": f"{dit}{dah}{dah}{dah}{dah}{dit}",
    '"': f"{dit}{dah}{dit}{dit}{dah}{dit}",
    "(": f"{dah}{dit}{dah}{dah}{dit}",
    ")": f"{dah}{dit}{dah}{dah}{dit}{dah}",
    "=": f"{dah}{dit}{dit}{dit}{dah}",
    "+": f"{dit}{dah}{dit}{dah}{dit}",
    "X": f"{dah}{dit}{dit}{dah}",  # TODO: supposed to be multipy sign but will also return letter "x" which is wrong
    "@": f"{dit}{dah}{dah}{dit}{dah}{dit}"
}


def get_bad_chars(message):
    bad_char_list = []
    for char in message:
        if char not in code_dict:
            if char != "\r" and char != "\n":
                bad_char_list.append(char)
    return bad_char_list


def convert(message):
    # clean_message = message.translate(str.maketrans("", "", string.punctuation))  # delete all punctuation from string
    morse_code = ""
    bad_char_list = get_bad_chars(message)
    if bad_char_list:  # if not empty
        return message, bad_char_list
    else:
        for char in message:
            if char != "\r" and char != "\n":
                morse_code = morse_code + code_dict[char]
        return morse_code


@app.route("/", methods=["POST", "GET"])
def home():
    if flask.request.method == "POST":
        message = flask.request.form['convert-text'].lower()
        morse_code = convert(message)
        # I am either a genius or have gone completely mad. There is no doubt a better way to highlight the bad chars
        # but this is the only way I could think of to generate the html to highlight characters.
        if type(morse_code) is tuple:
            html = "<p class='m-3'>"
            for char in morse_code[0]:
                if char in morse_code[1]:  # if current char is in the bad_char_list, highlight it red
                    html = html + f"<span style='color: red'>{char}</span>"
                else:
                    html = html + char
            html = html + "</p>"
            return flask.render_template("index.html", error=True, html=html)
        else:
            return flask.render_template("index.html", error=False, morse_code=morse_code)
    return flask.render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
