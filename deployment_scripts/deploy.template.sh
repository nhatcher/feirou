#!/bin/bash
# makes sure the program ends if any of the comands produces an error
set -e

readonly REPOSITORY_URL="<github.url>"
readonly REPOSITORY_NAME="<github.name>"

# stop the service
systemctl stop gunicorn.service

# remove old directory if exists
rm -rf "/var/lib/django/${REPOSITORY_NAME}"

if [[ -n "$1" ]]; then
    GIT_BRANCH="$1"
else
    GIT_BRANCH="main"
fi


# as the django user:
# 1. clone the repository
# 2. save the commit id
# 3. activate the environment and install dependencies
# 4. migrate the database if needed
# 5. Collect static files
sudo -u django -s /bin/bash << EOF
set -e
cd /var/lib/django/
git clone "${REPOSITORY_URL}"
cd "${REPOSITORY_NAME}"
git checkout "${GIT_BRANCH}"
git log -n 1 --format="%H" > ../deployed_commit_id.txt
python -m venv venv
source venv/bin/activate
pip install -r production_requirements.txt
cd server
export DJANGO_SETTINGS_MODULE=settings.settings.production
python manage.py migrate
python manage.py collectstatic --settings=settings.settings.production --no-input
EOF

cp /var/lib/django/deployed_commit_id.txt /var/www/"${REPOSITORY_NAME}"/

# download the artifacts for the frontend
rm -rf /var/www/"${REPOSITORY_NAME}"/
mkdir /var/www/"${REPOSITORY_NAME}"/
python /var/lib/django/"${REPOSITORY_NAME}"/deployment_scripts/download_artifact.py
unzip /var/www/"${REPOSITORY_NAME}"/dist.zip -d /var/www/"${REPOSITORY_NAME}"/
rm /var/www/"${REPOSITORY_NAME}"/dist.zip


# copy files for the admin pannel
rm -rf /var/www/django_admin/
mkdir -p /var/www/django_admin/static/
cp -r /var/lib/django/static/* /var/www/django_admin/static/

# make sure all is own by caddy user
chown caddy:caddy /var/www/ -R

# start the service again
systemctl start gunicorn.service

echo -e "\n\n ✨✨Success!✨✨"
