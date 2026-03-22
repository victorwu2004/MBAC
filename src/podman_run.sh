podman run -d \
  --name cms-feed-ingestor \
  --user appuser \
  --security-opt label=disable \
  -v ./data/incoming:/home/appuser/app/incoming:Z \
  -v ./logs:/home/appuser/app/logs:Z \
  -e AWS_ACCESS_KEY_ID="your_key" \
  -e AWS_SECRET_ACCESS_KEY="your_secret" \
  -e S3_BUCKET_NAME="medical-ai-copilot-phi-prod" \
  cms-ingestor:latest