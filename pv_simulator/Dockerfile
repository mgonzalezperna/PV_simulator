FROM python:3

WORKDIR /usr/src/app

RUN pip install --upgrade pip poetry 

COPY ./pv_simulator ./pv_simulator
COPY ./poetry.lock ./pyproject.toml ./

#wait-for-it is used to check if rabbit is stable.
RUN ["curl", "https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh", "-s" ,"--output", "wait-for-it.sh"]
RUN ["chmod", "+x", "wait-for-it.sh"]

RUN ["poetry", "config", "settings.virtualenvs.create", "false"]
RUN ["poetry", "install"]
