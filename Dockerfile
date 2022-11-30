FROM python:3.8

RUN mkdir /app

WORKDIR /app

# Add source files

ADD . /app

# Install dependencies

RUN python -m pip install -r requirements.txt

# Install package

RUN python -m pip install . --upgrade

# Prepare API port

EXPOSE 5000

# Start application

CMD ["beer_recognition_api"]