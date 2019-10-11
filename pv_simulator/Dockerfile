FROM python:3

WORKDIR /usr/src/app

RUN pip install --upgrade pip poetry 

COPY ./pv_simulator ./pv_simulator
COPY ./poetry.lock ./pyproject.toml ./

RUN ["poetry", "config", "settings.virtualenvs.create", "false"]
RUN ["poetry", "install"]
