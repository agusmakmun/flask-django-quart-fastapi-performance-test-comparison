from asgiref.wsgi import WsgiToAsgi
from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/api/dummy", methods=["GET"])
def dummy_endpoint():
    return jsonify({"message": "Hello from dummy endpoint!", "status": "success"})


# Create ASGI application
asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run(debug=True)
