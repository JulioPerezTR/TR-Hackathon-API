
import logging
from flask import Flask, request, jsonify
import pandas as pd

from queries.queries import Queries

app = Flask(__name__)

@app.route("/get_main_data", methods=["GET"])
def initial_dashboard():
    queries = Queries()
    if not request.args.get('column_name'):
        return queries.get_main_data()
    else:
        return queries.average_reviews_per_year(request.args.get('column_name'), 
                                                request.args.get('country'), 
                                                request.args.get('city'), 
                                                request.args.get('job_title'), 
                                                request.args.get('cluster'),
                                                request.args.get('operation_type'))


if __name__ == "__main__":
    app.run(debug=True)
