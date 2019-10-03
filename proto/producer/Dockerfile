FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

#wait-for-it is used to check if rabbit is stable.
RUN ["curl", "https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh", "-s" ,"--output", "wait-for-it.sh"]
RUN ["chmod", "+x", "wait-for-it.sh"]

COPY . .

CMD ["./wait-for-it.sh","my-rabbit:5672", "--", "python", "-u", "producer.py"]
