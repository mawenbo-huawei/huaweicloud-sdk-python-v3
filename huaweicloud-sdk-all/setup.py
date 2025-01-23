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
VERSION = "3.1.133"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.133',
    'huaweicloudsdkaad==3.1.133',
    'huaweicloudsdkantiddos==3.1.133',
    'huaweicloudsdkaom==3.1.133',
    'huaweicloudsdkaos==3.1.133',
    'huaweicloudsdkapig==3.1.133',
    'huaweicloudsdkapm==3.1.133',
    'huaweicloudsdkas==3.1.133',
    'huaweicloudsdkasm==3.1.133',
    'huaweicloudsdkbcs==3.1.133',
    'huaweicloudsdkbms==3.1.133',
    'huaweicloudsdkbss==3.1.133',
    'huaweicloudsdkbssintl==3.1.133',
    'huaweicloudsdkcae==3.1.133',
    'huaweicloudsdkcampusgo==3.1.133',
    'huaweicloudsdkcbh==3.1.133',
    'huaweicloudsdkcbr==3.1.133',
    'huaweicloudsdkcbs==3.1.133',
    'huaweicloudsdkcc==3.1.133',
    'huaweicloudsdkcce==3.1.133',
    'huaweicloudsdkccm==3.1.133',
    'huaweicloudsdkcdm==3.1.133',
    'huaweicloudsdkcdn==3.1.133',
    'huaweicloudsdkces==3.1.133',
    'huaweicloudsdkcfw==3.1.133',
    'huaweicloudsdkcgs==3.1.133',
    'huaweicloudsdkclassroom==3.1.133',
    'huaweicloudsdkcloudide==3.1.133',
    'huaweicloudsdkcloudpond==3.1.133',
    'huaweicloudsdkcloudrtc==3.1.133',
    'huaweicloudsdkcloudtable==3.1.133',
    'huaweicloudsdkcloudtest==3.1.133',
    'huaweicloudsdkcoc==3.1.133',
    'huaweicloudsdkcodeartsartifact==3.1.133',
    'huaweicloudsdkcodeartsbuild==3.1.133',
    'huaweicloudsdkcodeartscheck==3.1.133',
    'huaweicloudsdkcodeartsdeploy==3.1.133',
    'huaweicloudsdkcodeartsgovernance==3.1.133',
    'huaweicloudsdkcodeartsinspector==3.1.133',
    'huaweicloudsdkcodeartspipeline==3.1.133',
    'huaweicloudsdkcodecraft==3.1.133',
    'huaweicloudsdkcodehub==3.1.133',
    'huaweicloudsdkconfig==3.1.133',
    'huaweicloudsdkcph==3.1.133',
    'huaweicloudsdkcpts==3.1.133',
    'huaweicloudsdkcse==3.1.133',
    'huaweicloudsdkcsms==3.1.133',
    'huaweicloudsdkcss==3.1.133',
    'huaweicloudsdkcts==3.1.133',
    'huaweicloudsdkdas==3.1.133',
    'huaweicloudsdkdataartsfabric==3.1.133',
    'huaweicloudsdkdataartsfabricep==3.1.133',
    'huaweicloudsdkdataartsstudio==3.1.133',
    'huaweicloudsdkdbss==3.1.133',
    'huaweicloudsdkdc==3.1.133',
    'huaweicloudsdkdcs==3.1.133',
    'huaweicloudsdkddm==3.1.133',
    'huaweicloudsdkdds==3.1.133',
    'huaweicloudsdkdeh==3.1.133',
    'huaweicloudsdkdevstar==3.1.133',
    'huaweicloudsdkdgc==3.1.133',
    'huaweicloudsdkdis==3.1.133',
    'huaweicloudsdkdlf==3.1.133',
    'huaweicloudsdkdli==3.1.133',
    'huaweicloudsdkdns==3.1.133',
    'huaweicloudsdkdris==3.1.133',
    'huaweicloudsdkdrs==3.1.133',
    'huaweicloudsdkdsc==3.1.133',
    'huaweicloudsdkdwr==3.1.133',
    'huaweicloudsdkdws==3.1.133',
    'huaweicloudsdkec==3.1.133',
    'huaweicloudsdkecs==3.1.133',
    'huaweicloudsdkedgesec==3.1.133',
    'huaweicloudsdkeg==3.1.133',
    'huaweicloudsdkeihealth==3.1.133',
    'huaweicloudsdkeip==3.1.133',
    'huaweicloudsdkelb==3.1.133',
    'huaweicloudsdkeps==3.1.133',
    'huaweicloudsdker==3.1.133',
    'huaweicloudsdkevs==3.1.133',
    'huaweicloudsdkfrs==3.1.133',
    'huaweicloudsdkfunctiongraph==3.1.133',
    'huaweicloudsdkga==3.1.133',
    'huaweicloudsdkgaussdb==3.1.133',
    'huaweicloudsdkgaussdbfornosql==3.1.133',
    'huaweicloudsdkgaussdbforopengauss==3.1.133',
    'huaweicloudsdkgeip==3.1.133',
    'huaweicloudsdkges==3.1.133',
    'huaweicloudsdkgsl==3.1.133',
    'huaweicloudsdkhilens==3.1.133',
    'huaweicloudsdkhss==3.1.133',
    'huaweicloudsdkiam==3.1.133',
    'huaweicloudsdkiamaccessanalyzer==3.1.133',
    'huaweicloudsdkidentitycenter==3.1.133',
    'huaweicloudsdkidentitycenterstore==3.1.133',
    'huaweicloudsdkidme==3.1.133',
    'huaweicloudsdkidmeclassicapi==3.1.133',
    'huaweicloudsdkiec==3.1.133',
    'huaweicloudsdkief==3.1.133',
    'huaweicloudsdkimage==3.1.133',
    'huaweicloudsdkimagesearch==3.1.133',
    'huaweicloudsdkims==3.1.133',
    'huaweicloudsdkiotanalytics==3.1.133',
    'huaweicloudsdkiotda==3.1.133',
    'huaweicloudsdkiotdm==3.1.133',
    'huaweicloudsdkiotedge==3.1.133',
    'huaweicloudsdkivs==3.1.133',
    'huaweicloudsdkkafka==3.1.133',
    'huaweicloudsdkkms==3.1.133',
    'huaweicloudsdkkoomessage==3.1.133',
    'huaweicloudsdkkps==3.1.133',
    'huaweicloudsdklakeformation==3.1.133',
    'huaweicloudsdklive==3.1.133',
    'huaweicloudsdklts==3.1.133',
    'huaweicloudsdkmapds==3.1.133',
    'huaweicloudsdkmas==3.1.133',
    'huaweicloudsdkmastudio==3.1.133',
    'huaweicloudsdkmeeting==3.1.133',
    'huaweicloudsdkmetastudio==3.1.133',
    'huaweicloudsdkmoderation==3.1.133',
    'huaweicloudsdkmpc==3.1.133',
    'huaweicloudsdkmrs==3.1.133',
    'huaweicloudsdkmsgsms==3.1.133',
    'huaweicloudsdkmssi==3.1.133',
    'huaweicloudsdknat==3.1.133',
    'huaweicloudsdknlp==3.1.133',
    'huaweicloudsdkobs==3.1.133',
    'huaweicloudsdkocr==3.1.133',
    'huaweicloudsdkoctopus==3.1.133',
    'huaweicloudsdkoms==3.1.133',
    'huaweicloudsdkoptverse==3.1.133',
    'huaweicloudsdkorganizations==3.1.133',
    'huaweicloudsdkorgid==3.1.133',
    'huaweicloudsdkoroas==3.1.133',
    'huaweicloudsdkosm==3.1.133',
    'huaweicloudsdkpangulargemodels==3.1.133',
    'huaweicloudsdkprojectman==3.1.133',
    'huaweicloudsdkrabbitmq==3.1.133',
    'huaweicloudsdkram==3.1.133',
    'huaweicloudsdkrds==3.1.133',
    'huaweicloudsdkres==3.1.133',
    'huaweicloudsdkrgc==3.1.133',
    'huaweicloudsdkrms==3.1.133',
    'huaweicloudsdkrocketmq==3.1.133',
    'huaweicloudsdkroma==3.1.133',
    'huaweicloudsdksa==3.1.133',
    'huaweicloudsdkscm==3.1.133',
    'huaweicloudsdksdrs==3.1.133',
    'huaweicloudsdksecmaster==3.1.133',
    'huaweicloudsdkservicestage==3.1.133',
    'huaweicloudsdksfsturbo==3.1.133',
    'huaweicloudsdksis==3.1.133',
    'huaweicloudsdksmn==3.1.133',
    'huaweicloudsdksms==3.1.133',
    'huaweicloudsdksmsapi==3.1.133',
    'huaweicloudsdksts==3.1.133',
    'huaweicloudsdkswr==3.1.133',
    'huaweicloudsdktics==3.1.133',
    'huaweicloudsdktms==3.1.133',
    'huaweicloudsdkugo==3.1.133',
    'huaweicloudsdkvas==3.1.133',
    'huaweicloudsdkvcm==3.1.133',
    'huaweicloudsdkvod==3.1.133',
    'huaweicloudsdkvpc==3.1.133',
    'huaweicloudsdkvpcep==3.1.133',
    'huaweicloudsdkvpn==3.1.133',
    'huaweicloudsdkwaf==3.1.133',
    'huaweicloudsdkworkspace==3.1.133',
    'huaweicloudsdkworkspaceapp==3.1.133',
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
