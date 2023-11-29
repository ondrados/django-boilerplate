from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from users.urls import urlpatterns_auth
from users.urls import urlpatterns_users


def root(request):
    return JsonResponse({"hello": "world"})


urlpatterns_api = [
    path("auth/", include((urlpatterns_auth, "auth-api"), namespace="auth-api")),
    path("users/", include((urlpatterns_users, "users-api"), namespace="users-api")),
]

urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("api/", include(urlpatterns_api)),
    path("health/", include("health_check.urls")),
]

if settings.DEBUG:

    def trigger_error(request):
        return 1 / 0

    def trigger_test_task(request):
        from core.tasks import test_task
        test_task.delay()
        return JsonResponse({"status": "Ok"})


    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += (path("sentry-debug/", trigger_error),)
    urlpatterns += (path("test-task/", trigger_test_task),)
