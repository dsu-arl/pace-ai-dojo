FROM python:3.9-slim

USER root

COPY requirements.txt /requirements.txt

# Install any tools or configure anything:
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

USER hacker