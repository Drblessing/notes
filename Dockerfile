FROM python:3.8-buster
COPY ./code /code
COPY ./requirements.txt /code
COPY ./.env /code/.env
WORKDIR /code

# RUN apk add build-base
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0