import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts(['race'], dropna=True)

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == "Male"]["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df.loc[df["education"] == 'Bachelors']["education"].count()/df["education"].count()).round(3)*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    educationList = ["Bachelors", "Masters", "Doctorate"]
  
    higher_education = df.loc[df["education"].isin(educationList)]
    print(higher_education.loc[df['salary'] != "<=50K"]["education"].count())
    lower_education = df.loc[~df["education"].isin(educationList)]

    

    # percentage with salary >50K
    higher_education_rich = (higher_education.loc[df['salary'] != "<=50K"]["education"].count()/higher_education["education"].count()).round(3) *100
  
    lower_education_rich = (lower_education.loc[df['salary'] != "<=50K"]["education"].count()/lower_education["education"].count()).round(3) *100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    print(df["hours-per-week"].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    all_rich = df.loc[df["salary"] == ">50K"]

    lowHourTotal = df.loc[df["hours-per-week"] == min_work_hours]["hours-per-week"].count()
    lowHourRich = all_rich.loc[all_rich["hours-per-week"] == min_work_hours]["hours-per-week"].count()
  
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours]["hours-per-week"].count()

    rich_percentage = num_min_workers/lowHourRich

    # What country has the highest percentage of people that earn >50K?
    test1 = all_rich.value_counts("native-country")
    test2 = df.value_counts("native-country")
  
    highest_earning_country = test1.div(test2).idxmax()
    highest_earning_country_percentage = test1.div(test2).max().round(3)*100
    print(test1.div(test2).max())
  

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df["salary"] != ">50k") & (df["native-country"] == "India")].value_counts('occupation').index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print(lowHourTotal/lowHourRich)
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
