from app.settings.base import USE_TZ, TIME_ZONE, REDIS_URL


CELERY_BROKER_URL = f"{REDIS_URL}/1"
CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = True
# CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
