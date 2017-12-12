#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2

# The queries for easy copy + pasting with their titles

query1Title = 'What are the most popular three articles of all time?'
query1 = \
    """
    SELECT articles.title, count(*) as cnt
    from articles
    join log
    on log.path like concat('/article/%', articles.slug)
    group by articles.title
    order by cnt desc
    limit 3;
    """

query2Title = 'Who are the most popular article authors of all time?'
query2 = \
    """
    SELECT authors.name, count(*) as cnt
    from articles inner
    join authors on articles.author = authors.id inner join log
    on log.path like concat('%', articles.slug, '%')
    where log.status like '%200%'
    group by authors.name
    order by cnt desc
 """

query3Title = \
    'On which days did more than 1% of requests lead to errors?'
query3 = \
    """
    SELECT date,total,error, (error::float*100)/total::float as percent
    from (select time::timestamp::date as Date, count(status) as total,
    sum(case when status = '404 NOT FOUND' then 1 else 0 end) as error
    from log group by time::timestamp::date) as res
    where (error::float*100)/total::float > 1.0
    order by percent desc;
    """


# runs the query and returns the results

def run_query(query):
    db = psycopg2.connect('dbname=' + 'news')
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


# running and printing the queries

def topArticles():
    res = run_query(query1)
    print '\n' + query1Title
    for i in range(0, len(res), 1):
        print '\n' + str(i + 1) + ')' + res[i][0] + ' - ' \
            + str(res[i][1]) + ' views'


def popularAuthors():
    res = run_query(query2)
    print '\n' + query2Title
    for i in range(0, len(res), 1):
        print '\n' + str(i + 1) + ')' + res[i][0] + '" - ' \
            + str(res[i][1]) + ' views'


def errors():
    res = run_query(query3)
    print '\n' + query3Title
    for i in range(0, len(res), 1):
        print str(res[i][0]) + ' - ' + str(round(res[i][3], 2)) \
            + '% errors'


# call the three functions in main

if __name__ == '__main__':
    topArticles()
    popularAuthors()
    errors()
