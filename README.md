# coronarisk
Website that tells you your risk of coronavirus based on statistics and your input data

Uses nytimes coronavirus data that can be found here: https://github.com/nytimes/covid-19-data

Currently works for counties in the state of Maine

## calculations
Probability of being infected is calculated by (number of people infected in county / total population of county) (then times 100 for a percent)

Probability of being dead is (probability of being infected * (number of people dead from covid-19 in county / number of people infected with the coronavirus in the county) (then times 100 for a percent)
