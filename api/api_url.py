from django.urls import include, path

urlpatterns = [
    path("auth/", include("api.user.urls")),
    path("openai-content/", include("api.openai_content.urls")),
]
