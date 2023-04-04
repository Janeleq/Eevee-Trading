FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./price.py ./helpers.py ./app.py ./
CMD [ "python", "./price.py", './helpers.py', './app.py']
