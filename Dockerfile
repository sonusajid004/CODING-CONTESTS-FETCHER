FROM python:3.8-slim-buster

COPY . /home/user/app/
WORKDIR /home/user/app
RUN python3 -m pip install -r requirements.txt
EXPOSE 27017
CMD python app.py