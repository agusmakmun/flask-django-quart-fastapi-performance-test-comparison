from quart import Quart, jsonify

app = Quart(__name__)


@app.route("/api/dummy", methods=["GET"])
async def dummy_endpoint():
    return jsonify({"message": "Hello from dummy endpoint!", "status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
