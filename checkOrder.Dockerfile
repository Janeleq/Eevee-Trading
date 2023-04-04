FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Frontend
COPY ./Frontend ../Frontend

# Backend
COPY ./Backend/check_order.py .
COPY ./Backend/access_wallet.py .
COPY ./Backend/price.py .
COPY ./Backend/helpers.py .
CMD [ "python", "./check_order.py"]
