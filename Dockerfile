FROM python:3.7.3-slim

# Install Pipenv
RUN pip install pipenv
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Install dependencies
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --system

COPY . /udc
WORKDIR /udc

RUN useradd -ms /bin/bash udc
RUN chown -R udc:udc /udc
USER udc

CMD python ./app/fizzbuzz.py
