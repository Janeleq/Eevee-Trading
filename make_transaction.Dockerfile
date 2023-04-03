FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./make_transaction.py ./helpers.py ./invokes.py ./
CMD [ "python", "./make_transaction.py" ]
