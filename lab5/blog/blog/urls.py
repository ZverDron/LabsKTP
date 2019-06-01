from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from articles import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.archive, ),
    url(
    r'^article/(?P<article_id>\d+)$',
    views.get_article,
    name='get_article'
    ),
    url(r'^article/add', views.create_post, name='make_post' ),
    url(r'^admin/', include(admin.site.urls)),
)
