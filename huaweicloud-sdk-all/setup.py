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
VERSION = "3.1.50"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.50',
    'huaweicloudsdkantiddos==3.1.50',
    'huaweicloudsdkaom==3.1.50',
    'huaweicloudsdkaos==3.1.50',
    'huaweicloudsdkapig==3.1.50',
    'huaweicloudsdkapm==3.1.50',
    'huaweicloudsdkas==3.1.50',
    'huaweicloudsdkbcs==3.1.50',
    'huaweicloudsdkbms==3.1.50',
    'huaweicloudsdkbss==3.1.50',
    'huaweicloudsdkbssintl==3.1.50',
    'huaweicloudsdkcae==3.1.50',
    'huaweicloudsdkcampusgo==3.1.50',
    'huaweicloudsdkcbh==3.1.50',
    'huaweicloudsdkcbr==3.1.50',
    'huaweicloudsdkcbs==3.1.50',
    'huaweicloudsdkcc==3.1.50',
    'huaweicloudsdkcce==3.1.50',
    'huaweicloudsdkccm==3.1.50',
    'huaweicloudsdkcdm==3.1.50',
    'huaweicloudsdkcdn==3.1.50',
    'huaweicloudsdkces==3.1.50',
    'huaweicloudsdkcfw==3.1.50',
    'huaweicloudsdkcgs==3.1.50',
    'huaweicloudsdkclassroom==3.1.50',
    'huaweicloudsdkcloudide==3.1.50',
    'huaweicloudsdkcloudpipeline==3.1.50',
    'huaweicloudsdkcloudrtc==3.1.50',
    'huaweicloudsdkcloudtable==3.1.50',
    'huaweicloudsdkcloudtest==3.1.50',
    'huaweicloudsdkcodeartsartifact==3.1.50',
    'huaweicloudsdkcodeartsbuild==3.1.50',
    'huaweicloudsdkcodeartscheck==3.1.50',
    'huaweicloudsdkcodeartsdeploy==3.1.50',
    'huaweicloudsdkcodecraft==3.1.50',
    'huaweicloudsdkcodehub==3.1.50',
    'huaweicloudsdkconfig==3.1.50',
    'huaweicloudsdkcph==3.1.50',
    'huaweicloudsdkcpts==3.1.50',
    'huaweicloudsdkcse==3.1.50',
    'huaweicloudsdkcsms==3.1.50',
    'huaweicloudsdkcss==3.1.50',
    'huaweicloudsdkcts==3.1.50',
    'huaweicloudsdkdas==3.1.50',
    'huaweicloudsdkdataartsstudio==3.1.50',
    'huaweicloudsdkdbss==3.1.50',
    'huaweicloudsdkdc==3.1.50',
    'huaweicloudsdkdcs==3.1.50',
    'huaweicloudsdkddm==3.1.50',
    'huaweicloudsdkdds==3.1.50',
    'huaweicloudsdkdeh==3.1.50',
    'huaweicloudsdkdevsecurity==3.1.50',
    'huaweicloudsdkdevstar==3.1.50',
    'huaweicloudsdkdgc==3.1.50',
    'huaweicloudsdkdlf==3.1.50',
    'huaweicloudsdkdli==3.1.50',
    'huaweicloudsdkdns==3.1.50',
    'huaweicloudsdkdris==3.1.50',
    'huaweicloudsdkdrs==3.1.50',
    'huaweicloudsdkdsc==3.1.50',
    'huaweicloudsdkdwr==3.1.50',
    'huaweicloudsdkdws==3.1.50',
    'huaweicloudsdkecs==3.1.50',
    'huaweicloudsdkeg==3.1.50',
    'huaweicloudsdkeihealth==3.1.50',
    'huaweicloudsdkeip==3.1.50',
    'huaweicloudsdkelb==3.1.50',
    'huaweicloudsdkeps==3.1.50',
    'huaweicloudsdker==3.1.50',
    'huaweicloudsdkevs==3.1.50',
    'huaweicloudsdkfrs==3.1.50',
    'huaweicloudsdkfunctiongraph==3.1.50',
    'huaweicloudsdkga==3.1.50',
    'huaweicloudsdkgaussdb==3.1.50',
    'huaweicloudsdkgaussdbfornosql==3.1.50',
    'huaweicloudsdkgaussdbforopengauss==3.1.50',
    'huaweicloudsdkges==3.1.50',
    'huaweicloudsdkgsl==3.1.50',
    'huaweicloudsdkhilens==3.1.50',
    'huaweicloudsdkhss==3.1.50',
    'huaweicloudsdkiam==3.1.50',
    'huaweicloudsdkidentitycenter==3.1.50',
    'huaweicloudsdkidme==3.1.50',
    'huaweicloudsdkiec==3.1.50',
    'huaweicloudsdkief==3.1.50',
    'huaweicloudsdkies==3.1.50',
    'huaweicloudsdkimage==3.1.50',
    'huaweicloudsdkimagesearch==3.1.50',
    'huaweicloudsdkims==3.1.50',
    'huaweicloudsdkiotanalytics==3.1.50',
    'huaweicloudsdkiotda==3.1.50',
    'huaweicloudsdkiotedge==3.1.50',
    'huaweicloudsdkivs==3.1.50',
    'huaweicloudsdkkafka==3.1.50',
    'huaweicloudsdkkms==3.1.50',
    'huaweicloudsdkkoomessage==3.1.50',
    'huaweicloudsdkkps==3.1.50',
    'huaweicloudsdklakeformation==3.1.50',
    'huaweicloudsdklive==3.1.50',
    'huaweicloudsdklts==3.1.50',
    'huaweicloudsdkmapds==3.1.50',
    'huaweicloudsdkmas==3.1.50',
    'huaweicloudsdkmeeting==3.1.50',
    'huaweicloudsdkmetastudio==3.1.50',
    'huaweicloudsdkmoderation==3.1.50',
    'huaweicloudsdkmpc==3.1.50',
    'huaweicloudsdkmrs==3.1.50',
    'huaweicloudsdkmsgsms==3.1.50',
    'huaweicloudsdknat==3.1.50',
    'huaweicloudsdknlp==3.1.50',
    'huaweicloudsdkocr==3.1.50',
    'huaweicloudsdkoms==3.1.50',
    'huaweicloudsdkorganizations==3.1.50',
    'huaweicloudsdkoroas==3.1.50',
    'huaweicloudsdkosm==3.1.50',
    'huaweicloudsdkpangulargemodels==3.1.50',
    'huaweicloudsdkprojectman==3.1.50',
    'huaweicloudsdkrabbitmq==3.1.50',
    'huaweicloudsdkram==3.1.50',
    'huaweicloudsdkrds==3.1.50',
    'huaweicloudsdkres==3.1.50',
    'huaweicloudsdkrms==3.1.50',
    'huaweicloudsdkrocketmq==3.1.50',
    'huaweicloudsdkroma==3.1.50',
    'huaweicloudsdksa==3.1.50',
    'huaweicloudsdkscm==3.1.50',
    'huaweicloudsdksdrs==3.1.50',
    'huaweicloudsdksecmaster==3.1.50',
    'huaweicloudsdkservicestage==3.1.50',
    'huaweicloudsdksfsturbo==3.1.50',
    'huaweicloudsdksis==3.1.50',
    'huaweicloudsdksmn==3.1.50',
    'huaweicloudsdksms==3.1.50',
    'huaweicloudsdkswr==3.1.50',
    'huaweicloudsdktms==3.1.50',
    'huaweicloudsdkugo==3.1.50',
    'huaweicloudsdkvas==3.1.50',
    'huaweicloudsdkvcm==3.1.50',
    'huaweicloudsdkvod==3.1.50',
    'huaweicloudsdkvpc==3.1.50',
    'huaweicloudsdkvpcep==3.1.50',
    'huaweicloudsdkvss==3.1.50',
    'huaweicloudsdkwaf==3.1.50',
    'huaweicloudsdkworkspace==3.1.50',
    'huaweicloudsdkworkspaceapp==3.1.50',
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
