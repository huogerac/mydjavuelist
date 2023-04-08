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
