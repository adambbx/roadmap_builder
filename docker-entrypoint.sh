#!/bin/bash

set -e

if [ -f ./entrypoint-pre.sh ]; then
  ./entrypoint-pre.sh
fi

case $1 in
  run)
    python manage.py migrate --noinput || {
      echo "Cannot migrate the master database"
      exit 1
    }
    python manage.py collectstatic --clear --noinput || {
      echo "Cannot collect statics"
      exit 1
    }
    exec python manage.py runserver 0.0.0.0:8000 --settings="${DJANGO_SETTINGS_MODULE}"
    ;;
  wsgi)
    python manage.py migrate --noinput || {
      echo "Cannot migrate the master database"
      exit 1
    }
    python manage.py collectstatic --clear --noinput || {
      echo "Cannot collect statics"
      exit 1
    }
    exec uwsgi \
      --wsgi-file roadmap_builder/wsgi.py \
      --chdir=/app \
      --buffer-size=4096 \
      --module=roadmap_builder.wsgi:application \
      --socket 0.0.0.0:3031 \
      --master \
      --env DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE}" \
      --pidfile=/app/roadmap-master.pid \
      --threads=2 \
      --processes=8 \
      --harakiri-verbose \
      --backtrace-depth=4 \
      --harakiri=1000 \
      --socket-timeout=1000 \
      --http-timeout=1000 \
      --enable-threads \
      --max-requests=5000 \
      --vacuum \
      --touch-reload=/app/roadmap_builder/wsgi.py \
      --stats /tmp/stats.socket
    ;;
esac
