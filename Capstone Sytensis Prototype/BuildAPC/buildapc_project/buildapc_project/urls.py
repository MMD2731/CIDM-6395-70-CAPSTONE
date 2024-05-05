from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URLs from the buildapc_app application
    path('buildapc/', include('buildapc_app.urls')),
    # You can add more applications' URLs here as your project grows
]
