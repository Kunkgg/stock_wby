from celery import Celery
import os

# windows平台需要设置
if os.name == 'nt':
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

celery_app = Celery()
celery_app.config_from_object('src.celery_config.celeryConfig')
