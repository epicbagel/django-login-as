from django.conf.urls import patterns, include, url

urlpatterns = patterns('login_as.views',
    url('^$', 'chooser', name='login-as-chooser'),
    url('^(.+?)/$', 'login', name='login-as-login'),
)