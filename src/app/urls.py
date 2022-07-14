from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from users.urls import urlpatterns_auth, urlpatterns_user


def home(request):
    return JsonResponse({"hello": "world"})


def health_check(request):
    return JsonResponse({"status": "Ok"})


urlpatterns_api = [
    path("auth/", include((urlpatterns_auth, "auth-api"), namespace="auth-api")),
    path("user/", include((urlpatterns_user, "user-api"), namespace="user-api")),
]

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include(urlpatterns_api)),
    path("health/", health_check),
]

if settings.DEBUG:

    def trigger_error(request):
        1 / 0

    urlpatterns += (path("sentry-debug/", trigger_error),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
