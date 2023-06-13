# IrrCertifications
    Isaac Perks
    06/01/2023

# Description
A collection of code and projects used to complete various certifications I'm working on. Details about each project will be sectioned in this description. Details will include modificaitons I needed to make, goals I completed, and the tools I needed to use. A variety of these projects contains partially completed code and specific tools to test/grade them on the certification website, which may not be relevant here but are included. This servers as a back-up of code and proof of partial completion before recieving a certification itself.

## Data Analysis with Python
From freecodecamp.org "read data from sources like CSVs and SQL, and how to use libraries like Numpy, Pandas, Matplotlib, and Seaborn to process and visualize data". The completion of this certification is broken up into 5 projects. All 5 projects are completed on replit.com imported from the freecodecamp's provided git repo.

#### Completed
* Uploaded zips of replit, including boilerplate files and data. All provided by freecodecamp.org
* PDF copy of certificate can be found in the root folder for the data analysis project

https://www.freecodecamp.org/certification/Isaac_Perks/data-analysis-with-python-v7

### Mean-Varience-Standard Deviation Calculator
"output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix."

We take in any list of 9 digits, this list is converted into a 3x3 matrix and a dictionary is returned with the above requirements.
- Initially check for out of bounds array values and valid inputs
- convert the list of numbers using numpy reshape to a structure of 3x3
- Use this matrix list to create a dictionary using numpys flatten, tolist, mean functions
- Do the same for variance, std deviation, max, min, sum numpy functions
- Return dictionary containing completed values

### Demographic Data Analyzer
Analyze given CSV of demographic data
- Convert CSV to pandas dataframe
- Manipulate and modify dataframe to check various stats
    - Race total count
    - Average age of men
    - % of people with bachelors degree
    - % of people with and without advanced educations
    - % with salary > 50k, based on education
    - Min hours worked in demographic
    - % of min hours worked with >50k
    - Country with highest % of >50k people
    - Most popular occupation of >50k in india

### Medical Data Visualizer
Using a given CSV for medical data, I'm asked to visualize it by reformating the data and posting it to various types of plots/maps
- Import CSV into pandas variable
- flatten data into long form groups of medical data to a patients ID
- Reformat data to group it by cardio, showing each individual feature
- Send reformated data to a matplotlib Categorical Plot

### Page View Time Series Visualizer
A CSV provides date and view amounts of forum page views for freecodecamp.org.
- Import CSV file and parse data to organaize date values into pandas series and properly index the dataframe
- Remove outlier data for page views, high and low end
- Organize date formats, group data into various forms based on year/month
- Create a Line Plot containing total dates and values from the file
- Create a bar-plot sorted by month on the x-axis and grouped by year. Colored and placed on a legend
- Create 2 box-plots, one for yearly for trending views and the other monthly for seasonal differences

### Sea Level Predictor
Import CSV Data from Sea level adjustments between 1880 and 2013
- Create a scatterplot of data based on that information
- Use Scipy's line regression to create a model based on the change in sea level between 1880 to 2013
    - Use said model to predict sea levels by 2050 and plot a line along the graph
- Use previous data to create a new model from 2000 to 2013
    - Use this new model to predict a different line by 2050 and plot this along the graph as well


## Scientific Computing with Python

### Arithmetic Formatter
Create a formatter that takes in a standard x + y or x - y operation and formats it vertically, all inputs/outputs are strings
from 1234 - 432 to:
  1234
-  432
------
   802

*To be Filled In
