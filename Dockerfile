FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Environment variables to optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy and install Python dependencies
COPY ./requirements.pip ./requirements.pip
RUN pip install --upgrade pip && \
    pip install -r requirements.pip

# Copy application files
COPY ./run.py ./run.py
COPY ./entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Define the entrypoint for the container
ENTRYPOINT ["/entrypoint.sh"]