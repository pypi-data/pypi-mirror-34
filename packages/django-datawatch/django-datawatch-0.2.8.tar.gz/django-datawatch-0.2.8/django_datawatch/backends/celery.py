# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django_datawatch.backends.base import BaseBackend
from django_datawatch.tasks import django_datawatch_enqueue, \
    django_datawatch_run, django_datawatch_refresh
from django_datawatch.defaults import defaults


class Backend(BaseBackend):
    """
    A wrapper backend to execute tasks asynchronously in celery
    """
    def enqueue(self, slug, async=True):
        kwargs = dict(kwargs=dict(slug=slug),
                      queue=getattr(settings,
                                    'DJANGO_DATAWATCH_CELERY_QUEUE_NAME',
                                    defaults['CELERY_QUEUE_NAME']))
        if async:
            django_datawatch_enqueue.apply_async(**kwargs)
        else:
            django_datawatch_enqueue.apply(**kwargs)

    def refresh(self, slug, async=True):
        kwargs = dict(kwargs=dict(slug=slug),
                      queue=getattr(settings,
                                    'DJANGO_DATAWATCH_CELERY_QUEUE_NAME',
                                    defaults['CELERY_QUEUE_NAME']))
        if async:
            django_datawatch_refresh.apply_async(**kwargs)
        else:
            django_datawatch_refresh.apply(**kwargs)

    def run(self, slug, identifier, async=True):
        kwargs = dict(kwargs=dict(slug=slug, identifier=identifier),
                      queue=getattr(settings,
                                    'DJANGO_DATAWATCH_CELERY_QUEUE_NAME',
                                    defaults['CELERY_QUEUE_NAME']))
        if async:
            django_datawatch_run.apply_async(**kwargs)
        else:
            django_datawatch_run.apply(**kwargs)
