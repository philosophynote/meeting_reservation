FROM python:3.9.12
EXPOSE 80
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

# Allow statements and log messages to immediately appear in the Knative logs
# ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY main.py .
CMD ["uvicorn", "main:app","--reload" ,"--host", "0.0.0.0", "--port", "80"]