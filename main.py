import pandas as pd
class VideoanalyticsEngine:
    def __init__(self,csv_file):
       self._df = pd.read_csv(csv_file)
    def Calculate_dropoff(self):
       self._df['dropoff_rate']=self._df['Retention_Min5']-self._df['Retention_End']
       self._df['High_Dropoff_Alert']=self._df['dropoff_rate'] > 30
    def Engimant_score(self):
       self._df['Engimant_score']=((self._df['Likes'] + (self._df['Comments'] * 2)) / self._df['Views']) * self._df['Retention_End']
    def Category(self):
      return  self._df.groupby('Category').agg(['sum', 'count', 'max', 'min'])
obj = VideoanalyticsEngine('Video_ID VID_50.CSV')
obj.Calculate_dropoff()
obj.Engimant_score()
print(obj.Category())
print(obj._df)
