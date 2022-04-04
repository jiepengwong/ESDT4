FROM python:3-slim
WORKDIR /usr/src/app
COPY http.reqs.txt ./
RUN python -m pip install --no-cache-dir -r http.reqs.txt
COPY ./leave_rating.py ./invokes.py ./
CMD ["python", "./leave_rating.py"]
