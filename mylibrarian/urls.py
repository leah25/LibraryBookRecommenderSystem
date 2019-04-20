from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
        url(r'^login/$', auth_views.login, name='login'),
        url(r'^logout/$', auth_views.logout, name='logout'),
        url(r'^admin/', admin.site.urls),
        url(r'^', include('librarian.urls', namespace='librarian')),
        url(r'^', include('cart.urls', namespace='cart')),
        url('accounts/', include('django.contrib.auth.urls')),
]



def get_absolute_url(self):
    return reverse('librarian:book_detail',
                   args=[self.id, self.slug])

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)
