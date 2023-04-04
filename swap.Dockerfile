FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
COPY ./Backend/helpers.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Frontend
COPY ./Frontend ../Frontend

# Backend
COPY ./Backend/swap.py .
COPY ./Backend/invokes.py .
COPY ./Backend/amqp_setup.py .
CMD [ "python", "./swap.py"]
