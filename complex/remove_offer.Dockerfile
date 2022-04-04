FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install --no-cache-dir -r http.reqs.txt
COPY ./remove_offer.py ./invokes.py ./
CMD [ "python", "./remove_offer.py" ]