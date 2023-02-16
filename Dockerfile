FROM pypy:latest

WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD python garden.py