FROM pypy:latest
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app
CMD python garden.py