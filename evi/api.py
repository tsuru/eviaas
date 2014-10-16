from flask import Flask

import os


app = Flask(__name__)
app.debug = os.environ.get("API_DEBUG", "0") in ("True", "true", "1")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
