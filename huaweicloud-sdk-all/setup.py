# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

from os import path

from setuptools import setup, find_packages

NAME = "huaweicloudsdkall"
VERSION = "3.0.106"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.106',
    'huaweicloudsdkantiddos==3.0.106',
    'huaweicloudsdkaom==3.0.106',
    'huaweicloudsdkapig==3.0.106',
    'huaweicloudsdkapm==3.0.106',
    'huaweicloudsdkas==3.0.106',
    'huaweicloudsdkbcs==3.0.106',
    'huaweicloudsdkbms==3.0.106',
    'huaweicloudsdkbss==3.0.106',
    'huaweicloudsdkbssintl==3.0.106',
    'huaweicloudsdkcampusgo==3.0.106',
    'huaweicloudsdkcbh==3.0.106',
    'huaweicloudsdkcbr==3.0.106',
    'huaweicloudsdkcbs==3.0.106',
    'huaweicloudsdkcc==3.0.106',
    'huaweicloudsdkcce==3.0.106',
    'huaweicloudsdkccm==3.0.106',
    'huaweicloudsdkcdm==3.0.106',
    'huaweicloudsdkcdn==3.0.106',
    'huaweicloudsdkces==3.0.106',
    'huaweicloudsdkcgs==3.0.106',
    'huaweicloudsdkclassroom==3.0.106',
    'huaweicloudsdkcloudbuild==3.0.106',
    'huaweicloudsdkclouddeploy==3.0.106',
    'huaweicloudsdkcloudide==3.0.106',
    'huaweicloudsdkcloudpipeline==3.0.106',
    'huaweicloudsdkcloudrtc==3.0.106',
    'huaweicloudsdkcloudtable==3.0.106',
    'huaweicloudsdkcloudtest==3.0.106',
    'huaweicloudsdkcodecheck==3.0.106',
    'huaweicloudsdkcodecraft==3.0.106',
    'huaweicloudsdkcodehub==3.0.106',
    'huaweicloudsdkcph==3.0.106',
    'huaweicloudsdkcpts==3.0.106',
    'huaweicloudsdkcse==3.0.106',
    'huaweicloudsdkcsms==3.0.106',
    'huaweicloudsdkcss==3.0.106',
    'huaweicloudsdkcts==3.0.106',
    'huaweicloudsdkdas==3.0.106',
    'huaweicloudsdkdbss==3.0.106',
    'huaweicloudsdkdcs==3.0.106',
    'huaweicloudsdkddm==3.0.106',
    'huaweicloudsdkdds==3.0.106',
    'huaweicloudsdkdeh==3.0.106',
    'huaweicloudsdkdevstar==3.0.106',
    'huaweicloudsdkdgc==3.0.106',
    'huaweicloudsdkdli==3.0.106',
    'huaweicloudsdkdms==3.0.106',
    'huaweicloudsdkdns==3.0.106',
    'huaweicloudsdkdrs==3.0.106',
    'huaweicloudsdkdsc==3.0.106',
    'huaweicloudsdkdws==3.0.106',
    'huaweicloudsdkecs==3.0.106',
    'huaweicloudsdkeg==3.0.106',
    'huaweicloudsdkeip==3.0.106',
    'huaweicloudsdkelb==3.0.106',
    'huaweicloudsdkeps==3.0.106',
    'huaweicloudsdkevs==3.0.106',
    'huaweicloudsdkfrs==3.0.106',
    'huaweicloudsdkfunctiongraph==3.0.106',
    'huaweicloudsdkgaussdb==3.0.106',
    'huaweicloudsdkgaussdbfornosql==3.0.106',
    'huaweicloudsdkgaussdbforopengauss==3.0.106',
    'huaweicloudsdkges==3.0.106',
    'huaweicloudsdkgsl==3.0.106',
    'huaweicloudsdkhilens==3.0.106',
    'huaweicloudsdkhss==3.0.106',
    'huaweicloudsdkiam==3.0.106',
    'huaweicloudsdkiec==3.0.106',
    'huaweicloudsdkief==3.0.106',
    'huaweicloudsdkies==3.0.106',
    'huaweicloudsdkimage==3.0.106',
    'huaweicloudsdkimagesearch==3.0.106',
    'huaweicloudsdkims==3.0.106',
    'huaweicloudsdkiotanalytics==3.0.106',
    'huaweicloudsdkiotda==3.0.106',
    'huaweicloudsdkiotedge==3.0.106',
    'huaweicloudsdkivs==3.0.106',
    'huaweicloudsdkkafka==3.0.106',
    'huaweicloudsdkkms==3.0.106',
    'huaweicloudsdkkps==3.0.106',
    'huaweicloudsdklive==3.0.106',
    'huaweicloudsdklts==3.0.106',
    'huaweicloudsdkmeeting==3.0.106',
    'huaweicloudsdkmoderation==3.0.106',
    'huaweicloudsdkmpc==3.0.106',
    'huaweicloudsdkmrs==3.0.106',
    'huaweicloudsdknat==3.0.106',
    'huaweicloudsdknlp==3.0.106',
    'huaweicloudsdkocr==3.0.106',
    'huaweicloudsdkoms==3.0.106',
    'huaweicloudsdkosm==3.0.106',
    'huaweicloudsdkprojectman==3.0.106',
    'huaweicloudsdkrabbitmq==3.0.106',
    'huaweicloudsdkrds==3.0.106',
    'huaweicloudsdkres==3.0.106',
    'huaweicloudsdkrms==3.0.106',
    'huaweicloudsdkrocketmq==3.0.106',
    'huaweicloudsdkroma==3.0.106',
    'huaweicloudsdksa==3.0.106',
    'huaweicloudsdkscm==3.0.106',
    'huaweicloudsdksdrs==3.0.106',
    'huaweicloudsdkservicestage==3.0.106',
    'huaweicloudsdksfsturbo==3.0.106',
    'huaweicloudsdksis==3.0.106',
    'huaweicloudsdksmn==3.0.106',
    'huaweicloudsdksms==3.0.106',
    'huaweicloudsdkswr==3.0.106',
    'huaweicloudsdktms==3.0.106',
    'huaweicloudsdkugo==3.0.106',
    'huaweicloudsdkvas==3.0.106',
    'huaweicloudsdkvcm==3.0.106',
    'huaweicloudsdkvod==3.0.106',
    'huaweicloudsdkvpc==3.0.106',
    'huaweicloudsdkvpcep==3.0.106',
    'huaweicloudsdkvss==3.0.106',
    'huaweicloudsdkwaf==3.0.106',
]

OPTIONS = {
    'bdist_wheel': {
        'universal': True
    }
}

setup(
    name=NAME,
    version=VERSION,
    options=OPTIONS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["huaweicloud", "sdk", "all"],
    packages=find_packages(),
    platforms=['any'],
    install_requires=INSTALL_REQUIRES,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development'
    ]
)
