#!/bin/bash
echo "BUILD START"
which python3.11 > /dev/null 2>&1 && PYTHON="python3.11" || PYTHON="python3"
echo "Using Python: $($PYTHON --version)"

$PYTHON -m pip install -r requirements.txt

if [ -n "$DATABASE_URL" ] || [ -n "$POSTGRES_URL" ]; then
    echo "Applying database migrations..."
    $PYTHON manage.py migrate --noinput
fi

$PYTHON manage.py collectstatic --noinput --clear
echo "BUILD END"
