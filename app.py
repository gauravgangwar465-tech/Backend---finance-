from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Finance backend running"}

@app.route("/add-expense", methods=["POST"])
def add_expense():
    data = request.json
    return {"status": "success", "received": data}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
