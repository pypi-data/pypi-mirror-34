# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import ast
import os

from kombu import Exchange, Queue

from .settings import *

# SECRET_KEY = '************************'
SITEURL = "http://localhost/"
# TIME_ZONE = 'Europe/Paris'
ASYNC_SIGNALS = ast.literal_eval(os.environ.get('ASYNC_SIGNALS', 'False'))
RABBITMQ_SIGNALS_BROKER_URL = 'amqp://localhost:5672'
REDIS_SIGNALS_BROKER_URL = 'redis://localhost:6379/0'
LOCAL_SIGNALS_BROKER_URL = 'memory://'

if ASYNC_SIGNALS:
    _BROKER_URL = os.environ.get('BROKER_URL', RABBITMQ_SIGNALS_BROKER_URL)
    # _BROKER_URL =  = os.environ.get('BROKER_URL', REDIS_SIGNALS_BROKER_URL)

    CELERY_RESULT_BACKEND = _BROKER_URL
else:
    _BROKER_URL = LOCAL_SIGNALS_BROKER_URL

BROKER_URL = _BROKER_URL

CELERY_RESULT_PERSISTENT = False

# Allow to recover from any unknown crash.
CELERY_ACKS_LATE = True

# Set this to False in order to run async
CELERY_TASK_ALWAYS_EAGER = False if ASYNC_SIGNALS else True
CELERY_TASK_IGNORE_RESULT = False

# I use these to debug kombu crashes; we get a more informative message.
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_CREATE_MISSING_QUEUES = True
CELERY_TASK_RESULT_EXPIRES = 43200

# Sometimes, Ask asks us to enable this to debug issues.
# BTW, it will save some CPU cycles.
CELERY_DISABLE_RATE_LIMITS = False
CELERY_SEND_TASK_EVENTS = True
CELERY_WORKER_DISABLE_RATE_LIMITS = False
CELERY_WORKER_SEND_TASK_EVENTS = True
GEONODE_EXCHANGE = Exchange("default", type="direct", durable=True)
GEOSERVER_EXCHANGE = Exchange("geonode", type="topic", durable=False)
CELERY_TASK_QUEUES = (
    Queue('default', GEONODE_EXCHANGE, routing_key='default'),
    Queue('geonode', GEONODE_EXCHANGE, routing_key='geonode'),
    Queue('update', GEONODE_EXCHANGE, routing_key='update'),
    Queue('cleanup', GEONODE_EXCHANGE, routing_key='cleanup'),
    Queue('email', GEONODE_EXCHANGE, routing_key='email'),
)

CELERY_TASK_QUEUES += (
    Queue("broadcast", GEOSERVER_EXCHANGE, routing_key="#"),
    Queue("email.events", GEOSERVER_EXCHANGE, routing_key="email"),
    Queue("all.geoserver", GEOSERVER_EXCHANGE, routing_key="geoserver.#"),
    Queue(
        "geoserver.catalog",
        GEOSERVER_EXCHANGE,
        routing_key="geoserver.catalog"),
    Queue(
        "geoserver.data", GEOSERVER_EXCHANGE, routing_key="geoserver.catalog"),
    Queue(
        "geoserver.events",
        GEOSERVER_EXCHANGE,
        routing_key="geonode.geoserver"),
    Queue(
        "notifications.events",
        GEOSERVER_EXCHANGE,
        routing_key="notifications"),
    Queue(
        "geonode.layer.viewer",
        GEOSERVER_EXCHANGE,
        routing_key="geonode.viewer"),
)

# Allow our remote workers to get tasks faster if they have a
# slow internet connection (yes Gurney, I'm thinking of you).
CELERY_MESSAGE_COMPRESSION = 'gzip'

# The default beiing 5000, we need more than this.
CELERY_MAX_CACHED_RESULTS = 32768

# NOTE: I don't know if this is compatible with upstart.
CELERYD_POOL_RESTARTS = True

CELERY_TRACK_STARTED = True
CELERY_SEND_TASK_SENT_EVENT = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'cartoview',
        'USER': 'hishamkaram',
        'PASSWORD': 'clogic',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    # vector datastore for uploads
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'ENGINE': '', # Empty ENGINE name disables
        'NAME': 'cartoview_datastore',
        'USER': 'hishamkaram',
        'PASSWORD': 'clogic',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
LAYER_PREVIEW_LIBRARY = "geoext"

GEOFENCE_SECURITY_ENABLED = False if TEST and not INTEGRATION else True

