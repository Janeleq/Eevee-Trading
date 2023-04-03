FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./topup.py ./helpers.py ./
CMD [ "python", "./topup.py" ]
