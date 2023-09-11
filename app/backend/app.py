
import logging
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route("/chat", methods=["POST"])
def chat():
    
    try:
        pass
    
    except Exception as e:
        logging.exception("Exception in /chat")
        return jsonify({"error": str(e)}), 500
    
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        pass

    except Exception as e:
        logging.exception("Exception in /analyze") 
        return jsonify({"error": str(e)}), 500

    

if __name__ == "__main__":
    app.run(debug=True)
