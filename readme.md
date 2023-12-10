```
python -m pytest -s --log-cli-level=INFO .\tests\test_store.py 
```

```
celery -A src.celery_start.celery_app beat --loglevel=INFO 
celery -A src.celery_start.celery_app worker --loglevel=INFO --concurrency=4 -P threads
celery -A src.celery_start.celery_app worker --loglevel=INFO
celery -A src.celery_start.celery_app flower
```

## TODO

- 添加收到触犯更新组合 record 的操作按钮
- 设置组合数据自动更新方式
- 设置 `买点`， `卖点` 计算方式
- 添加 Notes