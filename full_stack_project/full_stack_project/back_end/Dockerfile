FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR  /app

COPY . /app

RUN whereis pip3
# RUN pip3 install -r requirement.txt
RUN pip3 install psycopg2
#RUN pip install psycopg2

#Run pip install -r requirements.txt

CMD uvicorn app:app --host 0.0.0.0 --port 8000

