from flask import Flask
import sys

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Web service need 2 arguments: ip address and port")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port)
