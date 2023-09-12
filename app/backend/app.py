
import logging
from flask import Flask, request, jsonify
import pandas as pd

from queries.queries import Queries
from chat.chat import Chat

app = Flask(__name__)

@app.route("/get_main_data", methods=["GET"])
def initial_dashboard():
    queries = Queries()
    raw_response = queries.get_main_data(request.args.get('country'),
                                 request.args.get('city'),
                                 request.args.get('job_title'),
                                 request.args.get('cluster'),
                                 request.args.get('operation_type'))
    response = jsonify(raw_response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
        
@app.route("/get_column_data", methods=["GET"])
def column_information():
    queries = Queries()
    raw_response = queries.average_reviews_per_year(request.args.get('column_name'),
                                            request.args.get('country'),
                                            request.args.get('city'), 
                                            request.args.get('job_title'), 
                                            request.args.get('cluster'),
                                            request.args.get('operation_type'))
    response = jsonify(raw_response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
    
@app.route("/get_importance_per_cluster", methods=["GET"])
def importance_per_cluster():
    queries = Queries()
    raw_response = queries.importance_per_cluster(request.args.get('cluster'),
                                          request.args.get('country'))
    response = jsonify(raw_response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    

@app.route("/chat", methods=["GET"])
def chat():
    chat = Chat()
    raw_response = chat.ask(request.args.get('question'))
    response = jsonify(raw_response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)
