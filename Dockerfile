FROM python:3-slim
# WORKDIR app
COPY requirements.txt ./
# RUN python -m pip install --no-cache-dir -r requirements.txt
# COPY ./book.py .
# CMD gunicorn --bind 0.0.0.0:5000 wsgi:app # run flask on gunicorn server since flask prompt to not use it in production deployment 
# gunicorn is a Python WSGI
# [ "python", "./book.py" ]
