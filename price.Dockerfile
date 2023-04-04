FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
COPY ./Backend/helpers.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Frontend
COPY ./Frontend ../Frontend

COPY ./Backend/price.py .
COPY ./Backend/helpers.py .
# COPY ./Backend/app.py .
CMD [ "python", "./price.py"]
