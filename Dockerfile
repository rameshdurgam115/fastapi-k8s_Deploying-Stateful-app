FROM python:3.11-slim

# 1) Upgrade pip
RUN python -m pip install --upgrade pip

WORKDIR /app

# 2) Copy & install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copy your application code
COPY main.py .

# 4) Expose port & run
EXPOSE 8000
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
