FROM python:3.5

COPY ./src /src
WORKDIR /src

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

CMD python app.py