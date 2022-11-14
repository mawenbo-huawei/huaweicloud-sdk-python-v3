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
VERSION = "3.1.10"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.10',
    'huaweicloudsdkantiddos==3.1.10',
    'huaweicloudsdkaom==3.1.10',
    'huaweicloudsdkapig==3.1.10',
    'huaweicloudsdkapm==3.1.10',
    'huaweicloudsdkas==3.1.10',
    'huaweicloudsdkbcs==3.1.10',
    'huaweicloudsdkbms==3.1.10',
    'huaweicloudsdkbss==3.1.10',
    'huaweicloudsdkbssintl==3.1.10',
    'huaweicloudsdkcae==3.1.10',
    'huaweicloudsdkcampusgo==3.1.10',
    'huaweicloudsdkcbh==3.1.10',
    'huaweicloudsdkcbr==3.1.10',
    'huaweicloudsdkcbs==3.1.10',
    'huaweicloudsdkcc==3.1.10',
    'huaweicloudsdkcce==3.1.10',
    'huaweicloudsdkccm==3.1.10',
    'huaweicloudsdkcdm==3.1.10',
    'huaweicloudsdkcdn==3.1.10',
    'huaweicloudsdkces==3.1.10',
    'huaweicloudsdkcgs==3.1.10',
    'huaweicloudsdkclassroom==3.1.10',
    'huaweicloudsdkcloudartifact==3.1.10',
    'huaweicloudsdkcloudbuild==3.1.10',
    'huaweicloudsdkclouddeploy==3.1.10',
    'huaweicloudsdkcloudide==3.1.10',
    'huaweicloudsdkcloudpipeline==3.1.10',
    'huaweicloudsdkcloudrtc==3.1.10',
    'huaweicloudsdkcloudtable==3.1.10',
    'huaweicloudsdkcloudtest==3.1.10',
    'huaweicloudsdkcodecheck==3.1.10',
    'huaweicloudsdkcodecraft==3.1.10',
    'huaweicloudsdkcodehub==3.1.10',
    'huaweicloudsdkcph==3.1.10',
    'huaweicloudsdkcpts==3.1.10',
    'huaweicloudsdkcse==3.1.10',
    'huaweicloudsdkcsms==3.1.10',
    'huaweicloudsdkcss==3.1.10',
    'huaweicloudsdkcts==3.1.10',
    'huaweicloudsdkdas==3.1.10',
    'huaweicloudsdkdbss==3.1.10',
    'huaweicloudsdkdcs==3.1.10',
    'huaweicloudsdkddm==3.1.10',
    'huaweicloudsdkdds==3.1.10',
    'huaweicloudsdkdeh==3.1.10',
    'huaweicloudsdkdevsecurity==3.1.10',
    'huaweicloudsdkdevstar==3.1.10',
    'huaweicloudsdkdgc==3.1.10',
    'huaweicloudsdkdli==3.1.10',
    'huaweicloudsdkdms==3.1.10',
    'huaweicloudsdkdns==3.1.10',
    'huaweicloudsdkdrs==3.1.10',
    'huaweicloudsdkdsc==3.1.10',
    'huaweicloudsdkdws==3.1.10',
    'huaweicloudsdkecs==3.1.10',
    'huaweicloudsdkeg==3.1.10',
    'huaweicloudsdkeihealth==3.1.10',
    'huaweicloudsdkeip==3.1.10',
    'huaweicloudsdkelb==3.1.10',
    'huaweicloudsdkeps==3.1.10',
    'huaweicloudsdker==3.1.10',
    'huaweicloudsdkevs==3.1.10',
    'huaweicloudsdkfrs==3.1.10',
    'huaweicloudsdkfunctiongraph==3.1.10',
    'huaweicloudsdkga==3.1.10',
    'huaweicloudsdkgaussdb==3.1.10',
    'huaweicloudsdkgaussdbfornosql==3.1.10',
    'huaweicloudsdkgaussdbforopengauss==3.1.10',
    'huaweicloudsdkges==3.1.10',
    'huaweicloudsdkgsl==3.1.10',
    'huaweicloudsdkhilens==3.1.10',
    'huaweicloudsdkhss==3.1.10',
    'huaweicloudsdkiam==3.1.10',
    'huaweicloudsdkiec==3.1.10',
    'huaweicloudsdkief==3.1.10',
    'huaweicloudsdkies==3.1.10',
    'huaweicloudsdkimage==3.1.10',
    'huaweicloudsdkimagesearch==3.1.10',
    'huaweicloudsdkims==3.1.10',
    'huaweicloudsdkiotanalytics==3.1.10',
    'huaweicloudsdkiotda==3.1.10',
    'huaweicloudsdkiotedge==3.1.10',
    'huaweicloudsdkivs==3.1.10',
    'huaweicloudsdkkafka==3.1.10',
    'huaweicloudsdkkms==3.1.10',
    'huaweicloudsdkkps==3.1.10',
    'huaweicloudsdklive==3.1.10',
    'huaweicloudsdklts==3.1.10',
    'huaweicloudsdkmeeting==3.1.10',
    'huaweicloudsdkmoderation==3.1.10',
    'huaweicloudsdkmpc==3.1.10',
    'huaweicloudsdkmrs==3.1.10',
    'huaweicloudsdknat==3.1.10',
    'huaweicloudsdknlp==3.1.10',
    'huaweicloudsdkocr==3.1.10',
    'huaweicloudsdkoms==3.1.10',
    'huaweicloudsdkosm==3.1.10',
    'huaweicloudsdkprojectman==3.1.10',
    'huaweicloudsdkrabbitmq==3.1.10',
    'huaweicloudsdkrds==3.1.10',
    'huaweicloudsdkres==3.1.10',
    'huaweicloudsdkrms==3.1.10',
    'huaweicloudsdkrocketmq==3.1.10',
    'huaweicloudsdkroma==3.1.10',
    'huaweicloudsdksa==3.1.10',
    'huaweicloudsdkscm==3.1.10',
    'huaweicloudsdksdrs==3.1.10',
    'huaweicloudsdkservicestage==3.1.10',
    'huaweicloudsdksfsturbo==3.1.10',
    'huaweicloudsdksis==3.1.10',
    'huaweicloudsdksmn==3.1.10',
    'huaweicloudsdksms==3.1.10',
    'huaweicloudsdkswr==3.1.10',
    'huaweicloudsdktms==3.1.10',
    'huaweicloudsdkugo==3.1.10',
    'huaweicloudsdkvas==3.1.10',
    'huaweicloudsdkvcm==3.1.10',
    'huaweicloudsdkvod==3.1.10',
    'huaweicloudsdkvpc==3.1.10',
    'huaweicloudsdkvpcep==3.1.10',
    'huaweicloudsdkvss==3.1.10',
    'huaweicloudsdkwaf==3.1.10',
    'huaweicloudsdkworkspace==3.1.10',
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
