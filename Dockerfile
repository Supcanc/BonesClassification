FROM python:3.11

WORKDIR /workdir

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "server/app.py" ]