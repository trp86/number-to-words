#!/bin/bash

# Create backend directory
mkdir -p backend

# Move backend files to backend directory
cp app.py backend/
cp requirements.txt backend/
cp render.yaml backend/
cp get_all_languages.py backend/
cp test_num2words.py backend/

# Copy index.html to frontend directory
cp index.html frontend/

echo "Project structure reorganized for deployment."
echo "Frontend files are in the 'frontend' directory."
echo "Backend files are in the 'backend' directory."
echo ""
echo "Next steps:"
echo "1. Deploy the backend to Render"
echo "2. Update the redirect URL in frontend/netlify.toml with your backend URL"
echo "3. Deploy the frontend to Netlify"