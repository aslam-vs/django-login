from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.views.home', name='home'),

    url(r'^signup$', 'apps.views.signup', name='signup'),
    # url(r'^django_login/', include('django_login.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),

    url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page': '/dashboard/'},name='logout'),
    # url(r'^subscriber/logout/$','django.contrib.auth.views.logout',{'next_page': '/index/login/'},name='sub_logout'),
     
)
