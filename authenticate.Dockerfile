FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
COPY ./Backend/helpers.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./Backend/authenticate.py .
COPY ./Backend/helpers.py .
COPY ./Backend/swap.py .
COPY ./Backend/price.py .
COPY ./Backend/access_wallet.py .
COPY ./Backend/make_transaction.py .
COPY ./Backend/invokes.py .
COPY ./Backend/price.py .
COPY ./Backend/check_order.py .
CMD [ "python", "./authenticate.py"]
# EXPOSE 5050
