curl https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv | grep "Maine" > mainecounties.csv

python3 csv-json.py
