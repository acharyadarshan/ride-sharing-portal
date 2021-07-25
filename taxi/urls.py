
from django.conf import settings # new
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path,re_path
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import TokenRefreshView
# justcomments

from trips.views import SignUpView, LogInView


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/sign_up/', SignUpView.as_view(), name='sign_up'),
    path('api/log_in/', LogInView.as_view(), name='log_in'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/trip/', include('trips.urls', 'trip',)),
    re_path(r'^.*',TemplateView.as_view(template_name='index.html')),
]
