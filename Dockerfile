FROM python:3.9
 
WORKDIR /openweather-test
COPY . /openweather-test
 
RUN pip install -r requirements.txt
