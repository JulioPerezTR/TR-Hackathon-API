from flask import Flask, request, jsonify
import pandas as pd
import os.path
import json

from datasets.glassdoor_dataset import GlassdoorDataframe

class Queries():
    def __init__(self) -> None:
        self.df = GlassdoorDataframe.glassdoor_dataframe()
        self.df['review_date'] = pd.to_datetime(self.df['Review Date'], format='%d/%m/%y')
        self.df["year"] = self.df['review_date'].dt.year
    
    def get_main_data(self):
        result = {
            'totalReviews':self.total_reviews(),
            'avgSenior': self.average_reviews_per_year('Senior Leadership', operation_type = 'mean'),
            'avgCarrer': self.average_reviews_per_year('Career Opportunities', operation_type = 'mean'),
            'avgCulture': self.average_reviews_per_year('Culture & Values', operation_type = 'mean'),
            'avgCompensation': self.average_reviews_per_year('Compensation & Benefits', operation_type = 'mean'),
            'avgDiversity': self.average_reviews_per_year('Diversity & Inclusion', operation_type = 'mean'),
            'avgWork': self.average_reviews_per_year('Work-Life Balance', operation_type = 'mean')
            }
        return json.dumps(result)
    
    def total_reviews(self):
        x = []
        y = []
        
        reviews_count = list(self.df.groupby('year').size())[::-1]
        years = self.df['year'].unique()
        
        for r in zip(years, reviews_count):
            x.insert(0,str(r[0]))
            y.insert(0,int(r[1]))
            
        return {'title':'Total reviews per year', 'x':x, 'y':y}
    
    def average_reviews_per_year(self, column_name, country = '', city = '', job_title = '', cluster = '', operation_type = 'mean'):
        x = []
        y = []
            
        years = self.df['year'].unique()
        for year in years:
            x.insert(0, int(year))
            df_filtered = self.df[self.df['year']== year]
            if country:
                df_filtered = df_filtered[df_filtered['Review Country Name'] == country]
            if city:
                df_filtered = df_filtered[df_filtered['Review City Name'] == city]
            if job_title:
                df_filtered = df_filtered[df_filtered['Job Title'] == job_title]
            if cluster:
                df_filtered = df_filtered[df_filtered['cluster'] == cluster]
                
                
            if(operation_type == 'mean' or operation_type == None):
                y.insert(0, round(df_filtered[column_name].mean(), 3))
            elif(operation_type == 'max'):
                y.insert(0, round(df_filtered[column_name].max(), 3))
            elif(operation_type == 'min'):
                y.insert(0, round(df_filtered[column_name].min(), 3))
            
        return {'title':'Average ' + column_name + ' per year', 'x':x, 'y':y}