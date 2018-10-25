LOG ANALYSIS PROJECT

This is the third and the final project of udacity nanodegree FULL STACK DEVELOPER 1. In this prject we need to run the query of the three questions.

PRE-REQIUSITES
For the code to run well you need to have some softwares installed in your PC'S. Download and install from the link below.
1)Download and[install Python3](https://www.python.org/downloads/ "Title")
2)Download and[install VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 "Title")
3)Download and[install Vagrant](https://www.vagrantup.com/ "Title")
4)Download the [SQL file ]( https://github.com/IshitaMejarwar/udacity_front_end_log_analysis.git "Title")

*What is newsdata.sql?
->newsdata.sql is a database which we have to connect and fetch the answers using tables and columns.

REQUIREMENTS

For this project we have to follow the following steps:-
1) Download and install python. Open idle and then go to File -> New. A new file is opened. write the code and save it with .py extension.
2) Download and Run Virtual box.
3) Download git bash.
4) Download Vagrant. Set up vagrant in the git bash. For that First you have to run FSND Virtual Machine. Inside that go to the vagrant directory, run vagrant up.
5)Now SSH to the virtual machine with vagrant ssh or in some machine its winpty vagrant ssh.
6)The command line will now startwith vagrant. Here cd into the /vagrant folder.
7)Download the newsdata.sql. Keep it in the vagrant directory and now you ccan copy the contents of this repository here.
8) To load the database type psql -d news -f newsdata.sql.
9) To run your database type psql -d news.
10) Now you can acces the three tables by \dt and \d table commands. Access the tables and the columns.
11) Run the command to create views section here to run the python programme successfully.
12) Once you create views run the queries in $python log_analysis.py. 
 
CREATE VIEWS

1)CREATE VIEW popular_view as
  SELECT author, title, count(*) as views
  FROM articles, log
  WHERE log.path concat('%', articles.slug)
  GROUP BY articles.author,
	 articles.title
  ORDER BY views desc;
2)CREATE VIEW author_view as
  SELECT count(*) as num
  FROM authors, articles, log
  WHERE authors.id = articles.author and 
	log.path like '%'|| articles.slug
  GROUP BY name
  ORDER BY num desc;
3)CREATE view nas as
  SELECT date_trunc('day', time) "day", 
  count(status) as totals
  FROM log
  WHERE status = '404 NOT FOUND'
  GROUP by day;

CREATE view total_error as
  SELECT date_trunc('day', time) "day", 
  count(status) as totals
  FROM log
  GROUP by day;