DEFAULT_WORKSPACE = os.getenv('DEFAULT_WORKSPACE', 'geonode')
CASCADE_WORKSPACE = os.getenv('CASCADE_WORKSPACE', 'geonode')

GEOSERVER_LOCATION = os.getenv('GEOSERVER_LOCATION',
                               'http://localhost:8080/geoserver/')

GEOSERVER_PUBLIC_LOCATION = os.getenv('GEOSERVER_PUBLIC_LOCATION',
                                      '{}geoserver/'.format(SITEURL))

OGC_SERVER_DEFAULT_USER = os.getenv('GEOSERVER_ADMIN_USER', 'admin')

OGC_SERVER_DEFAULT_PASSWORD = os.getenv('GEOSERVER_ADMIN_PASSWORD',
                                        'geoserver')
OGC_SERVER = {
    'default': {
        'BACKEND':
        'geonode.geoserver',
        'LOCATION':
        GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT':
        'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT':
        'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION':
        GEOSERVER_PUBLIC_LOCATION,
        'USER':
        OGC_SERVER_DEFAULT_USER,
        'PASSWORD':
        OGC_SERVER_DEFAULT_PASSWORD,
        'MAPFISH_PRINT_ENABLED':
        True,
        'PRINT_NG_ENABLED':
        True,
        'GEONODE_SECURITY_ENABLED':
        True,
        'GEOFENCE_SECURITY_ENABLED':
        GEOFENCE_SECURITY_ENABLED,
        'GEOGIG_ENABLED':
        False,
        'WMST_ENABLED':
        False,
        'BACKEND_WRITE_ENABLED':
        True,
        'WPS_ENABLED':
        False,
        'LOG_FILE':
        '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(
            os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE':
        os.getenv('DEFAULT_BACKEND_DATASTORE', 'datastore'),
        'PG_GEOGIG':
        False,
        'TIMEOUT':
        10  # number of seconds to allow for HTTP requests
    }
}
CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        # 'USER': 'admin',
        # 'PASSWORD': 'admin',

        # 'ALTERNATES_ONLY': True,
    }
}
# pycsw settings
PYCSW = {
    # pycsw configuration
    'CONFIGURATION': {
        # uncomment / adjust to override server config system defaults
        # 'server': {
        #    'maxrecords': '10',
        #    'pretty_print': 'true',
        #    'federatedcatalogues': 'http://catalog.data.gov/csw'
        # },
        'metadata:main': {
            'identification_title': 'GeoNode Catalogue',
            'identification_abstract': 'GeoNode is an open source platform' \
            ' that facilitates the creation, sharing, and collaborative use' \
            ' of geospatial data',
            'identification_keywords': 'sdi, catalogue, discovery, metadata,' \
            ' GeoNode',
            'identification_keywords_type': 'theme',
            'identification_fees': 'None',
            'identification_accessconstraints': 'None',
            'provider_name': 'Organization Name',
            'provider_url': SITEURL,
            'contact_name': 'Lastname, Firstname',
            'contact_position': 'Position Title',
            'contact_address': 'Mailing Address',
            'contact_city': 'City',
            'contact_stateorprovince': 'Administrative Area',
            'contact_postalcode': 'Zip or Postal Code',
            'contact_country': 'Country',
            'contact_phone': '+xx-xxx-xxx-xxxx',
            'contact_fax': '+xx-xxx-xxx-xxxx',
            'contact_email': 'Email Address',
            'contact_url': 'Contact URL',
            'contact_hours': 'Hours of Service',
            'contact_instructions': 'During hours of service. Off on ' \
            'weekends.',
            'contact_role': 'pointOfContact',
        },
        'metadata:inspire': {
            'enabled': 'true',
            'languages_supported': 'eng,gre',
            'default_language': 'eng',
            'date': 'YYYY-MM-DD',
            'gemet_keywords': 'Utility and governmental services',
            'conformity_service': 'notEvaluated',
            'contact_name': 'Organization Name',
            'contact_email': 'Email Address',
            'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD',
        }
    }
}

# GeoNode javascript client configuration

