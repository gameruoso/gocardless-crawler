## Synopsis

A simple multithread web crawler. the page to crawl is hardcoded in main.py, just update it if you wish to run it against other websites. 


## Code

The structure is very simple, there's a Crawl class which is instanciated multiple times, but all crawlers share the same class variables in order not to have clashes between what needs to be crawled and what is been already crawled'.
Then there is a util.py class and the main.

## Motivation

Gocardless code test

## Installation
It doesn't need to be installed

unix based machine:
Just need to have python3 and virtualenv installed.
Go to the gocardless-crawler folder and run ./run.sh
It will:
- build a virtual environment
- install dependencies
- run the application
- persists results on a file (sitemap.json)
- clean up the folder

Windows machines:
Needs to have python3 installed.
Install manually two libraries via pip and run main.py:
- pip3 install requests
- pip3 install beautifulsoup4
- python3 main.py

## Tests

No time to write tests, sorry
