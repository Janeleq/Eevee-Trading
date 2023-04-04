FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./Backend/authenticate.py .
# COPY ./Backend/app.py .
COPY ./Backend/price.py .
COPY ./Backend/access_wallet.py .
CMD [ "python", "./authenticate.py"]
EXPOSE 5050
