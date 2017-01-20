# forge-tool-control-api
Forge Access Control

Linux dev environment setup

Install required packages.
```
sudo apt-get install vim git docker docker-compose

sudo pip install -U pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper
```

Create our virtual python environment.
```
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv access-control
mkdir dev
cd dev
git clone [git url here]
cd forge-tool-control-api
```

To bring up postgres and the webserver.

```
docker-compose up
```

Once it is up, you can go to http://localhost:8000 to bring up the root.

Run the following to apply migrations to your local database.

```
sudo docker-compose run web ./manage.py migrate
```

Running commands:

```
sudo docker-compose run web /bin/bash
```
