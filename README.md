# EasyShop

This is a minimal Django project set up as a starting point for the EasyShop application.

## Setup (local)

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the homepage.

## Deployment notes

These instructions mirror the desired EC2 configuration (gunicorn + nginx):

1. **System packages**
   ```bash
   sudo apt update && sudo apt install python3-venv python3-dev nginx git
   ```

2. **Clone repo & virtualenv**
   ```bash
   git clone <your-repo-url> easyshop
   cd easyshop
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   ```

3. **Gunicorn systemd service** (/etc/systemd/system/gunicorn.service):
   ```ini
   [Unit]
   Description=gunicorn daemon for EasyShop
   After=network.target

   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/easyshop
   ExecStart=/home/ubuntu/easyshop/venv/bin/gunicorn --access-logfile - \
             --workers 3 --bind unix:/home/ubuntu/easyshop/easyshop.sock \
             easyshop.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

4. **Nginx configuration** (/etc/nginx/sites-available/easyshop):
   ```nginx
   server {
       listen 80;
       server_name your_domain_or_IP;

       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
           root /home/ubuntu/easyshop;
       }

       location / {
           include proxy_params;
           proxy_pass http://unix:/home/ubuntu/easyshop/easyshop.sock;
       }
   }
   ```
   Enable linking to `sites-enabled` and restart nginx.

5. **SSL**
   Use Certbot to obtain certificates and update nginx to listen on 443.

## Git

Initialize and push to your remote repository:

```bash
cd /workspace/EasyShop
git init
git add .
git commit -m "Initial EasyShop skeleton"
# add remote, then git push -u origin main
```
