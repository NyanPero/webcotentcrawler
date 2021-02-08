FROM python:3.8
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app
 
COPY requirements.txt ./
 
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
