FROM python:3-slim
WORKDIR /usr/src/app
COPY amqp.reqs.txt ./
RUN python -m pip install --no-cache-dir -r amqp.reqs.txt
COPY ./notifications.py ./amqp_setup.py ./
CMD [ "python", "./notifis.py" ]
#CMD [ "python", "./twillio_notifis.py" ]