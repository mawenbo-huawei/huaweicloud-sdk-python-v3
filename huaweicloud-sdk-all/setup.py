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
VERSION = "3.1.115"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.115',
    'huaweicloudsdkaad==3.1.115',
    'huaweicloudsdkantiddos==3.1.115',
    'huaweicloudsdkaom==3.1.115',
    'huaweicloudsdkaos==3.1.115',
    'huaweicloudsdkapig==3.1.115',
    'huaweicloudsdkapm==3.1.115',
    'huaweicloudsdkas==3.1.115',
    'huaweicloudsdkasm==3.1.115',
    'huaweicloudsdkbcs==3.1.115',
    'huaweicloudsdkbms==3.1.115',
    'huaweicloudsdkbss==3.1.115',
    'huaweicloudsdkbssintl==3.1.115',
    'huaweicloudsdkcae==3.1.115',
    'huaweicloudsdkcampusgo==3.1.115',
    'huaweicloudsdkcbh==3.1.115',
    'huaweicloudsdkcbr==3.1.115',
    'huaweicloudsdkcbs==3.1.115',
    'huaweicloudsdkcc==3.1.115',
    'huaweicloudsdkcce==3.1.115',
    'huaweicloudsdkccm==3.1.115',
    'huaweicloudsdkcdm==3.1.115',
    'huaweicloudsdkcdn==3.1.115',
    'huaweicloudsdkces==3.1.115',
    'huaweicloudsdkcfw==3.1.115',
    'huaweicloudsdkcgs==3.1.115',
    'huaweicloudsdkclassroom==3.1.115',
    'huaweicloudsdkcloudide==3.1.115',
    'huaweicloudsdkcloudpond==3.1.115',
    'huaweicloudsdkcloudrtc==3.1.115',
    'huaweicloudsdkcloudtable==3.1.115',
    'huaweicloudsdkcloudtest==3.1.115',
    'huaweicloudsdkcoc==3.1.115',
    'huaweicloudsdkcodeartsartifact==3.1.115',
    'huaweicloudsdkcodeartsbuild==3.1.115',
    'huaweicloudsdkcodeartscheck==3.1.115',
    'huaweicloudsdkcodeartsdeploy==3.1.115',
    'huaweicloudsdkcodeartsgovernance==3.1.115',
    'huaweicloudsdkcodeartsinspector==3.1.115',
    'huaweicloudsdkcodeartspipeline==3.1.115',
    'huaweicloudsdkcodecraft==3.1.115',
    'huaweicloudsdkcodehub==3.1.115',
    'huaweicloudsdkconfig==3.1.115',
    'huaweicloudsdkcph==3.1.115',
    'huaweicloudsdkcpts==3.1.115',
    'huaweicloudsdkcse==3.1.115',
    'huaweicloudsdkcsms==3.1.115',
    'huaweicloudsdkcss==3.1.115',
    'huaweicloudsdkcts==3.1.115',
    'huaweicloudsdkdas==3.1.115',
    'huaweicloudsdkdataartsstudio==3.1.115',
    'huaweicloudsdkdbss==3.1.115',
    'huaweicloudsdkdc==3.1.115',
    'huaweicloudsdkdcs==3.1.115',
    'huaweicloudsdkddm==3.1.115',
    'huaweicloudsdkdds==3.1.115',
    'huaweicloudsdkdeh==3.1.115',
    'huaweicloudsdkdevstar==3.1.115',
    'huaweicloudsdkdgc==3.1.115',
    'huaweicloudsdkdis==3.1.115',
    'huaweicloudsdkdlf==3.1.115',
    'huaweicloudsdkdli==3.1.115',
    'huaweicloudsdkdns==3.1.115',
    'huaweicloudsdkdris==3.1.115',
    'huaweicloudsdkdrs==3.1.115',
    'huaweicloudsdkdsc==3.1.115',
    'huaweicloudsdkdwr==3.1.115',
    'huaweicloudsdkdws==3.1.115',
    'huaweicloudsdkec==3.1.115',
    'huaweicloudsdkecs==3.1.115',
    'huaweicloudsdkedgesec==3.1.115',
    'huaweicloudsdkeg==3.1.115',
    'huaweicloudsdkeihealth==3.1.115',
    'huaweicloudsdkeip==3.1.115',
    'huaweicloudsdkelb==3.1.115',
    'huaweicloudsdkeps==3.1.115',
    'huaweicloudsdker==3.1.115',
    'huaweicloudsdkevs==3.1.115',
    'huaweicloudsdkfrs==3.1.115',
    'huaweicloudsdkfunctiongraph==3.1.115',
    'huaweicloudsdkga==3.1.115',
    'huaweicloudsdkgaussdb==3.1.115',
    'huaweicloudsdkgaussdbfornosql==3.1.115',
    'huaweicloudsdkgaussdbforopengauss==3.1.115',
    'huaweicloudsdkgeip==3.1.115',
    'huaweicloudsdkges==3.1.115',
    'huaweicloudsdkgsl==3.1.115',
    'huaweicloudsdkhilens==3.1.115',
    'huaweicloudsdkhss==3.1.115',
    'huaweicloudsdkiam==3.1.115',
    'huaweicloudsdkiamaccessanalyzer==3.1.115',
    'huaweicloudsdkidentitycenter==3.1.115',
    'huaweicloudsdkidentitycenterstore==3.1.115',
    'huaweicloudsdkidme==3.1.115',
    'huaweicloudsdkidmeclassicapi==3.1.115',
    'huaweicloudsdkiec==3.1.115',
    'huaweicloudsdkief==3.1.115',
    'huaweicloudsdkimage==3.1.115',
    'huaweicloudsdkimagesearch==3.1.115',
    'huaweicloudsdkims==3.1.115',
    'huaweicloudsdkiotanalytics==3.1.115',
    'huaweicloudsdkiotda==3.1.115',
    'huaweicloudsdkiotdm==3.1.115',
    'huaweicloudsdkiotedge==3.1.115',
    'huaweicloudsdkivs==3.1.115',
    'huaweicloudsdkkafka==3.1.115',
    'huaweicloudsdkkms==3.1.115',
    'huaweicloudsdkkoomessage==3.1.115',
    'huaweicloudsdkkps==3.1.115',
    'huaweicloudsdklakeformation==3.1.115',
    'huaweicloudsdklive==3.1.115',
    'huaweicloudsdklts==3.1.115',
    'huaweicloudsdkmapds==3.1.115',
    'huaweicloudsdkmas==3.1.115',
    'huaweicloudsdkmeeting==3.1.115',
    'huaweicloudsdkmetastudio==3.1.115',
    'huaweicloudsdkmoderation==3.1.115',
    'huaweicloudsdkmpc==3.1.115',
    'huaweicloudsdkmrs==3.1.115',
    'huaweicloudsdkmsgsms==3.1.115',
    'huaweicloudsdkmssi==3.1.115',
    'huaweicloudsdknat==3.1.115',
    'huaweicloudsdknlp==3.1.115',
    'huaweicloudsdkobs==3.1.115',
    'huaweicloudsdkocr==3.1.115',
    'huaweicloudsdkoctopus==3.1.115',
    'huaweicloudsdkoms==3.1.115',
    'huaweicloudsdkoptverse==3.1.115',
    'huaweicloudsdkorganizations==3.1.115',
    'huaweicloudsdkorgid==3.1.115',
    'huaweicloudsdkoroas==3.1.115',
    'huaweicloudsdkosm==3.1.115',
    'huaweicloudsdkpangulargemodels==3.1.115',
    'huaweicloudsdkprojectman==3.1.115',
    'huaweicloudsdkrabbitmq==3.1.115',
    'huaweicloudsdkram==3.1.115',
    'huaweicloudsdkrds==3.1.115',
    'huaweicloudsdkres==3.1.115',
    'huaweicloudsdkrgc==3.1.115',
    'huaweicloudsdkrms==3.1.115',
    'huaweicloudsdkrocketmq==3.1.115',
    'huaweicloudsdkroma==3.1.115',
    'huaweicloudsdksa==3.1.115',
    'huaweicloudsdkscm==3.1.115',
    'huaweicloudsdksdrs==3.1.115',
    'huaweicloudsdksecmaster==3.1.115',
    'huaweicloudsdkservicestage==3.1.115',
    'huaweicloudsdksfsturbo==3.1.115',
    'huaweicloudsdksis==3.1.115',
    'huaweicloudsdksmn==3.1.115',
    'huaweicloudsdksms==3.1.115',
    'huaweicloudsdksts==3.1.115',
    'huaweicloudsdkswr==3.1.115',
    'huaweicloudsdktics==3.1.115',
    'huaweicloudsdktms==3.1.115',
    'huaweicloudsdkugo==3.1.115',
    'huaweicloudsdkvas==3.1.115',
    'huaweicloudsdkvcm==3.1.115',
    'huaweicloudsdkvod==3.1.115',
    'huaweicloudsdkvpc==3.1.115',
    'huaweicloudsdkvpcep==3.1.115',
    'huaweicloudsdkvpn==3.1.115',
    'huaweicloudsdkwaf==3.1.115',
    'huaweicloudsdkworkspace==3.1.115',
    'huaweicloudsdkworkspaceapp==3.1.115',
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
