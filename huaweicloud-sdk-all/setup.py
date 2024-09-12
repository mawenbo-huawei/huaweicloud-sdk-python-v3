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
VERSION = "3.1.114"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.114',
    'huaweicloudsdkaad==3.1.114',
    'huaweicloudsdkantiddos==3.1.114',
    'huaweicloudsdkaom==3.1.114',
    'huaweicloudsdkaos==3.1.114',
    'huaweicloudsdkapig==3.1.114',
    'huaweicloudsdkapm==3.1.114',
    'huaweicloudsdkas==3.1.114',
    'huaweicloudsdkasm==3.1.114',
    'huaweicloudsdkbcs==3.1.114',
    'huaweicloudsdkbms==3.1.114',
    'huaweicloudsdkbss==3.1.114',
    'huaweicloudsdkbssintl==3.1.114',
    'huaweicloudsdkcae==3.1.114',
    'huaweicloudsdkcampusgo==3.1.114',
    'huaweicloudsdkcbh==3.1.114',
    'huaweicloudsdkcbr==3.1.114',
    'huaweicloudsdkcbs==3.1.114',
    'huaweicloudsdkcc==3.1.114',
    'huaweicloudsdkcce==3.1.114',
    'huaweicloudsdkccm==3.1.114',
    'huaweicloudsdkcdm==3.1.114',
    'huaweicloudsdkcdn==3.1.114',
    'huaweicloudsdkces==3.1.114',
    'huaweicloudsdkcfw==3.1.114',
    'huaweicloudsdkcgs==3.1.114',
    'huaweicloudsdkclassroom==3.1.114',
    'huaweicloudsdkcloudide==3.1.114',
    'huaweicloudsdkcloudpond==3.1.114',
    'huaweicloudsdkcloudrtc==3.1.114',
    'huaweicloudsdkcloudtable==3.1.114',
    'huaweicloudsdkcloudtest==3.1.114',
    'huaweicloudsdkcoc==3.1.114',
    'huaweicloudsdkcodeartsartifact==3.1.114',
    'huaweicloudsdkcodeartsbuild==3.1.114',
    'huaweicloudsdkcodeartscheck==3.1.114',
    'huaweicloudsdkcodeartsdeploy==3.1.114',
    'huaweicloudsdkcodeartsgovernance==3.1.114',
    'huaweicloudsdkcodeartsinspector==3.1.114',
    'huaweicloudsdkcodeartspipeline==3.1.114',
    'huaweicloudsdkcodecraft==3.1.114',
    'huaweicloudsdkcodehub==3.1.114',
    'huaweicloudsdkconfig==3.1.114',
    'huaweicloudsdkcph==3.1.114',
    'huaweicloudsdkcpts==3.1.114',
    'huaweicloudsdkcse==3.1.114',
    'huaweicloudsdkcsms==3.1.114',
    'huaweicloudsdkcss==3.1.114',
    'huaweicloudsdkcts==3.1.114',
    'huaweicloudsdkdas==3.1.114',
    'huaweicloudsdkdataartsstudio==3.1.114',
    'huaweicloudsdkdbss==3.1.114',
    'huaweicloudsdkdc==3.1.114',
    'huaweicloudsdkdcs==3.1.114',
    'huaweicloudsdkddm==3.1.114',
    'huaweicloudsdkdds==3.1.114',
    'huaweicloudsdkdeh==3.1.114',
    'huaweicloudsdkdevstar==3.1.114',
    'huaweicloudsdkdgc==3.1.114',
    'huaweicloudsdkdis==3.1.114',
    'huaweicloudsdkdlf==3.1.114',
    'huaweicloudsdkdli==3.1.114',
    'huaweicloudsdkdns==3.1.114',
    'huaweicloudsdkdris==3.1.114',
    'huaweicloudsdkdrs==3.1.114',
    'huaweicloudsdkdsc==3.1.114',
    'huaweicloudsdkdwr==3.1.114',
    'huaweicloudsdkdws==3.1.114',
    'huaweicloudsdkec==3.1.114',
    'huaweicloudsdkecs==3.1.114',
    'huaweicloudsdkedgesec==3.1.114',
    'huaweicloudsdkeg==3.1.114',
    'huaweicloudsdkeihealth==3.1.114',
    'huaweicloudsdkeip==3.1.114',
    'huaweicloudsdkelb==3.1.114',
    'huaweicloudsdkeps==3.1.114',
    'huaweicloudsdker==3.1.114',
    'huaweicloudsdkevs==3.1.114',
    'huaweicloudsdkfrs==3.1.114',
    'huaweicloudsdkfunctiongraph==3.1.114',
    'huaweicloudsdkga==3.1.114',
    'huaweicloudsdkgaussdb==3.1.114',
    'huaweicloudsdkgaussdbfornosql==3.1.114',
    'huaweicloudsdkgaussdbforopengauss==3.1.114',
    'huaweicloudsdkgeip==3.1.114',
    'huaweicloudsdkges==3.1.114',
    'huaweicloudsdkgsl==3.1.114',
    'huaweicloudsdkhilens==3.1.114',
    'huaweicloudsdkhss==3.1.114',
    'huaweicloudsdkiam==3.1.114',
    'huaweicloudsdkiamaccessanalyzer==3.1.114',
    'huaweicloudsdkidentitycenter==3.1.114',
    'huaweicloudsdkidentitycenterstore==3.1.114',
    'huaweicloudsdkidme==3.1.114',
    'huaweicloudsdkidmeclassicapi==3.1.114',
    'huaweicloudsdkiec==3.1.114',
    'huaweicloudsdkief==3.1.114',
    'huaweicloudsdkimage==3.1.114',
    'huaweicloudsdkimagesearch==3.1.114',
    'huaweicloudsdkims==3.1.114',
    'huaweicloudsdkiotanalytics==3.1.114',
    'huaweicloudsdkiotda==3.1.114',
    'huaweicloudsdkiotdm==3.1.114',
    'huaweicloudsdkiotedge==3.1.114',
    'huaweicloudsdkivs==3.1.114',
    'huaweicloudsdkkafka==3.1.114',
    'huaweicloudsdkkms==3.1.114',
    'huaweicloudsdkkoomessage==3.1.114',
    'huaweicloudsdkkps==3.1.114',
    'huaweicloudsdklakeformation==3.1.114',
    'huaweicloudsdklive==3.1.114',
    'huaweicloudsdklts==3.1.114',
    'huaweicloudsdkmapds==3.1.114',
    'huaweicloudsdkmas==3.1.114',
    'huaweicloudsdkmeeting==3.1.114',
    'huaweicloudsdkmetastudio==3.1.114',
    'huaweicloudsdkmoderation==3.1.114',
    'huaweicloudsdkmpc==3.1.114',
    'huaweicloudsdkmrs==3.1.114',
    'huaweicloudsdkmsgsms==3.1.114',
    'huaweicloudsdkmssi==3.1.114',
    'huaweicloudsdknat==3.1.114',
    'huaweicloudsdknlp==3.1.114',
    'huaweicloudsdkobs==3.1.114',
    'huaweicloudsdkocr==3.1.114',
    'huaweicloudsdkoctopus==3.1.114',
    'huaweicloudsdkoms==3.1.114',
    'huaweicloudsdkoptverse==3.1.114',
    'huaweicloudsdkorganizations==3.1.114',
    'huaweicloudsdkorgid==3.1.114',
    'huaweicloudsdkoroas==3.1.114',
    'huaweicloudsdkosm==3.1.114',
    'huaweicloudsdkpangulargemodels==3.1.114',
    'huaweicloudsdkprojectman==3.1.114',
    'huaweicloudsdkrabbitmq==3.1.114',
    'huaweicloudsdkram==3.1.114',
    'huaweicloudsdkrds==3.1.114',
    'huaweicloudsdkres==3.1.114',
    'huaweicloudsdkrgc==3.1.114',
    'huaweicloudsdkrms==3.1.114',
    'huaweicloudsdkrocketmq==3.1.114',
    'huaweicloudsdkroma==3.1.114',
    'huaweicloudsdksa==3.1.114',
    'huaweicloudsdkscm==3.1.114',
    'huaweicloudsdksdrs==3.1.114',
    'huaweicloudsdksecmaster==3.1.114',
    'huaweicloudsdkservicestage==3.1.114',
    'huaweicloudsdksfsturbo==3.1.114',
    'huaweicloudsdksis==3.1.114',
    'huaweicloudsdksmn==3.1.114',
    'huaweicloudsdksms==3.1.114',
    'huaweicloudsdksts==3.1.114',
    'huaweicloudsdkswr==3.1.114',
    'huaweicloudsdktics==3.1.114',
    'huaweicloudsdktms==3.1.114',
    'huaweicloudsdkugo==3.1.114',
    'huaweicloudsdkvas==3.1.114',
    'huaweicloudsdkvcm==3.1.114',
    'huaweicloudsdkvod==3.1.114',
    'huaweicloudsdkvpc==3.1.114',
    'huaweicloudsdkvpcep==3.1.114',
    'huaweicloudsdkvpn==3.1.114',
    'huaweicloudsdkwaf==3.1.114',
    'huaweicloudsdkworkspace==3.1.114',
    'huaweicloudsdkworkspaceapp==3.1.114',
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
