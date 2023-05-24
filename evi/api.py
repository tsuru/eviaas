from flask import Flask

import os


app = Flask(__name__)
app.debug = os.environ.get("API_DEBUG", "0") in ("True", "true", "1")


@app.route("/")
def index():
    return "tsuru/eviaas running", 200


@app.route("/resources", methods=["POST"])
def add_instance():
    return "", 201


@app.route("/resources/<name>", methods=["PUT"])
def update_instance(name):
    return "", 200


@app.route("/resources/<name>", methods=["DELETE"])
def remove_instance(name):
    return "", 200


@app.route("/resources/<name>/bind", methods=["DELETE"])
@app.route("/resources/<name>/bind-app", methods=["DELETE"])
def unbind(name):
    return "", 200


@app.route("/resources/<name>/bind", methods=["POST"])
@app.route("/resources/<name>/bind-app", methods=["POST"])
@app.route("/resources/<name>/binds/jobs/<job-name>", methods=["PUT"])
def bind(name):
    return os.environ.get("EVI_ENVIRONS", "{}"), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
