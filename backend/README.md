# Number to Words Converter Backend

This directory contains the backend code for the Number to Words Converter application.

## Deployment to Render

This backend is configured to be deployed to Render. The `render.yaml` file contains the necessary configuration for deployment.

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the service:
   - Name: number-to-words-api
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy the service

## After Deployment

After deploying the backend, copy the service URL and update the redirect in `frontend/netlify.toml` to point to your backend URL.