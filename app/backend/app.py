
import logging
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def initial_dashboard():
    try:
        df = glassdoor_dataframe()

        reviews = total_reviews_per_year(df)

        response = {
            'total_reviews': df.shape[0],
            'reviews_per_year': reviews
        }

        attributes = ['Senior Leadership', 'Career Opportunities', 'Culture & Values', 'Compensation & Benefits']
        for attr in attributes:
            response[attr] = mean_reviews_per_attribute(df, attr)

        return jsonify(response)
    
    except Exception as e:
        logging.exception("Exception in /shape")
        return jsonify({"error": str(e)}), 500
    
def total_reviews_per_year(df):
    try:
        df['review_date'] = pd.to_datetime(df['Review Date'], format='%d/%m/%y')
        df["year"] = df['review_date'].dt.year
        reviews_count = list(df.groupby('year').size())[::-1]
        years = df['year'].unique()

        reviews = {}
        for r in list(zip(years, reviews_count)):
            reviews[str(r[0])] = int(r[1])

        return dict(reviews)

    except Exception as e:
        return str(e)

def mean_reviews_per_attribute(df, attribute):
    try:
        years = df['year'].unique() 

        means = {}
        for year in years:
            means[str(year)] = df[df['year']== year][attribute].mean()
            
        return dict(means)

    except Exception as e:
        return str(e)
    
def reviews_per_attribute(df, attribute, function):
    try:
        years = df['year'].unique() 
        means = {}

        for year in years:
            if function == 'max':
                means[str(year)] = df[df['year']== year][attribute].max()
            elif function == 'min':
                means[str(year)] = df[df['year']== year][attribute].min()
            elif function == 'mean':
                means[str(year)] = df[df['year']== year][attribute].mean()
            elif function == 'sum':
                means[str(year)] = df[df['year']== year][attribute].sum()
            else:
                pass
            
        return dict(means)

    except Exception as e:
        return str(e)


@app.route("/shape", methods=["GET"])
def df_shape():
    
    try:
        df = glassdoor_dataframe()

        return jsonify({"totalReviews": df.shape[0]})
    
    except Exception as e:
        logging.exception("Exception in /shape")
        return jsonify({"error": str(e)}), 500
    
@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        pass

    except Exception as e:
        logging.exception("Exception in /analyze") 
        return jsonify({"error": str(e)}), 500


def glassdoor_dataframe():
    try:
        csv_file_path = '.\data\GlassdoorDataset.csv'
        df = pd.read_csv(csv_file_path)

        return df

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
