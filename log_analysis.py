#!/usr/bin/env python
import psycopg2
import bleach

DMNAME = "news"


def run_query(query):
        db = psycopg2.connect('dbname'=DBNAME)
try:
        db = psycopg2.connect('dbname'=DBNAME)
except:
        print ("Unable to connect to the database")
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows


def get_top_articles():
    """Top 3 articles"""
'#'Query string
qurey = """ SELECT title,views
FROM popular_view
limit 3;"""

'#'Run
results = run_query(query)

'#'Print Result
print('\nTOP THREE ARTICLES:')
count = 1
for i in results:
    number = '(' + str(count) + ')'
title = i[0]
views = 'with' + str(i[1]) + "views"
print(number+title+views)
count += 1


def get_top_authors():
                """Top 3 authors"""
'#'Query string
query = """SELECT name,num
FROM author_view
LIMIT 5;"""
'#'Run
results = run_query(query)
print('\n TOP AUTHORS')
count = 1
for i in results:
    print ('(' + str(count)+')' + i[0] + 'with' + str(i[1]) + "views")
count += 1


def get_daily_errors():
        """return days with more than 1% errors"""
'#'Build query string
query = """SELECT to_char (nas.day,'MM/DD/YYYY')
round(
(nas.totals*1.0/request_totals.totals*1.0)*100>2)
as percentage
FROM nas, view_total
where nas.day = view_total.day
AND
(nas*1.0/view_total.total*1.0)*100>1
order by percentage desc"""

print('Calculating Results...\n')
get_top_articles()
get_top_authors()
get_daily_errors()
