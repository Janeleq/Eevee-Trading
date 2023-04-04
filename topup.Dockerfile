FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
COPY helpers.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

# Frontend
COPY ./Frontend ../Frontend

# Backend
COPY ./Backend/topup.py .
COPY ./Backend/helpers.py .
COPY ./Backend/invokes.py .
COPY ./Backend/swap.py .

# COPY ./Backend/app.py .
CMD [ "python", "./topup.py" ]
