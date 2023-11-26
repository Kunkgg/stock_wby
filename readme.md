```
python -m pytest -s --log-cli-level=INFO .\tests\test_store.py 
```

```
celery -A src.celery_start.celery_app beat --loglevel=INFO 
celery -A src.celery_start.celery_app worker --loglevel=INFO --concurrency=4 -P threads
celery -A src.celery_start.celery_app worker --loglevel=INFO
celery -A src.celery_start.celery_app flower
```