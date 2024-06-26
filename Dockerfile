FROM python:3.11.6-slim
ENV SOURCE_DIR /app
RUN mkdir -p $SOURCE_DIR
WORKDIR $SOURCE_DIR

COPY requirements.txt $SOURCE_DIR
RUN pip install -r requirements.txt
COPY . $SOURCE_DIR

EXPOSE 8888

CMD ["gunicorn", "evi.api:app", "-b", "0.0.0.0:8888"]
