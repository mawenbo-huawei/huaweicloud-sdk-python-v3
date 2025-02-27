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
VERSION = "3.1.137"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.137',
    'huaweicloudsdkaad==3.1.137',
    'huaweicloudsdkantiddos==3.1.137',
    'huaweicloudsdkaom==3.1.137',
    'huaweicloudsdkaos==3.1.137',
    'huaweicloudsdkapig==3.1.137',
    'huaweicloudsdkapm==3.1.137',
    'huaweicloudsdkas==3.1.137',
    'huaweicloudsdkasm==3.1.137',
    'huaweicloudsdkbcs==3.1.137',
    'huaweicloudsdkbms==3.1.137',
    'huaweicloudsdkbss==3.1.137',
    'huaweicloudsdkbssintl==3.1.137',
    'huaweicloudsdkcae==3.1.137',
    'huaweicloudsdkcampusgo==3.1.137',
    'huaweicloudsdkcbh==3.1.137',
    'huaweicloudsdkcbr==3.1.137',
    'huaweicloudsdkcbs==3.1.137',
    'huaweicloudsdkcc==3.1.137',
    'huaweicloudsdkcce==3.1.137',
    'huaweicloudsdkccm==3.1.137',
    'huaweicloudsdkcdm==3.1.137',
    'huaweicloudsdkcdn==3.1.137',
    'huaweicloudsdkces==3.1.137',
    'huaweicloudsdkcfw==3.1.137',
    'huaweicloudsdkcgs==3.1.137',
    'huaweicloudsdkclassroom==3.1.137',
    'huaweicloudsdkcloudide==3.1.137',
    'huaweicloudsdkcloudpond==3.1.137',
    'huaweicloudsdkcloudrtc==3.1.137',
    'huaweicloudsdkcloudtable==3.1.137',
    'huaweicloudsdkcloudtest==3.1.137',
    'huaweicloudsdkcoc==3.1.137',
    'huaweicloudsdkcodeartsartifact==3.1.137',
    'huaweicloudsdkcodeartsbuild==3.1.137',
    'huaweicloudsdkcodeartscheck==3.1.137',
    'huaweicloudsdkcodeartsdeploy==3.1.137',
    'huaweicloudsdkcodeartsgovernance==3.1.137',
    'huaweicloudsdkcodeartsinspector==3.1.137',
    'huaweicloudsdkcodeartspipeline==3.1.137',
    'huaweicloudsdkcodecraft==3.1.137',
    'huaweicloudsdkcodehub==3.1.137',
    'huaweicloudsdkconfig==3.1.137',
    'huaweicloudsdkcph==3.1.137',
    'huaweicloudsdkcpts==3.1.137',
    'huaweicloudsdkcse==3.1.137',
    'huaweicloudsdkcsms==3.1.137',
    'huaweicloudsdkcss==3.1.137',
    'huaweicloudsdkcts==3.1.137',
    'huaweicloudsdkdas==3.1.137',
    'huaweicloudsdkdataartsfabric==3.1.137',
    'huaweicloudsdkdataartsfabricep==3.1.137',
    'huaweicloudsdkdataartsstudio==3.1.137',
    'huaweicloudsdkdbss==3.1.137',
    'huaweicloudsdkdc==3.1.137',
    'huaweicloudsdkdcs==3.1.137',
    'huaweicloudsdkddm==3.1.137',
    'huaweicloudsdkdds==3.1.137',
    'huaweicloudsdkdeh==3.1.137',
    'huaweicloudsdkdevstar==3.1.137',
    'huaweicloudsdkdgc==3.1.137',
    'huaweicloudsdkdis==3.1.137',
    'huaweicloudsdkdlf==3.1.137',
    'huaweicloudsdkdli==3.1.137',
    'huaweicloudsdkdns==3.1.137',
    'huaweicloudsdkdris==3.1.137',
    'huaweicloudsdkdrs==3.1.137',
    'huaweicloudsdkdsc==3.1.137',
    'huaweicloudsdkdwr==3.1.137',
    'huaweicloudsdkdws==3.1.137',
    'huaweicloudsdkec==3.1.137',
    'huaweicloudsdkecs==3.1.137',
    'huaweicloudsdkedgesec==3.1.137',
    'huaweicloudsdkeg==3.1.137',
    'huaweicloudsdkeihealth==3.1.137',
    'huaweicloudsdkeip==3.1.137',
    'huaweicloudsdkelb==3.1.137',
    'huaweicloudsdkeps==3.1.137',
    'huaweicloudsdker==3.1.137',
    'huaweicloudsdkevs==3.1.137',
    'huaweicloudsdkfrs==3.1.137',
    'huaweicloudsdkfunctiongraph==3.1.137',
    'huaweicloudsdkga==3.1.137',
    'huaweicloudsdkgaussdb==3.1.137',
    'huaweicloudsdkgaussdbfornosql==3.1.137',
    'huaweicloudsdkgaussdbforopengauss==3.1.137',
    'huaweicloudsdkgeip==3.1.137',
    'huaweicloudsdkges==3.1.137',
    'huaweicloudsdkgsl==3.1.137',
    'huaweicloudsdkhilens==3.1.137',
    'huaweicloudsdkhss==3.1.137',
    'huaweicloudsdkiam==3.1.137',
    'huaweicloudsdkiamaccessanalyzer==3.1.137',
    'huaweicloudsdkidentitycenter==3.1.137',
    'huaweicloudsdkidentitycenterstore==3.1.137',
    'huaweicloudsdkidme==3.1.137',
    'huaweicloudsdkidmeclassicapi==3.1.137',
    'huaweicloudsdkiec==3.1.137',
    'huaweicloudsdkief==3.1.137',
    'huaweicloudsdkimage==3.1.137',
    'huaweicloudsdkimagesearch==3.1.137',
    'huaweicloudsdkims==3.1.137',
    'huaweicloudsdkiotanalytics==3.1.137',
    'huaweicloudsdkiotda==3.1.137',
    'huaweicloudsdkiotdm==3.1.137',
    'huaweicloudsdkiotedge==3.1.137',
    'huaweicloudsdkivs==3.1.137',
    'huaweicloudsdkkafka==3.1.137',
    'huaweicloudsdkkms==3.1.137',
    'huaweicloudsdkkoomessage==3.1.137',
    'huaweicloudsdkkps==3.1.137',
    'huaweicloudsdkkvs==3.1.137',
    'huaweicloudsdklakeformation==3.1.137',
    'huaweicloudsdklive==3.1.137',
    'huaweicloudsdklts==3.1.137',
    'huaweicloudsdkmapds==3.1.137',
    'huaweicloudsdkmas==3.1.137',
    'huaweicloudsdkmastudio==3.1.137',
    'huaweicloudsdkmeeting==3.1.137',
    'huaweicloudsdkmetastudio==3.1.137',
    'huaweicloudsdkmoderation==3.1.137',
    'huaweicloudsdkmpc==3.1.137',
    'huaweicloudsdkmrs==3.1.137',
    'huaweicloudsdkmsgsms==3.1.137',
    'huaweicloudsdkmssi==3.1.137',
    'huaweicloudsdknat==3.1.137',
    'huaweicloudsdknlp==3.1.137',
    'huaweicloudsdkobs==3.1.137',
    'huaweicloudsdkocr==3.1.137',
    'huaweicloudsdkoctopus==3.1.137',
    'huaweicloudsdkoms==3.1.137',
    'huaweicloudsdkoptverse==3.1.137',
    'huaweicloudsdkorganizations==3.1.137',
    'huaweicloudsdkorgid==3.1.137',
    'huaweicloudsdkoroas==3.1.137',
    'huaweicloudsdkosm==3.1.137',
    'huaweicloudsdkpangulargemodels==3.1.137',
    'huaweicloudsdkprojectman==3.1.137',
    'huaweicloudsdkrabbitmq==3.1.137',
    'huaweicloudsdkram==3.1.137',
    'huaweicloudsdkrds==3.1.137',
    'huaweicloudsdkres==3.1.137',
    'huaweicloudsdkrgc==3.1.137',
    'huaweicloudsdkrms==3.1.137',
    'huaweicloudsdkrocketmq==3.1.137',
    'huaweicloudsdkroma==3.1.137',
    'huaweicloudsdksa==3.1.137',
    'huaweicloudsdkscm==3.1.137',
    'huaweicloudsdksdrs==3.1.137',
    'huaweicloudsdksecmaster==3.1.137',
    'huaweicloudsdkservicestage==3.1.137',
    'huaweicloudsdksfsturbo==3.1.137',
    'huaweicloudsdksis==3.1.137',
    'huaweicloudsdksmn==3.1.137',
    'huaweicloudsdksmnglobal==3.1.137',
    'huaweicloudsdksms==3.1.137',
    'huaweicloudsdksmsapi==3.1.137',
    'huaweicloudsdksts==3.1.137',
    'huaweicloudsdkswr==3.1.137',
    'huaweicloudsdktics==3.1.137',
    'huaweicloudsdktms==3.1.137',
    'huaweicloudsdkugo==3.1.137',
    'huaweicloudsdkvas==3.1.137',
    'huaweicloudsdkvcm==3.1.137',
    'huaweicloudsdkvod==3.1.137',
    'huaweicloudsdkvpc==3.1.137',
    'huaweicloudsdkvpcep==3.1.137',
    'huaweicloudsdkvpn==3.1.137',
    'huaweicloudsdkwaf==3.1.137',
    'huaweicloudsdkworkspace==3.1.137',
    'huaweicloudsdkworkspaceapp==3.1.137',
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
