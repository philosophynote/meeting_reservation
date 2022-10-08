FROM python:3.9.12

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

EXPOSE 8080

# Allow statements and log messages to immediately appear in the Knative logs
# ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY app.py .
CMD streamlit run app.py \
  --browser.serverAddress="0.0.0.0" \
  --server.enableCORS=false \
  --server.port="8080"