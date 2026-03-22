# Use a secure, slim base image
FROM python:3.11-slim

# Set environment variables for Python stability
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_HOME=/home/appuser/app

# Create a non-root user and set up directory
RUN groupadd -r appgroup && useradd -r -g appgroup -m -d /home/appuser appuser
WORKDIR $APP_HOME

# Install dependencies as root, then clean up
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ingestion script and change ownership
COPY cms_feed_ingestor.py .
RUN chown -R appuser:appgroup $APP_HOME

# Switch to the non-root user
USER appuser

# Run the ingestor
CMD ["python", "cms_feed_ingestor.py"]