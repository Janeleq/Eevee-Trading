FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./authenticate.py ./app.py ./price.py ./
CMD [ "python", "./authenticate.py", './app.py', './price.py']
