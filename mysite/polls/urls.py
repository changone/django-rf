# encoding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


def main():
    pass


if __name__ == '__main__':
    main()