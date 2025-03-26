import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./doc/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    race_list=race_count.tolist()
    print(race_list)

    # What is the average age of men?
    #method 1
    average_age_men = df[df["sex"]=="Male"]["age"].sum() / len(df[df["sex"]=="Male"]["age"])

    #method 2
    average_age_men = df[df["sex"]=="Male"]["age"].mean() 
    print(average_age_men)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df["education"]=="Bachelors").sum()/(len(df["education"])))*100 
    print(percentage_bachelors)
    
     # # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
   
    # # with and without `Bachelors`, `Masters`, or `Doctorate`
    # method1
    higher_education = (df[advanced_education & (df["salary"] == ">50K")].shape[0] / df[advanced_education].shape[0]) * 100
    # method2
    higher_education = (df[advanced_education & (df["salary"] == ">50K")].shape[0] / len(df[advanced_education])) * 100
    print(higher_education)

    # # What percentage of people without advanced education make more than 50K?
    not_advanced_education=~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_education = (df[not_advanced_education & (df["salary"] == ">50K")].shape[0] / df[not_advanced_education].shape[0]) * 100
    print(lower_education)

    # # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    print(min_work_hours)

    # # What percentage of the people who work the minimum number of hours per week have a salary of >50K?


    num_min_workers = df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0]
    total_min_workers = df[df["hours-per-week"] == min_work_hours].shape[0]

    rich_percentage = (num_min_workers / total_min_workers) * 100 if total_min_workers > 0 else 0
    print(rich_percentage)


    # What country has the highest percentage of people that earn >50K?
    total_people_of_country= df["native-country"].value_counts()
    total_people_of_country_high_salary= df[df["salary"]==">50K"]["native-country"].value_counts()
    percentage_people=(total_people_of_country_high_salary/total_people_of_country).fillna(0)*100

    highest_earning_country = percentage_people.idxmax()
    highest_earning_country_percentage = percentage_people.max()
    print(highest_earning_country)
    print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    total_people_high_salary_IN=df[(df["native-country"]=="India") & (df["salary"]==">50K")]
    ocuupation_high_salry_people_have_IN=total_people_high_salary_IN["occupation"].value_counts()

    top_IN_occupation = ocuupation_high_salry_people_have_IN.idxmax()
    print(top_IN_occupation)

calculate_demographic_data()   
    
    