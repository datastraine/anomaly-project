# anomaly-project
Table of Content
* Wrangle[#Wrangle]
* Findings[#Findings]
* Data Dictionary[#Data-Dictionary]


# [Wrangle](https://github.com/datastraine/anomaly-project/blob/main/wrangle.py)
**Note:** Files for this task were provided off network and connect be retrieved from the via the net. To get access you must request access from the DBA.

After being handed the cohort.csv and the anonymized-curriculum-access.txt files, the data was prepared in a wrangle.py file and accessed by the defined student_data() function. The student_data function creates separate DataFrames(DF)for cohort.csv and anonymized-curriculum-access.txt and then combines them into a single DF called 'data' with the following alterations:
    
  * Turns the datetime column type into to a dateobject
  * Creates day (name), month, and hour columns
  * Creates a classtype, program, and location column from the program_id column
  * Sets the index to datetime
   
It then separates the WebDev and Data Science curriculums in their own DFs. Finally, it returns data, webdev, ds, and cohort DFs. A full breakdown of the code can be found [here](https://github.com/datastraine/anomaly-project/blob/main/wrangle.py). 

# Findings
A full breakdown of the findings can be found in the [exploration.ipynb](https://github.com/datastraine/anomaly-project/blob/main/exploration.ipynb) notebook. The key findings of this exploration are:
  * When a cohort views a lesson significantly more than other cohorts they do not typically surpass 20% of the total number of views for that page across all cohorts for WebDev. It is reasonable to assume this will continue for Data Science as more people go through the program.
  * The least viewed pages are typically viewed 3 times or less.
  * Students that aren't viewing pages while they are in the program typically have a daily view average of 50% less than the average views a day for the cohort. I assume these students either quit the program or have multiple user ids, but would need to dig in deeper to confirm
  * At least one user, with a high degree of certainty, was found to be engaged in web scraping.

# Data Dictionary
Below is the data dictionary


