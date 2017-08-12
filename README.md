# Understanding-EducationSystem-Twitter-Sentiment

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

