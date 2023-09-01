from os import environ

DBNAME = environ["MYSQL_DBNAME"]
DBUSER = environ["MYSQL_USER"]
DBPASSWORD = environ["MYSQL_PASSWORD"]
DBHOST = environ["MYSQL_HOST"]
DBPORT = environ["MYSQL_PORT"]
DBPORT = int(DBPORT)
