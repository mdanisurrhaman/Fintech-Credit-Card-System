#!/bin/bash
set -e

echo "🚀 Deployment started ..."

# Go to project root (safe)
cd /home/anish/Fintech-Credit-Card-System

# Pull latest code
echo "📥 Pulling latest code..."
git pull origin main
echo "✅ Code updated."

# Activate virtual environment
echo "🐍 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Django operations
echo "🗄️ Running migrations..."
python manage.py migrate

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Restart gunicorn safely
echo "🔁 Restarting Gunicorn..."
sudo systemctl restart fintech.gunicorn

# Deactivate env
deactivate

echo "✅ Deployment finished successfully!"

# #!/bin/bash
# set -e

# echo "Deployment started ..."

# # Pull the latest version of the app
# echo "Copying New changes...."
# git pull origin master
# echo "New changes copied to server !"

# # Activate Virtual Env
# #Syntax:- source virtual_env_name/bin/activate
# source mb/bin/activate
# echo "Virtual env 'mb' Activated !"

# echo "Clearing Cache..."
# python manage.py clean_pyc
# python manage.py clear_cache

# echo "Installing Dependencies..."
# pip install -r requirements.txt --no-input

# echo "Serving Static Files..."
# python manage.py collectstatic --noinput

# echo "Running Database migration..."
# python manage.py makemigrations
# python manage.py migrate

# # Deactivate Virtual Env
# deactivate
# echo "Virtual env 'mb' Deactivated !"

# echo "Reloading App..."
# #kill -HUP `ps -C gunicorn fch -o pid | head -n 1`
# ps aux |grep gunicorn |grep inner_project_folder_name | awk '{ print $2 }' |xargs kill -HUP

# echo "Deployment Finished !"