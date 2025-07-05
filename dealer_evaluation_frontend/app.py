from flask import Flask
from flask_cors import CORS
from flask import send_from_directory
import os

app = Flask("Product deal check")
CORS(app)


@app.route("/")
def getHomePage():
    return send_from_directory("html", "index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(port=port, debug=True)
    # When no port is specified, starts at default port 5000
