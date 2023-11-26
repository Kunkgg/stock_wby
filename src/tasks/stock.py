from src.celery_start import celery_app
from src.store import save_stock_all_spot


@celery_app.task
def auto_save_stock_all_spot():
    save_stock_all_spot()
