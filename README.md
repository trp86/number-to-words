# Number to Words Converter

A web application that converts numbers to words in multiple languages. The application consists of a Flask backend API and a static HTML/CSS/JS frontend.

## Project Structure

- `app.py`: Flask backend API
- `index.html`: Frontend HTML/CSS/JS
- `requirements.txt`: Python dependencies
- `netlify.toml`: Configuration for Netlify deployment
- `render.yaml`: Configuration for Render deployment
- `frontend/`: Directory for frontend deployment
- `backend/`: Directory for backend deployment
- `setup_deployment.sh`: Script to organize files for deployment

## Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open http://localhost:5000 in your browser

## Deployment

### Preparing for Deployment

Run the setup script to organize files for deployment:

```bash
./setup_deployment.sh
```

This script will:
1. Create `frontend/` and `backend/` directories
2. Copy the necessary files to each directory
3. Set up the project structure for deployment

### Frontend Deployment to Netlify

1. Create a new site on Netlify
2. Connect your GitHub repository
3. Configure the build settings:
   - Build command: (leave empty)
   - Publish directory: `frontend`
4. Deploy the site
5. After deployment, update the redirect in `frontend/netlify.toml` to point to your backend URL

### Backend Deployment to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the service:
   - Name: number-to-words-api
   - Environment: Python
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy the service
5. After deployment, copy the service URL and update the redirect in `frontend/netlify.toml`

## CORS Configuration

The backend is already configured to allow CORS requests from any origin. If you need to restrict this, update the CORS configuration in `app.py`.