FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./transaction_log.py ./helpers.py ./app.py ./invokes.py ./
CMD [ "python", "./transaction_log.py" ]
