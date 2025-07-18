# Start with a standard Python environment
FROM python:3.9-slim

# Set the main folder for our app inside the container
WORKDIR /app

# Copy the shopping list and install the libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our application code into the folder
COPY app.py .

# Tell the world our container uses this port
EXPOSE 8080

# The command to start our app using the production server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
