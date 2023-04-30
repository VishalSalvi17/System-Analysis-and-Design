from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from website.views import(
	Locations,
	Hotels,
	Room_Status,
	ContactUs
)

from accounts.views import(
	Users,
	Make_Payment
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',Locations.as_view()),
    path('contact/',ContactUs.as_view()),
    path('destination/',Hotels.as_view()),
    path('about/',Room_Status.as_view()),
    path('payment/',Make_Payment.as_view()),
    path('register/',Users.as_view()),
    path('',include('website.urls')), 
    path('accounts/',include('accounts.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 