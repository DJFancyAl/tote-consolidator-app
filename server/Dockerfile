# Base
FROM python

# Copy Files
COPY requirements.txt /app/
COPY app.py /app/
COPY consolidations.py /app/
COPY database_sql.py /app/
COPY data.csv /app/
COPY waitress_server.py /app/

# Change Directory
WORKDIR /app

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run waitress_server
CMD ["python", "waitress_server.py"]