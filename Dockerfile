FROM ubuntu


# ENV MYSQL_DBNAME ${MYSQL_DBNAME}
# ENV MYSQL_USER ${MYSQL_USER}
# ENV MYSQL_PASSWORD ${MYSQL_PASSWORD}
# ENV MYSQL_HOST ${MYSQL_HOST}
# ENV MYSQL_PORT ${MYSQL_PORT}
# sudo docker container run -e MYSQL_PORT=$MYSQL_PORT -e MYSQL_DBNAME=$MYSQL_DBNAME -e MYSQL_USER=$MYSQL_USER -e MYSQL_DBNAME=$MYSQL_DBNAME -e MYSQL_PASSWORD=$MYSQL_PASSWORD -e MYSQL_HOST=$MYSQL_HOST bug_tracker
# sudo docker container run --network='host' -e MYSQL_PORT=$MYSQL_PORT -e MYSQL_DBNAME=$MYSQL_DBNAME -e MYSQL_USER=$MYSQL_USER -e MYSQL_DBNAME=$MYSQL_DBNAME -e MYSQL_PASSWORD=$MYSQL_PASSWORD -e MYSQL_HOST=$MYSQL_HOST bug_tracker

WORKDIR /bug_tracker
COPY . /bug_tracker/
RUN apt install bash
RUN chown -R root /bug_tracker/

RUN apt update && apt install -y python3-dev python3-pip
RUN curl https://get.trunk.io -fsSL | bash


RUN python3 -m pip install -U pip
RUN python3 -m pip install -U virtualenv poetry
RUN apt install -y build-essential pkg-config
RUN apt install -y default-libmysqlclient-dev
RUN poetry install
CMD ["poetry", "run", "uvicorn", "tracker.main:api", "--reload"]