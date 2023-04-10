curl -L https://fly.io/install.sh | sh
flyctl auth login

fly launch
fly deploy
flyctl logs
fly deploy
fly secrets list
fly secrets --help
fly secrets set ALLOWED_HOSTS="mydjavuelist.fly.dev"
fly secrets list

fly ssh console -a mydjavuelist
# cd app
# python manage.py createsuperuser

fly ssh console --pty -C 'python /app/manage.py createsuperuser'