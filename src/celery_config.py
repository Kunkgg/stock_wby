
class celeryConfig(object):
    timezone = 'Asia/Shanghai'
    broker_url = "redis://localhost:6379/1"
    backend = ""
    include = ['src.tasks.stock']
    beat_schedule = {
        'save-stock-all-spot-every-180s':
            {
                'task': 'src.tasks.stock.auto_save_stock_all_spot',
                'schedule': 180,
            },
    }
