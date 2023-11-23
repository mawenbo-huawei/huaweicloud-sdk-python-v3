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
VERSION = "3.1.69"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.69',
    'huaweicloudsdkaad==3.1.69',
    'huaweicloudsdkantiddos==3.1.69',
    'huaweicloudsdkaom==3.1.69',
    'huaweicloudsdkaos==3.1.69',
    'huaweicloudsdkapig==3.1.69',
    'huaweicloudsdkapm==3.1.69',
    'huaweicloudsdkas==3.1.69',
    'huaweicloudsdkasm==3.1.69',
    'huaweicloudsdkbcs==3.1.69',
    'huaweicloudsdkbms==3.1.69',
    'huaweicloudsdkbss==3.1.69',
    'huaweicloudsdkbssintl==3.1.69',
    'huaweicloudsdkcae==3.1.69',
    'huaweicloudsdkcampusgo==3.1.69',
    'huaweicloudsdkcbh==3.1.69',
    'huaweicloudsdkcbr==3.1.69',
    'huaweicloudsdkcbs==3.1.69',
    'huaweicloudsdkcc==3.1.69',
    'huaweicloudsdkcce==3.1.69',
    'huaweicloudsdkccm==3.1.69',
    'huaweicloudsdkcdm==3.1.69',
    'huaweicloudsdkcdn==3.1.69',
    'huaweicloudsdkces==3.1.69',
    'huaweicloudsdkcfw==3.1.69',
    'huaweicloudsdkcgs==3.1.69',
    'huaweicloudsdkclassroom==3.1.69',
    'huaweicloudsdkcloudide==3.1.69',
    'huaweicloudsdkcloudpond==3.1.69',
    'huaweicloudsdkcloudrtc==3.1.69',
    'huaweicloudsdkcloudtable==3.1.69',
    'huaweicloudsdkcloudtest==3.1.69',
    'huaweicloudsdkcodeartsartifact==3.1.69',
    'huaweicloudsdkcodeartsbuild==3.1.69',
    'huaweicloudsdkcodeartscheck==3.1.69',
    'huaweicloudsdkcodeartsdeploy==3.1.69',
    'huaweicloudsdkcodeartsinspector==3.1.69',
    'huaweicloudsdkcodeartspipeline==3.1.69',
    'huaweicloudsdkcodecraft==3.1.69',
    'huaweicloudsdkcodehub==3.1.69',
    'huaweicloudsdkconfig==3.1.69',
    'huaweicloudsdkcph==3.1.69',
    'huaweicloudsdkcpts==3.1.69',
    'huaweicloudsdkcse==3.1.69',
    'huaweicloudsdkcsms==3.1.69',
    'huaweicloudsdkcss==3.1.69',
    'huaweicloudsdkcts==3.1.69',
    'huaweicloudsdkdas==3.1.69',
    'huaweicloudsdkdataartsstudio==3.1.69',
    'huaweicloudsdkdbss==3.1.69',
    'huaweicloudsdkdc==3.1.69',
    'huaweicloudsdkdcs==3.1.69',
    'huaweicloudsdkddm==3.1.69',
    'huaweicloudsdkdds==3.1.69',
    'huaweicloudsdkdeh==3.1.69',
    'huaweicloudsdkdevsecurity==3.1.69',
    'huaweicloudsdkdevstar==3.1.69',
    'huaweicloudsdkdgc==3.1.69',
    'huaweicloudsdkdlf==3.1.69',
    'huaweicloudsdkdli==3.1.69',
    'huaweicloudsdkdns==3.1.69',
    'huaweicloudsdkdris==3.1.69',
    'huaweicloudsdkdrs==3.1.69',
    'huaweicloudsdkdsc==3.1.69',
    'huaweicloudsdkdwr==3.1.69',
    'huaweicloudsdkdws==3.1.69',
    'huaweicloudsdkec==3.1.69',
    'huaweicloudsdkecs==3.1.69',
    'huaweicloudsdkedgesec==3.1.69',
    'huaweicloudsdkeg==3.1.69',
    'huaweicloudsdkeihealth==3.1.69',
    'huaweicloudsdkeip==3.1.69',
    'huaweicloudsdkelb==3.1.69',
    'huaweicloudsdkeps==3.1.69',
    'huaweicloudsdker==3.1.69',
    'huaweicloudsdkevs==3.1.69',
    'huaweicloudsdkfrs==3.1.69',
    'huaweicloudsdkfunctiongraph==3.1.69',
    'huaweicloudsdkga==3.1.69',
    'huaweicloudsdkgaussdb==3.1.69',
    'huaweicloudsdkgaussdbfornosql==3.1.69',
    'huaweicloudsdkgaussdbforopengauss==3.1.69',
    'huaweicloudsdkges==3.1.69',
    'huaweicloudsdkgsl==3.1.69',
    'huaweicloudsdkhilens==3.1.69',
    'huaweicloudsdkhss==3.1.69',
    'huaweicloudsdkiam==3.1.69',
    'huaweicloudsdkidentitycenter==3.1.69',
    'huaweicloudsdkidentitycenterstore==3.1.69',
    'huaweicloudsdkidme==3.1.69',
    'huaweicloudsdkiec==3.1.69',
    'huaweicloudsdkief==3.1.69',
    'huaweicloudsdkimage==3.1.69',
    'huaweicloudsdkimagesearch==3.1.69',
    'huaweicloudsdkims==3.1.69',
    'huaweicloudsdkiotanalytics==3.1.69',
    'huaweicloudsdkiotda==3.1.69',
    'huaweicloudsdkiotedge==3.1.69',
    'huaweicloudsdkivs==3.1.69',
    'huaweicloudsdkkafka==3.1.69',
    'huaweicloudsdkkms==3.1.69',
    'huaweicloudsdkkoomessage==3.1.69',
    'huaweicloudsdkkps==3.1.69',
    'huaweicloudsdklakeformation==3.1.69',
    'huaweicloudsdklive==3.1.69',
    'huaweicloudsdklts==3.1.69',
    'huaweicloudsdkmapds==3.1.69',
    'huaweicloudsdkmas==3.1.69',
    'huaweicloudsdkmeeting==3.1.69',
    'huaweicloudsdkmetastudio==3.1.69',
    'huaweicloudsdkmoderation==3.1.69',
    'huaweicloudsdkmpc==3.1.69',
    'huaweicloudsdkmrs==3.1.69',
    'huaweicloudsdkmsgsms==3.1.69',
    'huaweicloudsdkmssi==3.1.69',
    'huaweicloudsdknat==3.1.69',
    'huaweicloudsdknlp==3.1.69',
    'huaweicloudsdkocr==3.1.69',
    'huaweicloudsdkoms==3.1.69',
    'huaweicloudsdkoptverse==3.1.69',
    'huaweicloudsdkorganizations==3.1.69',
    'huaweicloudsdkoroas==3.1.69',
    'huaweicloudsdkosm==3.1.69',
    'huaweicloudsdkpangulargemodels==3.1.69',
    'huaweicloudsdkprojectman==3.1.69',
    'huaweicloudsdkrabbitmq==3.1.69',
    'huaweicloudsdkram==3.1.69',
    'huaweicloudsdkrds==3.1.69',
    'huaweicloudsdkres==3.1.69',
    'huaweicloudsdkrms==3.1.69',
    'huaweicloudsdkrocketmq==3.1.69',
    'huaweicloudsdkroma==3.1.69',
    'huaweicloudsdksa==3.1.69',
    'huaweicloudsdkscm==3.1.69',
    'huaweicloudsdksdrs==3.1.69',
    'huaweicloudsdksecmaster==3.1.69',
    'huaweicloudsdkservicestage==3.1.69',
    'huaweicloudsdksfsturbo==3.1.69',
    'huaweicloudsdksis==3.1.69',
    'huaweicloudsdksmn==3.1.69',
    'huaweicloudsdksms==3.1.69',
    'huaweicloudsdkswr==3.1.69',
    'huaweicloudsdktics==3.1.69',
    'huaweicloudsdktms==3.1.69',
    'huaweicloudsdkugo==3.1.69',
    'huaweicloudsdkvas==3.1.69',
    'huaweicloudsdkvcm==3.1.69',
    'huaweicloudsdkvod==3.1.69',
    'huaweicloudsdkvpc==3.1.69',
    'huaweicloudsdkvpcep==3.1.69',
    'huaweicloudsdkvpn==3.1.69',
    'huaweicloudsdkwaf==3.1.69',
    'huaweicloudsdkworkspace==3.1.69',
    'huaweicloudsdkworkspaceapp==3.1.69',
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
