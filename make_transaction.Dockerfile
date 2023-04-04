FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Frontend
COPY ./Frontend ../Frontend

# Backend
COPY ./Backend/make_transaction.py .
COPY ./Backend/helpers.py .
COPY ./Backend/invokes.py .
COPY ./Backend/price.py .
COPY ./Backend/authenticate.py .
COPY ./Backend/checkOrder.py .
CMD [ "python", "./make_transaction.py"]
