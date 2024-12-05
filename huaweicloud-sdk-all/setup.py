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
VERSION = "3.1.125"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.125',
    'huaweicloudsdkaad==3.1.125',
    'huaweicloudsdkantiddos==3.1.125',
    'huaweicloudsdkaom==3.1.125',
    'huaweicloudsdkaos==3.1.125',
    'huaweicloudsdkapig==3.1.125',
    'huaweicloudsdkapm==3.1.125',
    'huaweicloudsdkas==3.1.125',
    'huaweicloudsdkasm==3.1.125',
    'huaweicloudsdkbcs==3.1.125',
    'huaweicloudsdkbms==3.1.125',
    'huaweicloudsdkbss==3.1.125',
    'huaweicloudsdkbssintl==3.1.125',
    'huaweicloudsdkcae==3.1.125',
    'huaweicloudsdkcampusgo==3.1.125',
    'huaweicloudsdkcbh==3.1.125',
    'huaweicloudsdkcbr==3.1.125',
    'huaweicloudsdkcbs==3.1.125',
    'huaweicloudsdkcc==3.1.125',
    'huaweicloudsdkcce==3.1.125',
    'huaweicloudsdkccm==3.1.125',
    'huaweicloudsdkcdm==3.1.125',
    'huaweicloudsdkcdn==3.1.125',
    'huaweicloudsdkces==3.1.125',
    'huaweicloudsdkcfw==3.1.125',
    'huaweicloudsdkcgs==3.1.125',
    'huaweicloudsdkclassroom==3.1.125',
    'huaweicloudsdkcloudide==3.1.125',
    'huaweicloudsdkcloudpond==3.1.125',
    'huaweicloudsdkcloudrtc==3.1.125',
    'huaweicloudsdkcloudtable==3.1.125',
    'huaweicloudsdkcloudtest==3.1.125',
    'huaweicloudsdkcoc==3.1.125',
    'huaweicloudsdkcodeartsartifact==3.1.125',
    'huaweicloudsdkcodeartsbuild==3.1.125',
    'huaweicloudsdkcodeartscheck==3.1.125',
    'huaweicloudsdkcodeartsdeploy==3.1.125',
    'huaweicloudsdkcodeartsgovernance==3.1.125',
    'huaweicloudsdkcodeartsinspector==3.1.125',
    'huaweicloudsdkcodeartspipeline==3.1.125',
    'huaweicloudsdkcodecraft==3.1.125',
    'huaweicloudsdkcodehub==3.1.125',
    'huaweicloudsdkconfig==3.1.125',
    'huaweicloudsdkcph==3.1.125',
    'huaweicloudsdkcpts==3.1.125',
    'huaweicloudsdkcse==3.1.125',
    'huaweicloudsdkcsms==3.1.125',
    'huaweicloudsdkcss==3.1.125',
    'huaweicloudsdkcts==3.1.125',
    'huaweicloudsdkdas==3.1.125',
    'huaweicloudsdkdataartsfabric==3.1.125',
    'huaweicloudsdkdataartsfabricep==3.1.125',
    'huaweicloudsdkdataartsstudio==3.1.125',
    'huaweicloudsdkdbss==3.1.125',
    'huaweicloudsdkdc==3.1.125',
    'huaweicloudsdkdcs==3.1.125',
    'huaweicloudsdkddm==3.1.125',
    'huaweicloudsdkdds==3.1.125',
    'huaweicloudsdkdeh==3.1.125',
    'huaweicloudsdkdevstar==3.1.125',
    'huaweicloudsdkdgc==3.1.125',
    'huaweicloudsdkdis==3.1.125',
    'huaweicloudsdkdlf==3.1.125',
    'huaweicloudsdkdli==3.1.125',
    'huaweicloudsdkdns==3.1.125',
    'huaweicloudsdkdris==3.1.125',
    'huaweicloudsdkdrs==3.1.125',
    'huaweicloudsdkdsc==3.1.125',
    'huaweicloudsdkdwr==3.1.125',
    'huaweicloudsdkdws==3.1.125',
    'huaweicloudsdkec==3.1.125',
    'huaweicloudsdkecs==3.1.125',
    'huaweicloudsdkedgesec==3.1.125',
    'huaweicloudsdkeg==3.1.125',
    'huaweicloudsdkeihealth==3.1.125',
    'huaweicloudsdkeip==3.1.125',
    'huaweicloudsdkelb==3.1.125',
    'huaweicloudsdkeps==3.1.125',
    'huaweicloudsdker==3.1.125',
    'huaweicloudsdkevs==3.1.125',
    'huaweicloudsdkfrs==3.1.125',
    'huaweicloudsdkfunctiongraph==3.1.125',
    'huaweicloudsdkga==3.1.125',
    'huaweicloudsdkgaussdb==3.1.125',
    'huaweicloudsdkgaussdbfornosql==3.1.125',
    'huaweicloudsdkgaussdbforopengauss==3.1.125',
    'huaweicloudsdkgeip==3.1.125',
    'huaweicloudsdkges==3.1.125',
    'huaweicloudsdkgsl==3.1.125',
    'huaweicloudsdkhilens==3.1.125',
    'huaweicloudsdkhss==3.1.125',
    'huaweicloudsdkiam==3.1.125',
    'huaweicloudsdkiamaccessanalyzer==3.1.125',
    'huaweicloudsdkidentitycenter==3.1.125',
    'huaweicloudsdkidentitycenterstore==3.1.125',
    'huaweicloudsdkidme==3.1.125',
    'huaweicloudsdkidmeclassicapi==3.1.125',
    'huaweicloudsdkiec==3.1.125',
    'huaweicloudsdkief==3.1.125',
    'huaweicloudsdkimage==3.1.125',
    'huaweicloudsdkimagesearch==3.1.125',
    'huaweicloudsdkims==3.1.125',
    'huaweicloudsdkiotanalytics==3.1.125',
    'huaweicloudsdkiotda==3.1.125',
    'huaweicloudsdkiotdm==3.1.125',
    'huaweicloudsdkiotedge==3.1.125',
    'huaweicloudsdkivs==3.1.125',
    'huaweicloudsdkkafka==3.1.125',
    'huaweicloudsdkkms==3.1.125',
    'huaweicloudsdkkoomessage==3.1.125',
    'huaweicloudsdkkps==3.1.125',
    'huaweicloudsdklakeformation==3.1.125',
    'huaweicloudsdklive==3.1.125',
    'huaweicloudsdklts==3.1.125',
    'huaweicloudsdkmapds==3.1.125',
    'huaweicloudsdkmas==3.1.125',
    'huaweicloudsdkmastudio==3.1.125',
    'huaweicloudsdkmeeting==3.1.125',
    'huaweicloudsdkmetastudio==3.1.125',
    'huaweicloudsdkmoderation==3.1.125',
    'huaweicloudsdkmpc==3.1.125',
    'huaweicloudsdkmrs==3.1.125',
    'huaweicloudsdkmsgsms==3.1.125',
    'huaweicloudsdkmssi==3.1.125',
    'huaweicloudsdknat==3.1.125',
    'huaweicloudsdknlp==3.1.125',
    'huaweicloudsdkobs==3.1.125',
    'huaweicloudsdkocr==3.1.125',
    'huaweicloudsdkoctopus==3.1.125',
    'huaweicloudsdkoms==3.1.125',
    'huaweicloudsdkoptverse==3.1.125',
    'huaweicloudsdkorganizations==3.1.125',
    'huaweicloudsdkorgid==3.1.125',
    'huaweicloudsdkoroas==3.1.125',
    'huaweicloudsdkosm==3.1.125',
    'huaweicloudsdkpangulargemodels==3.1.125',
    'huaweicloudsdkprojectman==3.1.125',
    'huaweicloudsdkrabbitmq==3.1.125',
    'huaweicloudsdkram==3.1.125',
    'huaweicloudsdkrds==3.1.125',
    'huaweicloudsdkres==3.1.125',
    'huaweicloudsdkrgc==3.1.125',
    'huaweicloudsdkrms==3.1.125',
    'huaweicloudsdkrocketmq==3.1.125',
    'huaweicloudsdkroma==3.1.125',
    'huaweicloudsdksa==3.1.125',
    'huaweicloudsdkscm==3.1.125',
    'huaweicloudsdksdrs==3.1.125',
    'huaweicloudsdksecmaster==3.1.125',
    'huaweicloudsdkservicestage==3.1.125',
    'huaweicloudsdksfsturbo==3.1.125',
    'huaweicloudsdksis==3.1.125',
    'huaweicloudsdksmn==3.1.125',
    'huaweicloudsdksms==3.1.125',
    'huaweicloudsdksts==3.1.125',
    'huaweicloudsdkswr==3.1.125',
    'huaweicloudsdktics==3.1.125',
    'huaweicloudsdktms==3.1.125',
    'huaweicloudsdkugo==3.1.125',
    'huaweicloudsdkvas==3.1.125',
    'huaweicloudsdkvcm==3.1.125',
    'huaweicloudsdkvod==3.1.125',
    'huaweicloudsdkvpc==3.1.125',
    'huaweicloudsdkvpcep==3.1.125',
    'huaweicloudsdkvpn==3.1.125',
    'huaweicloudsdkwaf==3.1.125',
    'huaweicloudsdkworkspace==3.1.125',
    'huaweicloudsdkworkspaceapp==3.1.125',
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
