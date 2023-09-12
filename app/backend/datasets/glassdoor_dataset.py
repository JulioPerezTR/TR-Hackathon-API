import pandas as pd
import os.path

class GlassdoorDataframe():
    def __init__(self) -> None:
        pass
    
    def glassdoor_dataframe():
        try:
            csv_file_path = os.path.dirname(__file__) + '/../data/GlassdoorV2.csv'
            df = pd.read_csv(csv_file_path)
            return df
        except Exception as e:
            return str(e)