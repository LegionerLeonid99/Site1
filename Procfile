web: sh -c 'FLASK_ENV=production gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --forwarded-allow-ips="*" --access-logfile - --error-logfile - --log-level debug wsgi:app'
