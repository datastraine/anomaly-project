- [Anomaly Project](#anomaly-project)
- [Wrangle](#wrangle)
- [Findings](#findings)
- [Data Dictionary](#data-dictionary)
  
# Anomaly Project
The goal of this project is to answer the following set of questions about users who access the CodeUp(TM) class curriculum.

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
7. Which lessons are least accessed? 

All questions except question #5 were accessed within the time constraints allowed. Below is how this project was undertaken and a summary of its findings.

# [Wrangle](https://github.com/datastraine/anomaly-project/blob/main/wrangle.py)
**Note:** Files for this task were provided off network and connect be retrieved from the via the net. To get access you must request access from the DBA.

After being handed the cohort.csv and the anonymized-curriculum-access.txt files, the data was prepared in a wrangle.py file and accessed by the defined student_data() function. The student_data function creates separate DataFrames(DF)for cohort.csv and anonymized-curriculum-access.txt and then combines them into a single DF called 'data' with the following alterations:
    
  * Turns the datetime column type into to a dateobject
  * Creates day (name), month, and hour columns
  * Creates a classtype, program, and location column from the program_id column
  * Sets the index to datetime
   
It then separates the WebDev and Data Science curriculums in their own DFs. Finally, it returns data, webdev, ds, and cohort DFs. A full breakdown of the code can be found [here](https://github.com/datastraine/anomaly-project/blob/main/wrangle.py). 

# [Findings](https://github.com/datastraine/anomaly-project/blob/main/exploration.ipynb)
A full breakdown of the findings can be found in the [exploration.ipynb](https://github.com/datastraine/anomaly-project/blob/main/exploration.ipynb) notebook. The key findings of this exploration are:
  * When a cohort views a lesson significantly more than other cohorts they do not typically surpass 20% of the total number of views for that page across all cohorts for WebDev. It is reasonable to assume this will continue for Data Science as more people go through the program.
  * The least viewed pages are typically viewed 3 times or less.
  * Students that aren't viewing pages while they are in the program typically have a daily view average of 50% less than the average views a day for the cohort. I assume these students either quit the program or have multiple user ids, but would need to dig in deeper to confirm
  * At least one user, with a high degree of certainty, was found to be engaged in web scraping.

# Data Dictionary
Below is the data dictionary

| Name  | Description  |
|---|---|
| datetime | The date and time (to the seconds) that a web page was accessed. |
| date |  The date that a web page was accessed.  |
| day | The day name that a web page was accessed. |
| hour | The hour of the day that a web page was accessed. In 24 hour format |
| month  | The two digit month that a web page was accessed. |
| ip | The ip addressed that accessed a web page  |
| page | The web page accessed.   |
| page_viewed | The web page accessed.   |
| user_id | The unique id for each user |
| cohort_id | The unique id associated for each cohort |
| name | The name associated with the cohort_id  |
| start_date | The beginning of class for a cohort  |
| end_date | The final day of class for a cohort  |
| program_id  | The unique id for a program |
| classtype | The type of class (Web or Data Science) and location of each program id |
| program  |  The type of class (Web or Data Science) of each program |
| location | The city each program is located in |
| hits | The number of web visit  |
| probability | The likelihood of the event in question happening |
| total_hits | The sum of all web visit across the sections of data being looked at |
| mean_hits | The average of all web visits across the sections of data being looked at  |
