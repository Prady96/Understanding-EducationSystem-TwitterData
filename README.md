# Analysis of Twitter Sentiments on Quality of Education Provided in Indian Schools
In This we have taken Out Live data from twitter Website and we have tried to analyse on different aspects of education hashtags . We have considered various hashtags and famous trends from them categorise each comment as Positive, Negative and Neutral , via this we have plot pie - charts each of these sections

# Working & All the Related Datasets and Codes:

In this to take out data from twitter we wrote code in python which is written in analyse.py after executing this file an excel sheet would be formed , After every tweet there would be a categorisation weather this tweet is positive or negative 

So now we have plotted this positive and negative comments in form of pie-charts from pandas-plot.py to analyse them better after this we have compared them with the original conditions that is going on 

We have added all the dataSets on github along with codes and datasets that we considered for different hashtags

#cramming 		-> cramming.csv
#DropOut 		-> dropout.csv
#EducationInIndia 	-> edindia.csv
#hometuitions 	 -> hometuitions.csv
#NITIAayog 		-> NITIAayog.csv
#SarvSikshaAbhyan 	-> SSA.csv
#Tutions 		-> tutions.csv

Government dataSet:
U-DISE-SchoolEducationInIndia

# twitter-sentiment
A command line utility to analyse twitter sentiment for any given topic and writes output to a CSV file.

## Installing
```
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
create a `.env` file and with the following contents
```
CONSUMER_KEY=<consumer key here>
CONSUMER_SECRET=<consumer secret here>
ACCESS_TOKEN=<access token here>
ACCESS_TOKEN_SECRET=<access token secret here>
```

## Running
```
(venv) $ ./analyse.py [query] [outfile] --threshold [threshold] --limit [limit]
```
For eg.
```
(venv) $ ./analyse.py "obama" obama.csv --threshold 0 --limit 5 
```
