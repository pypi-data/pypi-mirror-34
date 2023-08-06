from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import json
from builtins import *
from django.core.urlresolvers import reverse
from agon_ratings.models import Rating
from cartoview.app_manager.models import App, AppInstance
from django import template
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from django.utils.html import mark_safe
from future import standard_library
from django.conf import settings
from geonode.documents.models import Document
from geonode.groups.models import Group, GroupProfile
from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.people.models import Profile
from guardian.shortcuts import get_objects_for_user

standard_library.install_aliases()
register = template.Library()


@register.filter()
def dump_json(obj):
    # if obj is None:
    #     return "null"
    return mark_safe(json.dumps(obj))


@register.assignment_tag
def num_ratings(obj):
    ct = ContentType.objects.get_for_model(obj)
    return len(Rating.objects.filter(object_id=obj.pk, content_type=ct))


@register.simple_tag
def layers_counts():
    return Layer.objects.count()


@register.simple_tag
def maps_counts():
    return Map.objects.count()


@register.simple_tag
def apps_counts():
    return AppInstance.objects.count()


@register.simple_tag
def users_counts():
    return Profile.objects.exclude(username="AnonymousUser").count()


@register.simple_tag
def groups_counts():
    return Group.objects.exclude(name="anonymous").count()


@register.simple_tag
def apps_url(url_name, *args, **kwargs):
    url = None
    try:
        url = reverse(url_name, args=args, kwargs=kwargs)
    except:
        pass
    return json.dumps(url)


@register.assignment_tag(takes_context=True)
def facets(context):
    request = context['request']
    title_filter = request.GET.get('title__icontains', '')

    facet_type = context['facet_type'] if 'facet_type' in context else 'all'

    if not settings.SKIP_PERMS_FILTER:
        authorized = get_objects_for_user(
            request.user, 'base.view_resourcebase').values('id')

    if facet_type == 'documents':

        documents = Document.objects.filter(title__icontains=title_filter)

        if settings.RESOURCE_PUBLISHING:
            documents = documents.filter(is_published=True)

        if not settings.SKIP_PERMS_FILTER:
            documents = documents.filter(id__in=authorized)

        counts = documents.values('doc_type').annotate(count=Count('doc_type'))
        facets = dict([(count['doc_type'], count['count'])
                       for count in counts])

        return facets

    elif facet_type == 'appinstances':
        appinstances = AppInstance.objects.filter(
            title__icontains=title_filter)
        if settings.RESOURCE_PUBLISHING:
            appinstances = appinstances.filter(is_published=True)

        if not settings.SKIP_PERMS_FILTER:
            appinstances = appinstances.filter(id__in=authorized)

        counts = appinstances.values('app__title').annotate(
            count=Count('app__name'))
        facets = dict([(count['app__title'], count['count'])
                       for count in counts])
        return facets

    else:

        layers = Layer.objects.filter(title__icontains=title_filter)

        if settings.RESOURCE_PUBLISHING:
            layers = layers.filter(is_published=True)

        if not settings.SKIP_PERMS_FILTER:
            layers = layers.filter(id__in=authorized)

        counts = layers.values('storeType').annotate(count=Count('storeType'))
        count_dict = dict([(count['storeType'], count['count'])
                           for count in counts])

        facets = {
            'raster': count_dict.get('coverageStore', 0),
            'vector': count_dict.get('dataStore', 0),
            'remote': count_dict.get('remoteStore', 0),
        }

        # Break early if only_layers is set.
        if facet_type == 'layers':
            return facets

        maps = Map.objects.filter(title__icontains=title_filter)
        documents = Document.objects.filter(title__icontains=title_filter)

        if not settings.SKIP_PERMS_FILTER:
            maps = maps.filter(id__in=authorized)
            documents = documents.filter(id__in=authorized)

        facets['map'] = maps.count()
        facets['document'] = documents.count()
        if facet_type == 'home':
            facets['user'] = get_user_model().objects.exclude(
                username='AnonymousUser').count()
            facets['app'] = App.objects.count()
            facets['group'] = GroupProfile.objects.exclude(
                access="private").count()

            facets['layer'] = facets['raster'] + \
                facets['vector'] + facets['remote']

    return facets


@register.filter(name='jsonify')
def jsonify(values):
    """Json Object"""
    return mark_safe(json.dumps(values))


@register.filter(name='objects_count')
def objects_count(instances, user):
    permitted = [instance for instance in instances if user.has_perm(
        'view_resourcebase', instance.get_self_resource())]
    return len(permitted)


@register.simple_tag(name='cartoview_reverse')
def reverse_url(url_name, *args, **kwargs):
    url = None
    try:
        url = reverse(url_name, args=args, kwargs=kwargs)
    except:
        pass
    return json.dumps(url)
