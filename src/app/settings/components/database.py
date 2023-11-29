import dj_database_url

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# https://github.com/jazzband/dj-database-url

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
