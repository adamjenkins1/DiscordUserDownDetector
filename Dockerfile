FROM python:3.8.2-slim

COPY ./app /app
ADD ./requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -U pip \
    && pip3 install --no-cache-dir gunicorn \
    && pip3 install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "app.src.main:app"]