# default map projection
# Note: If set to EPSG:4326, then only EPSG:4326 basemaps will work.
DEFAULT_MAP_CRS = "EPSG:900913"

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (0, 0)
DEFAULT_MAP_ZOOM = 0
ALT_OSM_BASEMAPS = os.environ.get('ALT_OSM_BASEMAPS', True)
CARTODB_BASEMAPS = os.environ.get('CARTODB_BASEMAPS', True)
STAMEN_BASEMAPS = os.environ.get('STAMEN_BASEMAPS', True)
THUNDERFOREST_BASEMAPS = os.environ.get('THUNDERFOREST_BASEMAPS', True)
MAPBOX_ACCESS_TOKEN = os.environ.get(
    'MAPBOX_ACCESS_TOKEN',
    '<MAPBOX_ACCESS_TOKEN>'
)
BING_API_KEY = os.environ.get('BING_API_KEY', '<BING_API_KEY>')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '<GOOGLE_API_KEY>')
CELERYD_HIJACK_ROOT_LOGGER = True
CELERYD_CONCURENCY = 1
CELERY_ALWAYS_EAGER = True
CELERYD_LOG_FILE = None
CELERY_REDIRECT_STDOUTS = True
CELERYD_LOG_LEVEL = 1
SKIP_PERMS_FILTER = False
HAYSTACK_FACET_COUNTS = True
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE':
        'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
        'URL':
        'http://127.0.0.1:9200/',
        'INDEX_NAME':
        'haystack',
    },
    #    'db': {
    #        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    #        'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    #        }
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format':
            '%(levelname)s %(asctime)s %(module)s %(process)d '
            '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
        },
        "geonode": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "gsconfig.catalog": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "owslib": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "pycsw": {
            "handlers": ["console"],
            "level": "ERROR",
        },
    },
}

# Additional settings
CORS_ORIGIN_ALLOW_ALL = True

GEOIP_PATH = "/usr/local/share/GeoIP"

MONITORING_ENABLED = False
# add following lines to your local settings to enable monitoring
if MONITORING_ENABLED:
    MIDDLEWARE_CLASSES += (
        'geonode.contrib.monitoring.middleware.MonitoringMiddleware', )
    MONITORING_CONFIG = None
    MONITORING_SERVICE_NAME = 'local-geonode'

# Define email service on GeoNode
EMAIL_ENABLE = True

if EMAIL_ENABLE:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'Example.com <no-reply@localhost>'

# Advanced Security Workflow Settings
CLIENT_RESULTS_LIMIT = 20
API_LIMIT_PER_PAGE = 1000
FREETEXT_KEYWORDS_READONLY = False
RESOURCE_PUBLISHING = False
ADMIN_MODERATE_UPLOADS = False
GROUP_PRIVATE_RESOURCES = False
GROUP_MANDATORY_RESOURCES = False
MODIFY_TOPICCATEGORY = True
USER_MESSAGES_ALLOW_MULTIPLE_RECIPIENTS = True
DISPLAY_WMS_LINKS = True

# uncomment the following to enable osgeo_importer
# INSTALLED_APPS += ('osgeo_importer', )

# # osgeo_importer settings
# OSGEO_DATASTORE = 'datastore'
# OSGEO_IMPORTER_GEONODE_ENABLED = True
# OSGEO_IMPORTER_VALID_EXTENSIONS = [
#     'shp', 'shx', 'prj', 'dbf', 'kml', 'geojson', 'json', 'tif', 'tiff',
#     'gpkg', 'csv', 'zip', 'xml', 'sld'
# ]
# IMPORT_HANDLERS = [
#     # If GeoServer handlers are enabled, you must have an instance of geoserver running.
#     # Warning: the order of the handlers here matters.
#     'osgeo_importer.handlers.FieldConverterHandler',
#     'osgeo_importer.handlers.geoserver.GeoserverPublishHandler',
#     'osgeo_importer.handlers.geoserver.GeoserverPublishCoverageHandler',
#     'osgeo_importer.handlers.geoserver.GeoServerTimeHandler',
#     'osgeo_importer.handlers.geoserver.GeoWebCacheHandler',
#     'osgeo_importer.handlers.geoserver.GeoServerBoundsHandler',
#     'osgeo_importer.handlers.geoserver.GenericSLDHandler',
#     'osgeo_importer.handlers.geonode.GeoNodePublishHandler',
#     #    'osgeo_importer.handlers.mapproxy.publish_handler.MapProxyGPKGTilePublishHandler',
#     'osgeo_importer.handlers.geoserver.GeoServerStyleHandler',
#     'osgeo_importer.handlers.geonode.GeoNodeMetadataHandler'
# ]

# PROJECTION_DIRECTORY = os.path.join(PROJECT_ROOT, "data")

# uncomment the following to enable geonode client
#INSTALLED_APPS += ('geonode-client',)
# LAYER_PREVIEW_LIBRARY="react"
ROOT_URLCONF = "cartoview.urls"
