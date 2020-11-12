import pandas as pd
import numpy as np

'''
Files for this ask were provided off network and connect be retrived from the web. You must request access to them from the DBA

* Pulls in the CodeUp anonymized student access data from a text file into a DF and renames the columns .
* Merges the cohort data from the cohort.csv file with the student data
* Sets the index to datetime
* Creates a classtype, program, and location columns from program_id...
   and knowing which cohort belongs to which program ID
* Creates seperate data frames for webdev and data science (ds) users
* returns data, webdev, and ds dataframes
'''
def student_data():
    # Reads the data from the anonymized-curriculum-access.txt into a DF
    data = pd.read_csv('anonymized-curriculum-access.txt', sep=" ", header=None, na_values='"-"')
    # Rename columns as needed
    data.columns=['date', 'time', 'page_viewed','user_id','cohort_id','ip']
    # Combine the date time columns and convert it to a datetimeobj
    data['datetime'] = data['date'] + ' ' + data['time']
    data['datetime'] = pd.to_datetime(data.datetime)
    # Create a columns for hour, day name, and month
    data['hour'] = data['datetime'].dt.hour
    data['day'] = data['datetime'].dt.day_name()
    data['month'] = data['datetime'].dt.month_name()
    #Set the index to the new datetime column and sort it
    # Read the cohort data Zach gave us into a Df
    cohort = pd.read_csv('cohorts.csv')
    # Merge the cohort data onto usage df 
    data = data.merge(cohort, on='cohort_id', how='left')
    # Create an empty column to hold classtype 
    data['classtype'] = 'x'
    # Use .loc and column name to create classtype values from class id
    data.loc[data['program_id'] == 1, 'classtype'] = 'Web-SanAntonio'
    data.loc[data['program_id'] == 2, 'classtype'] = 'Web-Dallas'
    data.loc[data['program_id'] == 3, 'classtype'] = 'DataScience-SanAntonio'
    data.loc[data['program_id'] == 4, 'classtype'] = 'Web-Houston'
    #Then split the class type column into two on -
    data[['program','location']] = data.classtype.str.split("-",expand=True) 
    # Create seperate data fames for web and datascience
    web = data[data['program']=='Web']
    ds = data[data['program']=='DataScience']
    # sort the values by datetime
    ds = ds.sort_values(by='datetime')
    web = web.sort_values(by='datetime')
    # set the index to datetime
    ds=ds.set_index('datetime')
    web=web.set_index('datetime')
    return data, web, ds