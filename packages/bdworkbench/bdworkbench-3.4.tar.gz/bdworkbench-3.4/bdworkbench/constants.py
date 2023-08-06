#!/usr/bin/env python
#
# Copyright (c) 2016 BlueData Software, Inc.
#

from version import __version__ as VERSION

AWB_VERSION = VERSION

DEFAULT_INT_NEGONE = -1

DEFAULT_STR_ONE = '1'
DEFAULT_STR_ALL = 'all'
DEFAULT_STR_EMPTY = "''"
DEFAULT_STR_VERSION = '1.0'
DEFAULT_STR_DEFAULT = 'default'

DEFAULT_CONFIG_API_VER = '8'
DEFAULT_CATALOG_API_VER = '4'

DEFAULT_BOOL_TRUE = True
DEFAULT_BOOL_FALSE = False

DEFAULT_CATEGORY_HADOOP = 'Hadoop'

SUPPORTED_DOCKER_VERSIONS = { # ActualVer : RecordedVer
                             '1.7': '1.7',
                             '1.12': '1.12',
                             '1.13': '1.12'}

DEFAULT_IMAGE_ROLES = 'all_roles'
OS_CLASS_DICT = {'centos6': ('centos', '6'),
                 'centos7': ('centos', '7'),
                 'rhel6'  : ('rhel',  '6'),
                 'rhel7'  : ('rhel',  '7'),
                 'ubuntu16' : ('ubuntu', '16')}

# Catalog API version when the specific feature was introduced.
IMAGE_REGISTRY_SUPPORT  = '3'
IMAGE_PER_ROLE_SUPPORT  = '4'

# BlueData internal Environment variables
AWB_DEBUG='AWB_DEBUG'
AWB_INTERNAL_ORGNAME='AWB_INTERNAL_ORGNAME'

# User facing environment variables.
RHEL_USERNAME='RHEL_USERNAME'
RHEL_PASSWORD='RHEL_PASSWORD'

AWB_SKIP_IMAGE_REBUILD='AWB_SKIP_IMAGE_REBUILD'

AWB_REGISTRY_USERNAME='AWB_REGISTRY_USERNAME'
AWB_REGISTRY_PASSWORD='AWB_REGISTRY_PASSWORD'
DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE='DOCKER_CONTENT_TRUST_ROOT_PASSPHRASE'
DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE='DOCKER_CONTENT_TRUST_REPOSITORY_PASSPHRASE'

VERSION_STR = 'version'
DISTROID_STR = 'distro_id'
ENTRY_STR = 'entry'
