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
VERSION = "3.1.139"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.139',
    'huaweicloudsdkaad==3.1.139',
    'huaweicloudsdkantiddos==3.1.139',
    'huaweicloudsdkaom==3.1.139',
    'huaweicloudsdkaos==3.1.139',
    'huaweicloudsdkapig==3.1.139',
    'huaweicloudsdkapm==3.1.139',
    'huaweicloudsdkas==3.1.139',
    'huaweicloudsdkasm==3.1.139',
    'huaweicloudsdkbcs==3.1.139',
    'huaweicloudsdkbms==3.1.139',
    'huaweicloudsdkbss==3.1.139',
    'huaweicloudsdkbssintl==3.1.139',
    'huaweicloudsdkcae==3.1.139',
    'huaweicloudsdkcampusgo==3.1.139',
    'huaweicloudsdkcbh==3.1.139',
    'huaweicloudsdkcbr==3.1.139',
    'huaweicloudsdkcbs==3.1.139',
    'huaweicloudsdkcc==3.1.139',
    'huaweicloudsdkcce==3.1.139',
    'huaweicloudsdkccm==3.1.139',
    'huaweicloudsdkcdm==3.1.139',
    'huaweicloudsdkcdn==3.1.139',
    'huaweicloudsdkces==3.1.139',
    'huaweicloudsdkcfw==3.1.139',
    'huaweicloudsdkcgs==3.1.139',
    'huaweicloudsdkclassroom==3.1.139',
    'huaweicloudsdkcloudide==3.1.139',
    'huaweicloudsdkcloudpond==3.1.139',
    'huaweicloudsdkcloudrtc==3.1.139',
    'huaweicloudsdkcloudtable==3.1.139',
    'huaweicloudsdkcloudtest==3.1.139',
    'huaweicloudsdkcoc==3.1.139',
    'huaweicloudsdkcodeartsartifact==3.1.139',
    'huaweicloudsdkcodeartsbuild==3.1.139',
    'huaweicloudsdkcodeartscheck==3.1.139',
    'huaweicloudsdkcodeartsdeploy==3.1.139',
    'huaweicloudsdkcodeartsgovernance==3.1.139',
    'huaweicloudsdkcodeartsinspector==3.1.139',
    'huaweicloudsdkcodeartspipeline==3.1.139',
    'huaweicloudsdkcodecraft==3.1.139',
    'huaweicloudsdkcodehub==3.1.139',
    'huaweicloudsdkconfig==3.1.139',
    'huaweicloudsdkcph==3.1.139',
    'huaweicloudsdkcpts==3.1.139',
    'huaweicloudsdkcse==3.1.139',
    'huaweicloudsdkcsms==3.1.139',
    'huaweicloudsdkcss==3.1.139',
    'huaweicloudsdkcts==3.1.139',
    'huaweicloudsdkdas==3.1.139',
    'huaweicloudsdkdataartsfabric==3.1.139',
    'huaweicloudsdkdataartsfabricep==3.1.139',
    'huaweicloudsdkdataartsstudio==3.1.139',
    'huaweicloudsdkdbss==3.1.139',
    'huaweicloudsdkdc==3.1.139',
    'huaweicloudsdkdcs==3.1.139',
    'huaweicloudsdkddm==3.1.139',
    'huaweicloudsdkdds==3.1.139',
    'huaweicloudsdkdeh==3.1.139',
    'huaweicloudsdkdevstar==3.1.139',
    'huaweicloudsdkdgc==3.1.139',
    'huaweicloudsdkdis==3.1.139',
    'huaweicloudsdkdlf==3.1.139',
    'huaweicloudsdkdli==3.1.139',
    'huaweicloudsdkdns==3.1.139',
    'huaweicloudsdkdris==3.1.139',
    'huaweicloudsdkdrs==3.1.139',
    'huaweicloudsdkdsc==3.1.139',
    'huaweicloudsdkdwr==3.1.139',
    'huaweicloudsdkdws==3.1.139',
    'huaweicloudsdkec==3.1.139',
    'huaweicloudsdkecs==3.1.139',
    'huaweicloudsdkedgesec==3.1.139',
    'huaweicloudsdkeg==3.1.139',
    'huaweicloudsdkeihealth==3.1.139',
    'huaweicloudsdkeip==3.1.139',
    'huaweicloudsdkelb==3.1.139',
    'huaweicloudsdkeps==3.1.139',
    'huaweicloudsdker==3.1.139',
    'huaweicloudsdkevs==3.1.139',
    'huaweicloudsdkfrs==3.1.139',
    'huaweicloudsdkfunctiongraph==3.1.139',
    'huaweicloudsdkga==3.1.139',
    'huaweicloudsdkgaussdb==3.1.139',
    'huaweicloudsdkgaussdbfornosql==3.1.139',
    'huaweicloudsdkgaussdbforopengauss==3.1.139',
    'huaweicloudsdkgeip==3.1.139',
    'huaweicloudsdkges==3.1.139',
    'huaweicloudsdkgsl==3.1.139',
    'huaweicloudsdkhilens==3.1.139',
    'huaweicloudsdkhss==3.1.139',
    'huaweicloudsdkiam==3.1.139',
    'huaweicloudsdkiamaccessanalyzer==3.1.139',
    'huaweicloudsdkidentitycenter==3.1.139',
    'huaweicloudsdkidentitycenterstore==3.1.139',
    'huaweicloudsdkidme==3.1.139',
    'huaweicloudsdkidmeclassicapi==3.1.139',
    'huaweicloudsdkiec==3.1.139',
    'huaweicloudsdkief==3.1.139',
    'huaweicloudsdkimage==3.1.139',
    'huaweicloudsdkimagesearch==3.1.139',
    'huaweicloudsdkims==3.1.139',
    'huaweicloudsdkiotanalytics==3.1.139',
    'huaweicloudsdkiotda==3.1.139',
    'huaweicloudsdkiotdm==3.1.139',
    'huaweicloudsdkiotedge==3.1.139',
    'huaweicloudsdkivs==3.1.139',
    'huaweicloudsdkkafka==3.1.139',
    'huaweicloudsdkkms==3.1.139',
    'huaweicloudsdkkoomessage==3.1.139',
    'huaweicloudsdkkps==3.1.139',
    'huaweicloudsdkkvs==3.1.139',
    'huaweicloudsdklakeformation==3.1.139',
    'huaweicloudsdklive==3.1.139',
    'huaweicloudsdklts==3.1.139',
    'huaweicloudsdkmapds==3.1.139',
    'huaweicloudsdkmas==3.1.139',
    'huaweicloudsdkmastudio==3.1.139',
    'huaweicloudsdkmeeting==3.1.139',
    'huaweicloudsdkmetastudio==3.1.139',
    'huaweicloudsdkmoderation==3.1.139',
    'huaweicloudsdkmpc==3.1.139',
    'huaweicloudsdkmrs==3.1.139',
    'huaweicloudsdkmsgsms==3.1.139',
    'huaweicloudsdkmssi==3.1.139',
    'huaweicloudsdknat==3.1.139',
    'huaweicloudsdknlp==3.1.139',
    'huaweicloudsdkobs==3.1.139',
    'huaweicloudsdkocr==3.1.139',
    'huaweicloudsdkoctopus==3.1.139',
    'huaweicloudsdkoms==3.1.139',
    'huaweicloudsdkoptverse==3.1.139',
    'huaweicloudsdkorganizations==3.1.139',
    'huaweicloudsdkorgid==3.1.139',
    'huaweicloudsdkoroas==3.1.139',
    'huaweicloudsdkosm==3.1.139',
    'huaweicloudsdkpangulargemodels==3.1.139',
    'huaweicloudsdkprojectman==3.1.139',
    'huaweicloudsdkrabbitmq==3.1.139',
    'huaweicloudsdkram==3.1.139',
    'huaweicloudsdkrds==3.1.139',
    'huaweicloudsdkres==3.1.139',
    'huaweicloudsdkrgc==3.1.139',
    'huaweicloudsdkrms==3.1.139',
    'huaweicloudsdkrocketmq==3.1.139',
    'huaweicloudsdkroma==3.1.139',
    'huaweicloudsdksa==3.1.139',
    'huaweicloudsdkscm==3.1.139',
    'huaweicloudsdksdrs==3.1.139',
    'huaweicloudsdksecmaster==3.1.139',
    'huaweicloudsdkservicestage==3.1.139',
    'huaweicloudsdksfsturbo==3.1.139',
    'huaweicloudsdksis==3.1.139',
    'huaweicloudsdksmn==3.1.139',
    'huaweicloudsdksmnglobal==3.1.139',
    'huaweicloudsdksms==3.1.139',
    'huaweicloudsdksmsapi==3.1.139',
    'huaweicloudsdksts==3.1.139',
    'huaweicloudsdkswr==3.1.139',
    'huaweicloudsdktics==3.1.139',
    'huaweicloudsdktms==3.1.139',
    'huaweicloudsdkugo==3.1.139',
    'huaweicloudsdkvas==3.1.139',
    'huaweicloudsdkvcm==3.1.139',
    'huaweicloudsdkvod==3.1.139',
    'huaweicloudsdkvpc==3.1.139',
    'huaweicloudsdkvpcep==3.1.139',
    'huaweicloudsdkvpn==3.1.139',
    'huaweicloudsdkwaf==3.1.139',
    'huaweicloudsdkworkspace==3.1.139',
    'huaweicloudsdkworkspaceapp==3.1.139',
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
