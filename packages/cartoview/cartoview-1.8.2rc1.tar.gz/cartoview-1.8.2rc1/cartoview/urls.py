# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from geonode.urls import urlpatterns
from cartoview.cartoview_api.views import layer_config_json, update_extent
from cartoview_api.rest import (
    AllResourcesResource, AttributeResource, MapLayerResource)
from cartoview.app_manager.rest import (AppInstanceResource, AppResource,
                                        AppTypeResource,
                                        LayerFilterExtensionResource)
from cartoview.views import index as cartoview_index, check_version
from geonode.api.urls import api

api.register(AppInstanceResource())
api.register(AppResource())
api.register(AppTypeResource())
api.register(LayerFilterExtensionResource())
api.register(AllResourcesResource())
api.register(AttributeResource())
api.register(MapLayerResource())
urlpatterns = patterns(
    '',
    url(r'^/?$', cartoview_index, name='home'),
    url(r'^layer/(?P<layername>[^/]*)/json/?$',
        layer_config_json, name='layer_json'),
    url(r'^update/extent/(?P<typename>[^/]*)$', update_extent,
        name='cartoview.update_extent'),
    url(r'^check-version/$', check_version, name='check_version'),
    url(r'', include(api.urls)),
    (r'^apps/', include('cartoview.app_manager.urls')),) + urlpatterns
