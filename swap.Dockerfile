FROM python:3-slim
WORKDIR /usr/src/app/Backend
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./swap.py ./invokes.py ./
CMD [ "python", "./swap.py", './invokes.py' ]
