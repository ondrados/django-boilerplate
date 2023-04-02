from app import celery_app


@celery_app.task()
def test_task():
    pass