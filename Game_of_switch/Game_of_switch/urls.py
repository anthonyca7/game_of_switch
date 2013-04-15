from django.conf.urls import patterns, include, url
from Game import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Game_of_switch.views.home', name='home'),
    # url(r'^Game_of_switch/', include('Game_of_switch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('Game.urls')),
    url(r'^register', 'Game.views.register'),
    url(r'^login', 'Game.views.login'),
    url(r'^board/', views.board, name='board'),
)
