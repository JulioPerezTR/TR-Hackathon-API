
import logging
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def initial_dashboard():
    csv_file_path = '.\data\GlassdoorV2.csv'  # Replace with the path to your CSV file
    json_data = csv_to_json(csv_file_path)

    return json_data.to_json()
    
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

    
def csv_to_json(csv_file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Convert the DataFrame to JSON
        df_tier=pd.DataFrame(df[(df['tier']=='TierI') & (df['cluster']==10)]['Cons'])

        return df_tier

    except Exception as e:
        return str(e)



if __name__ == "__main__":
    app.run(debug=True)
