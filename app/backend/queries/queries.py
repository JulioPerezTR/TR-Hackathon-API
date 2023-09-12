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
    
    def get_main_data(self, country = '', city = '', job_title = '', cluster = '', operation_type = ''):
        result = [
            self.total_reviews(country, city, job_title, cluster),
            self.average_reviews_per_year('Senior Leadership', country, city, job_title, cluster, operation_type),
            self.average_reviews_per_year('Career Opportunities', country, city, job_title, cluster, operation_type),
            self.average_reviews_per_year('Culture & Values', country, city, job_title, cluster, operation_type),
            self.average_reviews_per_year('Compensation & Benefits', country, city, job_title, cluster, operation_type),
            self.average_reviews_per_year('Diversity & Inclusion', country, city, job_title, cluster, operation_type),
            self.average_reviews_per_year('Work-Life Balance', country, city, job_title, cluster, operation_type)
        ]
        return json.dumps(result)
    
    def total_reviews(self, country = '', city = '', job_title = '', cluster = ''):
        x = []
        y = []
        
        df_filtered = self.df
        if country:
            df_filtered = df_filtered[df_filtered['Review Country Name'] == country]
        if city:
            df_filtered = df_filtered[df_filtered['Review City Name'] == city]
        if job_title:
            df_filtered = df_filtered[df_filtered['Job Title'] == job_title]
        if cluster:
            df_filtered = df_filtered[df_filtered['cluster'] == cluster]
            
            
        reviews_count = list(df_filtered.groupby('year').size())[::-1]
        years = df_filtered['year'].unique()
        
        for r in zip(years, reviews_count):
            x.insert(0,str(r[0]))
            y.insert(0,int(r[1]))
        
        average = sum(y)
        return {'title':'Total reviews per year', 'x':x, 'y':y, 'average':average}
    
    def average_reviews_per_year(self, column_name, country = '', city = '', job_title = '', cluster = '', operation_type = ''):
        x = []
        y = []
        operation_text = ''
        
        df_filtered = self.df
        if country:
            df_filtered = df_filtered[df_filtered['Review Country Name'] == country]
        if city:
            df_filtered = df_filtered[df_filtered['Review City Name'] == city]
        if job_title:
            df_filtered = df_filtered[df_filtered['Job Title'] == job_title]
        if cluster:
            df_filtered = df_filtered[df_filtered['cluster'] == cluster]
        
        print(df_filtered)
        years = df_filtered['year'].unique()
        for year in years:
            x.insert(0, str(year))
            df_year_filtered = df_filtered[df_filtered['year'] == year]
                
            print(df_year_filtered[column_name])
            if(operation_type == 'mean' or operation_type == None):
                y.insert(0, float(df_year_filtered[column_name].mean()))
                operation_text = 'Average '
            elif(operation_type == 'max'):
                y.insert(0, float(df_year_filtered[column_name].max()))
                operation_text = 'Maximum '
            elif(operation_type == 'min'):
                y.insert(0, float(df_year_filtered[column_name].min()))
                operation_text = 'Minimum '
        
        average = sum(y)/len(y)
            
        return {'title': operation_text + column_name + ' per year', 'x':x, 'y':y, 'average':average}