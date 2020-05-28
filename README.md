# coronarisk
Website that tells you your risk of coronavirus based on statistics and your input data

Uses nytimes updating coronavirus data that can be found here: https://github.com/nytimes/covid-19-data

Uses historical coronavirus data from a study here: http://weekly.chinacdc.cn/en/article/id/e53946e2-c6c4-41e9-9a9b-fea8db1a8f51

Currently works for counties in the state of Maine

## calculations
Probability of being infected is calculated by (number of people infected in county with inputted traits / total population of county with inputted traits) (then times 100 for a percent)

Probability of being dead is (probability of being infected with inputted traits * (number of people dead from covid-19 in county / number of people infected with the coronavirus in the county) (then times 100 for a percent) if "None" is selected for health conditions.
If another health condition is selected, then the probability of being dead is the whichever is greater, (the county data mortality rate or the coronavirus study mortality rate for that condition) then times the probability of being infected in the county with inputted traits.
