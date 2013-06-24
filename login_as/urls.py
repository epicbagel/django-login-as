from django.conf.urls import patterns, include, url

urlpatterns = patterns('login_as.views',
    url(r'^user/(?P<user_id>\d+)', 'login', {}, name = 'login-as-login'),
    url('^$', 'chooser', name='login-as-chooser'),
    #url('^(.+?)/$', 'login', name='login-as-login'),
)