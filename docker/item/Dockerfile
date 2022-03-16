# Docker client uses a Dockerfile to build an image.
# A Dockerfile is a simple text-file that contains a list of commands. 

FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./item.py .
CMD [ "python", "./item.py" ]
