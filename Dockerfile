FROM python:3.8-slim

# Args
ARG APP_MAX_REQUEST_BYTES=50000000
ARG APP_WORKERS=4
ARG APP_PORT=8000
ARG APP_ENV=prod

# Set APP envs
ENV APP_MAX_REQUEST_BYTES=${APP_MAX_REQUEST_BYTES}
ENV APP_WORKERS=${APP_WORKERS}
ENV APP_PORT=${APP_PORT}
ENV APP_ENV=${APP_ENV}

# Set working directory
WORKDIR /usr/src/app

# Copy your application code
COPY ./app ./app
COPY ./static ./static

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create user
RUN adduser --disabled-password --gecos '' genie
USER genie

# Make port 8000 available to outside world
EXPOSE 8000

# Command to run your application
CMD ["python","-m","app.main"]
