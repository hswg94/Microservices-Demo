# Use official Python image as the base
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /python-docker

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
COPY products.json products.json
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Document the port the app listens on
EXPOSE 80

# Set default port environment variable
ENV PORT=80

# Start the Flask app using the PORT env variable (shell form for env expansion)
CMD python3 -m flask run --host=0.0.0.0 -p $PORT
