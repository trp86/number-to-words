# Deployment Guide for Number to Words Converter

This guide provides detailed instructions for deploying the Number to Words Converter application to Netlify (frontend) and Render (backend).

## Prerequisites

- GitHub account
- Netlify account
- Render account
- Git repository with your code

## Step 1: Prepare Your Repository

1. Make sure your code is in a Git repository
2. Run the setup script to organize files for deployment:
   ```bash
   ./setup_deployment.sh
   ```
3. Commit and push the changes to your repository

## Step 2: Deploy the Backend to Render

1. Log in to your Render account
2. Click on "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: `number-to-words-api` (or any name you prefer)
   - Environment: `Python`
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Select the appropriate plan (Free tier is sufficient for testing)
5. Click "Create Web Service"
6. Wait for the deployment to complete
7. Copy the service URL (e.g., `https://number-to-words-api.onrender.com`)

## Step 3: Update Frontend Configuration

1. Open `frontend/netlify.toml`
2. Update the redirect URL with your backend URL:
   ```toml
   [[redirects]]
     from = "/api/*"
     to = "https://your-backend-url.onrender.com/api/:splat"
     status = 200
     force = true
   ```
   Replace `https://your-backend-url.onrender.com` with your actual backend URL
3. Commit and push the changes to your repository

## Step 4: Deploy the Frontend to Netlify

1. Log in to your Netlify account
2. Click on "Add new site" and select "Import an existing project"
3. Connect your GitHub repository
4. Configure the build settings:
   - Base directory: (leave empty)
   - Build command: (leave empty)
   - Publish directory: `frontend`
5. Click "Deploy site"
6. Wait for the deployment to complete
7. Your site is now live at the Netlify URL (e.g., `https://your-site-name.netlify.app`)

## Step 5: Configure Custom Domain (Optional)

### For Netlify (Frontend):

1. Go to your site's dashboard on Netlify
2. Click on "Domain settings"
3. Click on "Add custom domain"
4. Follow the instructions to set up your custom domain

### For Render (Backend):

1. Go to your web service dashboard on Render
2. Click on "Settings"
3. Scroll down to "Custom Domains"
4. Click on "Add Custom Domain"
5. Follow the instructions to set up your custom domain

## Troubleshooting

### CORS Issues

If you encounter CORS issues, make sure:

1. The backend CORS configuration is correct in `app.py`
2. The redirect in `netlify.toml` is correctly configured
3. The backend URL in the redirect is correct and accessible

### Deployment Failures

1. Check the build logs for errors
2. Make sure all dependencies are correctly specified in `requirements.txt`
3. Verify that the start command is correct