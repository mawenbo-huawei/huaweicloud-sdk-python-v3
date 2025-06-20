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
VERSION = "3.1.150"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.150',
    'huaweicloudsdkaad==3.1.150',
    'huaweicloudsdkantiddos==3.1.150',
    'huaweicloudsdkaom==3.1.150',
    'huaweicloudsdkaos==3.1.150',
    'huaweicloudsdkapig==3.1.150',
    'huaweicloudsdkapm==3.1.150',
    'huaweicloudsdkas==3.1.150',
    'huaweicloudsdkasm==3.1.150',
    'huaweicloudsdkbcs==3.1.150',
    'huaweicloudsdkbms==3.1.150',
    'huaweicloudsdkbss==3.1.150',
    'huaweicloudsdkbssintl==3.1.150',
    'huaweicloudsdkcae==3.1.150',
    'huaweicloudsdkcampusgo==3.1.150',
    'huaweicloudsdkcbh==3.1.150',
    'huaweicloudsdkcbr==3.1.150',
    'huaweicloudsdkcbs==3.1.150',
    'huaweicloudsdkcc==3.1.150',
    'huaweicloudsdkcce==3.1.150',
    'huaweicloudsdkccm==3.1.150',
    'huaweicloudsdkcdm==3.1.150',
    'huaweicloudsdkcdn==3.1.150',
    'huaweicloudsdkces==3.1.150',
    'huaweicloudsdkcfw==3.1.150',
    'huaweicloudsdkcgs==3.1.150',
    'huaweicloudsdkclassroom==3.1.150',
    'huaweicloudsdkcloudide==3.1.150',
    'huaweicloudsdkcloudpond==3.1.150',
    'huaweicloudsdkcloudrtc==3.1.150',
    'huaweicloudsdkcloudtable==3.1.150',
    'huaweicloudsdkcloudtest==3.1.150',
    'huaweicloudsdkcoc==3.1.150',
    'huaweicloudsdkcodeartsartifact==3.1.150',
    'huaweicloudsdkcodeartsbuild==3.1.150',
    'huaweicloudsdkcodeartscheck==3.1.150',
    'huaweicloudsdkcodeartsdeploy==3.1.150',
    'huaweicloudsdkcodeartsgovernance==3.1.150',
    'huaweicloudsdkcodeartsinspector==3.1.150',
    'huaweicloudsdkcodeartspipeline==3.1.150',
    'huaweicloudsdkcodecraft==3.1.150',
    'huaweicloudsdkcodehub==3.1.150',
    'huaweicloudsdkconfig==3.1.150',
    'huaweicloudsdkcph==3.1.150',
    'huaweicloudsdkcpts==3.1.150',
    'huaweicloudsdkcse==3.1.150',
    'huaweicloudsdkcsms==3.1.150',
    'huaweicloudsdkcss==3.1.150',
    'huaweicloudsdkcts==3.1.150',
    'huaweicloudsdkdas==3.1.150',
    'huaweicloudsdkdataartsfabric==3.1.150',
    'huaweicloudsdkdataartsfabricep==3.1.150',
    'huaweicloudsdkdataartsstudio==3.1.150',
    'huaweicloudsdkdbss==3.1.150',
    'huaweicloudsdkdc==3.1.150',
    'huaweicloudsdkdcs==3.1.150',
    'huaweicloudsdkddm==3.1.150',
    'huaweicloudsdkdds==3.1.150',
    'huaweicloudsdkdeh==3.1.150',
    'huaweicloudsdkdevstar==3.1.150',
    'huaweicloudsdkdgc==3.1.150',
    'huaweicloudsdkdis==3.1.150',
    'huaweicloudsdkdlf==3.1.150',
    'huaweicloudsdkdli==3.1.150',
    'huaweicloudsdkdns==3.1.150',
    'huaweicloudsdkdris==3.1.150',
    'huaweicloudsdkdrs==3.1.150',
    'huaweicloudsdkdsc==3.1.150',
    'huaweicloudsdkdwr==3.1.150',
    'huaweicloudsdkdws==3.1.150',
    'huaweicloudsdkec==3.1.150',
    'huaweicloudsdkecs==3.1.150',
    'huaweicloudsdkedgesec==3.1.150',
    'huaweicloudsdkeg==3.1.150',
    'huaweicloudsdkeihealth==3.1.150',
    'huaweicloudsdkeip==3.1.150',
    'huaweicloudsdkelb==3.1.150',
    'huaweicloudsdkeps==3.1.150',
    'huaweicloudsdker==3.1.150',
    'huaweicloudsdkevs==3.1.150',
    'huaweicloudsdkfrs==3.1.150',
    'huaweicloudsdkfunctiongraph==3.1.150',
    'huaweicloudsdkga==3.1.150',
    'huaweicloudsdkgaussdb==3.1.150',
    'huaweicloudsdkgaussdbfornosql==3.1.150',
    'huaweicloudsdkgaussdbforopengauss==3.1.150',
    'huaweicloudsdkgeip==3.1.150',
    'huaweicloudsdkges==3.1.150',
    'huaweicloudsdkgsl==3.1.150',
    'huaweicloudsdkhilens==3.1.150',
    'huaweicloudsdkhss==3.1.150',
    'huaweicloudsdkiam==3.1.150',
    'huaweicloudsdkiamaccessanalyzer==3.1.150',
    'huaweicloudsdkidentitycenter==3.1.150',
    'huaweicloudsdkidentitycenteroidc==3.1.150',
    'huaweicloudsdkidentitycenterportalapi==3.1.150',
    'huaweicloudsdkidentitycenterscim==3.1.150',
    'huaweicloudsdkidentitycenterstore==3.1.150',
    'huaweicloudsdkidme==3.1.150',
    'huaweicloudsdkidmeclassicapi==3.1.150',
    'huaweicloudsdkiec==3.1.150',
    'huaweicloudsdkief==3.1.150',
    'huaweicloudsdkimage==3.1.150',
    'huaweicloudsdkimagesearch==3.1.150',
    'huaweicloudsdkims==3.1.150',
    'huaweicloudsdkiotanalytics==3.1.150',
    'huaweicloudsdkiotda==3.1.150',
    'huaweicloudsdkiotdm==3.1.150',
    'huaweicloudsdkiotedge==3.1.150',
    'huaweicloudsdkivs==3.1.150',
    'huaweicloudsdkkafka==3.1.150',
    'huaweicloudsdkkms==3.1.150',
    'huaweicloudsdkkoomessage==3.1.150',
    'huaweicloudsdkkps==3.1.150',
    'huaweicloudsdkkvs==3.1.150',
    'huaweicloudsdklakeformation==3.1.150',
    'huaweicloudsdklive==3.1.150',
    'huaweicloudsdklms==3.1.150',
    'huaweicloudsdklts==3.1.150',
    'huaweicloudsdkmapds==3.1.150',
    'huaweicloudsdkmas==3.1.150',
    'huaweicloudsdkmastudio==3.1.150',
    'huaweicloudsdkmeeting==3.1.150',
    'huaweicloudsdkmetastudio==3.1.150',
    'huaweicloudsdkmoderation==3.1.150',
    'huaweicloudsdkmpc==3.1.150',
    'huaweicloudsdkmrs==3.1.150',
    'huaweicloudsdkmsgsms==3.1.150',
    'huaweicloudsdkmssi==3.1.150',
    'huaweicloudsdknat==3.1.150',
    'huaweicloudsdknlp==3.1.150',
    'huaweicloudsdkobs==3.1.150',
    'huaweicloudsdkocr==3.1.150',
    'huaweicloudsdkoctopus==3.1.150',
    'huaweicloudsdkoms==3.1.150',
    'huaweicloudsdkoptverse==3.1.150',
    'huaweicloudsdkorganizations==3.1.150',
    'huaweicloudsdkorgid==3.1.150',
    'huaweicloudsdkoroas==3.1.150',
    'huaweicloudsdkosm==3.1.150',
    'huaweicloudsdkpangulargemodels==3.1.150',
    'huaweicloudsdkprojectman==3.1.150',
    'huaweicloudsdkrabbitmq==3.1.150',
    'huaweicloudsdkram==3.1.150',
    'huaweicloudsdkrds==3.1.150',
    'huaweicloudsdkres==3.1.150',
    'huaweicloudsdkrgc==3.1.150',
    'huaweicloudsdkrms==3.1.150',
    'huaweicloudsdkrocketmq==3.1.150',
    'huaweicloudsdkroma==3.1.150',
    'huaweicloudsdksa==3.1.150',
    'huaweicloudsdkscm==3.1.150',
    'huaweicloudsdksdrs==3.1.150',
    'huaweicloudsdksecmaster==3.1.150',
    'huaweicloudsdkservicestage==3.1.150',
    'huaweicloudsdksfsturbo==3.1.150',
    'huaweicloudsdksis==3.1.150',
    'huaweicloudsdksmn==3.1.150',
    'huaweicloudsdksmnglobal==3.1.150',
    'huaweicloudsdksms==3.1.150',
    'huaweicloudsdksmsapi==3.1.150',
    'huaweicloudsdksts==3.1.150',
    'huaweicloudsdkswr==3.1.150',
    'huaweicloudsdktics==3.1.150',
    'huaweicloudsdktms==3.1.150',
    'huaweicloudsdkugo==3.1.150',
    'huaweicloudsdkvas==3.1.150',
    'huaweicloudsdkvcm==3.1.150',
    'huaweicloudsdkvod==3.1.150',
    'huaweicloudsdkvpc==3.1.150',
    'huaweicloudsdkvpcep==3.1.150',
    'huaweicloudsdkvpn==3.1.150',
    'huaweicloudsdkwaf==3.1.150',
    'huaweicloudsdkworkspace==3.1.150',
    'huaweicloudsdkworkspaceapp==3.1.150',
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
