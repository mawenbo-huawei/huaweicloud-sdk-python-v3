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
VERSION = "3.1.88"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.88',
    'huaweicloudsdkaad==3.1.88',
    'huaweicloudsdkantiddos==3.1.88',
    'huaweicloudsdkaom==3.1.88',
    'huaweicloudsdkaos==3.1.88',
    'huaweicloudsdkapig==3.1.88',
    'huaweicloudsdkapm==3.1.88',
    'huaweicloudsdkas==3.1.88',
    'huaweicloudsdkasm==3.1.88',
    'huaweicloudsdkbcs==3.1.88',
    'huaweicloudsdkbms==3.1.88',
    'huaweicloudsdkbss==3.1.88',
    'huaweicloudsdkbssintl==3.1.88',
    'huaweicloudsdkcae==3.1.88',
    'huaweicloudsdkcampusgo==3.1.88',
    'huaweicloudsdkcbh==3.1.88',
    'huaweicloudsdkcbr==3.1.88',
    'huaweicloudsdkcbs==3.1.88',
    'huaweicloudsdkcc==3.1.88',
    'huaweicloudsdkcce==3.1.88',
    'huaweicloudsdkccm==3.1.88',
    'huaweicloudsdkcdm==3.1.88',
    'huaweicloudsdkcdn==3.1.88',
    'huaweicloudsdkces==3.1.88',
    'huaweicloudsdkcfw==3.1.88',
    'huaweicloudsdkcgs==3.1.88',
    'huaweicloudsdkclassroom==3.1.88',
    'huaweicloudsdkcloudide==3.1.88',
    'huaweicloudsdkcloudpond==3.1.88',
    'huaweicloudsdkcloudrtc==3.1.88',
    'huaweicloudsdkcloudtable==3.1.88',
    'huaweicloudsdkcloudtest==3.1.88',
    'huaweicloudsdkcodeartsartifact==3.1.88',
    'huaweicloudsdkcodeartsbuild==3.1.88',
    'huaweicloudsdkcodeartscheck==3.1.88',
    'huaweicloudsdkcodeartsdeploy==3.1.88',
    'huaweicloudsdkcodeartsinspector==3.1.88',
    'huaweicloudsdkcodeartspipeline==3.1.88',
    'huaweicloudsdkcodecraft==3.1.88',
    'huaweicloudsdkcodehub==3.1.88',
    'huaweicloudsdkconfig==3.1.88',
    'huaweicloudsdkcph==3.1.88',
    'huaweicloudsdkcpts==3.1.88',
    'huaweicloudsdkcse==3.1.88',
    'huaweicloudsdkcsms==3.1.88',
    'huaweicloudsdkcss==3.1.88',
    'huaweicloudsdkcts==3.1.88',
    'huaweicloudsdkdas==3.1.88',
    'huaweicloudsdkdataartsstudio==3.1.88',
    'huaweicloudsdkdbss==3.1.88',
    'huaweicloudsdkdc==3.1.88',
    'huaweicloudsdkdcs==3.1.88',
    'huaweicloudsdkddm==3.1.88',
    'huaweicloudsdkdds==3.1.88',
    'huaweicloudsdkdeh==3.1.88',
    'huaweicloudsdkdevsecurity==3.1.88',
    'huaweicloudsdkdevstar==3.1.88',
    'huaweicloudsdkdgc==3.1.88',
    'huaweicloudsdkdis==3.1.88',
    'huaweicloudsdkdlf==3.1.88',
    'huaweicloudsdkdli==3.1.88',
    'huaweicloudsdkdns==3.1.88',
    'huaweicloudsdkdris==3.1.88',
    'huaweicloudsdkdrs==3.1.88',
    'huaweicloudsdkdsc==3.1.88',
    'huaweicloudsdkdwr==3.1.88',
    'huaweicloudsdkdws==3.1.88',
    'huaweicloudsdkec==3.1.88',
    'huaweicloudsdkecs==3.1.88',
    'huaweicloudsdkedgesec==3.1.88',
    'huaweicloudsdkeg==3.1.88',
    'huaweicloudsdkeihealth==3.1.88',
    'huaweicloudsdkeip==3.1.88',
    'huaweicloudsdkelb==3.1.88',
    'huaweicloudsdkeps==3.1.88',
    'huaweicloudsdker==3.1.88',
    'huaweicloudsdkevs==3.1.88',
    'huaweicloudsdkfrs==3.1.88',
    'huaweicloudsdkfunctiongraph==3.1.88',
    'huaweicloudsdkga==3.1.88',
    'huaweicloudsdkgaussdb==3.1.88',
    'huaweicloudsdkgaussdbfornosql==3.1.88',
    'huaweicloudsdkgaussdbforopengauss==3.1.88',
    'huaweicloudsdkgeip==3.1.88',
    'huaweicloudsdkges==3.1.88',
    'huaweicloudsdkgsl==3.1.88',
    'huaweicloudsdkhilens==3.1.88',
    'huaweicloudsdkhss==3.1.88',
    'huaweicloudsdkiam==3.1.88',
    'huaweicloudsdkiamaccessanalyzer==3.1.88',
    'huaweicloudsdkidentitycenter==3.1.88',
    'huaweicloudsdkidentitycenterstore==3.1.88',
    'huaweicloudsdkidme==3.1.88',
    'huaweicloudsdkidmeclassicapi==3.1.88',
    'huaweicloudsdkiec==3.1.88',
    'huaweicloudsdkief==3.1.88',
    'huaweicloudsdkimage==3.1.88',
    'huaweicloudsdkimagesearch==3.1.88',
    'huaweicloudsdkims==3.1.88',
    'huaweicloudsdkiotanalytics==3.1.88',
    'huaweicloudsdkiotda==3.1.88',
    'huaweicloudsdkiotedge==3.1.88',
    'huaweicloudsdkivs==3.1.88',
    'huaweicloudsdkkafka==3.1.88',
    'huaweicloudsdkkms==3.1.88',
    'huaweicloudsdkkoomessage==3.1.88',
    'huaweicloudsdkkps==3.1.88',
    'huaweicloudsdklakeformation==3.1.88',
    'huaweicloudsdklive==3.1.88',
    'huaweicloudsdklts==3.1.88',
    'huaweicloudsdkmapds==3.1.88',
    'huaweicloudsdkmas==3.1.88',
    'huaweicloudsdkmeeting==3.1.88',
    'huaweicloudsdkmetastudio==3.1.88',
    'huaweicloudsdkmoderation==3.1.88',
    'huaweicloudsdkmpc==3.1.88',
    'huaweicloudsdkmrs==3.1.88',
    'huaweicloudsdkmsgsms==3.1.88',
    'huaweicloudsdkmssi==3.1.88',
    'huaweicloudsdknat==3.1.88',
    'huaweicloudsdknlp==3.1.88',
    'huaweicloudsdkobs==3.1.88',
    'huaweicloudsdkocr==3.1.88',
    'huaweicloudsdkoctopus==3.1.88',
    'huaweicloudsdkoms==3.1.88',
    'huaweicloudsdkoptverse==3.1.88',
    'huaweicloudsdkorganizations==3.1.88',
    'huaweicloudsdkorgid==3.1.88',
    'huaweicloudsdkoroas==3.1.88',
    'huaweicloudsdkosm==3.1.88',
    'huaweicloudsdkpangulargemodels==3.1.88',
    'huaweicloudsdkprojectman==3.1.88',
    'huaweicloudsdkrabbitmq==3.1.88',
    'huaweicloudsdkram==3.1.88',
    'huaweicloudsdkrds==3.1.88',
    'huaweicloudsdkres==3.1.88',
    'huaweicloudsdkrgc==3.1.88',
    'huaweicloudsdkrms==3.1.88',
    'huaweicloudsdkrocketmq==3.1.88',
    'huaweicloudsdkroma==3.1.88',
    'huaweicloudsdksa==3.1.88',
    'huaweicloudsdkscm==3.1.88',
    'huaweicloudsdksdrs==3.1.88',
    'huaweicloudsdksecmaster==3.1.88',
    'huaweicloudsdkservicestage==3.1.88',
    'huaweicloudsdksfsturbo==3.1.88',
    'huaweicloudsdksis==3.1.88',
    'huaweicloudsdksmn==3.1.88',
    'huaweicloudsdksms==3.1.88',
    'huaweicloudsdkswr==3.1.88',
    'huaweicloudsdktics==3.1.88',
    'huaweicloudsdktms==3.1.88',
    'huaweicloudsdkugo==3.1.88',
    'huaweicloudsdkvas==3.1.88',
    'huaweicloudsdkvcm==3.1.88',
    'huaweicloudsdkvod==3.1.88',
    'huaweicloudsdkvpc==3.1.88',
    'huaweicloudsdkvpcep==3.1.88',
    'huaweicloudsdkvpn==3.1.88',
    'huaweicloudsdkwaf==3.1.88',
    'huaweicloudsdkworkspace==3.1.88',
    'huaweicloudsdkworkspaceapp==3.1.88',
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
