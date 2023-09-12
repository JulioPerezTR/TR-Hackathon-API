from flask import Flask, request, jsonify
import pandas as pd
import os.path
import json
import numpy as np
import pandas as pd
from datetime import datetime
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

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
        return result
    
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
            df_filtered = df_filtered[df_filtered['cluster'] == int(cluster)]
        
        #print(df_filtered)
        years = df_filtered['year'].unique()
        for year in years:
            x.insert(0, str(year))
            df_year_filtered = df_filtered[df_filtered['year'] == year]
                
            #print(df_year_filtered[column_name])
            if(operation_type == 'mean' or operation_type == None):
                y.insert(0, float(df_year_filtered[column_name].mean()))
                operation_text = 'Average '
            elif(operation_type == 'max'):
                y.insert(0, float(df_year_filtered[column_name].max()))
                operation_text = 'Maximum '
            elif(operation_type == 'min'):
                y.insert(0, float(df_year_filtered[column_name].min()))
                operation_text = 'Minimum '
        if len(y) == 0:
            average = 0
        else:
            average = sum(y)/len(y)
            
        return {'title': operation_text + column_name + ' per year', 'x':x, 'y':y, 'average':average}
    
    
    def importance_per_cluster(self, cluster, country = ''):
        df_light=self.df[['Overall Satisfaction','Work-Life Balance','Culture & Values','Career Opportunities','Compensation & Benefits','Senior Leadership','cluster','tier', 'Review Country Name']]

        df_cluster=df_light[(df_light['cluster']==cluster)]
        if country:
            df_cluster = df_cluster[df_cluster['Review Country Name'] == country]
            
        df_cluster=df_cluster[['Overall Satisfaction','Work-Life Balance','Culture & Values','Career Opportunities','Compensation & Benefits','Senior Leadership']]

        analysis = self.conjoint_analysis(df_cluster)
        dict_res = analysis.to_dict(orient='records')

        response = {}
        for importance in dict_res:
            response[importance['attr']] = importance['relative_importance'] 

        response['cluster_id'] = cluster

        return response
    
    
    
    def conjoint_analysis(self, df_rating):
        x = df_rating[[x for x in df_rating.columns if  x != 'Overall Satisfaction']]
        xdum = pd.get_dummies(x, columns=[c for c in x.columns])
        y = df_rating['Overall Satisfaction']
        res = sm.OLS(y, xdum, family=sm.families.Binomial()).fit()

        df_res = pd.DataFrame({
            'param_name': res.params.keys()
            , 'param_w': res.params.values
            , 'pval': res.pvalues
        })

        # adding field for absolute of parameters
        df_res['abs_param_w'] = np.abs(df_res['param_w'])
        # marking field is significant under 95% confidence interval
        df_res['is_sig_95'] = (df_res['pval'] < 0.05)
        # constructing color naming for each param
        df_res['c'] = ['blue' if x else 'red' for x in df_res['is_sig_95']]
        # make it sorted by abs of parameter value
        df_res = df_res.sort_values(by='abs_param_w', ascending=True)

        range_per_feature = dict()
        for key, coeff in res.params.items():
            sk =  key.split('_')
            feature = sk[0]
            if len(sk) == 1:
                feature = key
            if feature not in range_per_feature:
                range_per_feature[feature] = list()

            range_per_feature[feature].append(coeff)

        # importance per feature is range of coef in a feature
        # while range is simply max(x) - min(x)
        importance_per_feature = {
            k: max(v) - min(v) for k, v in range_per_feature.items()
        }

        # compute relative importance per feature
        # or normalized feature importance by dividing
        # sum of importance for all features
        total_feature_importance = sum(importance_per_feature.values())
        relative_importance_per_feature = {
            k: 100 * round(v/total_feature_importance, 3) for k, v in importance_per_feature.items()
        }
            
        alt_data = pd.DataFrame(
            list(relative_importance_per_feature.items()),
            columns=['attr', 'relative_importance']
        ).sort_values(by='relative_importance', ascending=False)
            
        return alt_data