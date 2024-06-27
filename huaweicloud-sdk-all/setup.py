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
VERSION = "3.1.103"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.103',
    'huaweicloudsdkaad==3.1.103',
    'huaweicloudsdkantiddos==3.1.103',
    'huaweicloudsdkaom==3.1.103',
    'huaweicloudsdkaos==3.1.103',
    'huaweicloudsdkapig==3.1.103',
    'huaweicloudsdkapm==3.1.103',
    'huaweicloudsdkas==3.1.103',
    'huaweicloudsdkasm==3.1.103',
    'huaweicloudsdkbcs==3.1.103',
    'huaweicloudsdkbms==3.1.103',
    'huaweicloudsdkbss==3.1.103',
    'huaweicloudsdkbssintl==3.1.103',
    'huaweicloudsdkcae==3.1.103',
    'huaweicloudsdkcampusgo==3.1.103',
    'huaweicloudsdkcbh==3.1.103',
    'huaweicloudsdkcbr==3.1.103',
    'huaweicloudsdkcbs==3.1.103',
    'huaweicloudsdkcc==3.1.103',
    'huaweicloudsdkcce==3.1.103',
    'huaweicloudsdkccm==3.1.103',
    'huaweicloudsdkcdm==3.1.103',
    'huaweicloudsdkcdn==3.1.103',
    'huaweicloudsdkces==3.1.103',
    'huaweicloudsdkcfw==3.1.103',
    'huaweicloudsdkcgs==3.1.103',
    'huaweicloudsdkclassroom==3.1.103',
    'huaweicloudsdkcloudide==3.1.103',
    'huaweicloudsdkcloudpond==3.1.103',
    'huaweicloudsdkcloudrtc==3.1.103',
    'huaweicloudsdkcloudtable==3.1.103',
    'huaweicloudsdkcloudtest==3.1.103',
    'huaweicloudsdkcodeartsartifact==3.1.103',
    'huaweicloudsdkcodeartsbuild==3.1.103',
    'huaweicloudsdkcodeartscheck==3.1.103',
    'huaweicloudsdkcodeartsdeploy==3.1.103',
    'huaweicloudsdkcodeartsinspector==3.1.103',
    'huaweicloudsdkcodeartspipeline==3.1.103',
    'huaweicloudsdkcodecraft==3.1.103',
    'huaweicloudsdkcodehub==3.1.103',
    'huaweicloudsdkconfig==3.1.103',
    'huaweicloudsdkcph==3.1.103',
    'huaweicloudsdkcpts==3.1.103',
    'huaweicloudsdkcse==3.1.103',
    'huaweicloudsdkcsms==3.1.103',
    'huaweicloudsdkcss==3.1.103',
    'huaweicloudsdkcts==3.1.103',
    'huaweicloudsdkdas==3.1.103',
    'huaweicloudsdkdataartsstudio==3.1.103',
    'huaweicloudsdkdbss==3.1.103',
    'huaweicloudsdkdc==3.1.103',
    'huaweicloudsdkdcs==3.1.103',
    'huaweicloudsdkddm==3.1.103',
    'huaweicloudsdkdds==3.1.103',
    'huaweicloudsdkdeh==3.1.103',
    'huaweicloudsdkdevsecurity==3.1.103',
    'huaweicloudsdkdevstar==3.1.103',
    'huaweicloudsdkdgc==3.1.103',
    'huaweicloudsdkdis==3.1.103',
    'huaweicloudsdkdlf==3.1.103',
    'huaweicloudsdkdli==3.1.103',
    'huaweicloudsdkdns==3.1.103',
    'huaweicloudsdkdris==3.1.103',
    'huaweicloudsdkdrs==3.1.103',
    'huaweicloudsdkdsc==3.1.103',
    'huaweicloudsdkdwr==3.1.103',
    'huaweicloudsdkdws==3.1.103',
    'huaweicloudsdkec==3.1.103',
    'huaweicloudsdkecs==3.1.103',
    'huaweicloudsdkedgesec==3.1.103',
    'huaweicloudsdkeg==3.1.103',
    'huaweicloudsdkeihealth==3.1.103',
    'huaweicloudsdkeip==3.1.103',
    'huaweicloudsdkelb==3.1.103',
    'huaweicloudsdkeps==3.1.103',
    'huaweicloudsdker==3.1.103',
    'huaweicloudsdkevs==3.1.103',
    'huaweicloudsdkfrs==3.1.103',
    'huaweicloudsdkfunctiongraph==3.1.103',
    'huaweicloudsdkga==3.1.103',
    'huaweicloudsdkgaussdb==3.1.103',
    'huaweicloudsdkgaussdbfornosql==3.1.103',
    'huaweicloudsdkgaussdbforopengauss==3.1.103',
    'huaweicloudsdkgeip==3.1.103',
    'huaweicloudsdkges==3.1.103',
    'huaweicloudsdkgsl==3.1.103',
    'huaweicloudsdkhilens==3.1.103',
    'huaweicloudsdkhss==3.1.103',
    'huaweicloudsdkiam==3.1.103',
    'huaweicloudsdkiamaccessanalyzer==3.1.103',
    'huaweicloudsdkidentitycenter==3.1.103',
    'huaweicloudsdkidentitycenterstore==3.1.103',
    'huaweicloudsdkidme==3.1.103',
    'huaweicloudsdkidmeclassicapi==3.1.103',
    'huaweicloudsdkiec==3.1.103',
    'huaweicloudsdkief==3.1.103',
    'huaweicloudsdkimage==3.1.103',
    'huaweicloudsdkimagesearch==3.1.103',
    'huaweicloudsdkims==3.1.103',
    'huaweicloudsdkiotanalytics==3.1.103',
    'huaweicloudsdkiotda==3.1.103',
    'huaweicloudsdkiotedge==3.1.103',
    'huaweicloudsdkivs==3.1.103',
    'huaweicloudsdkkafka==3.1.103',
    'huaweicloudsdkkms==3.1.103',
    'huaweicloudsdkkoomessage==3.1.103',
    'huaweicloudsdkkps==3.1.103',
    'huaweicloudsdklakeformation==3.1.103',
    'huaweicloudsdklive==3.1.103',
    'huaweicloudsdklts==3.1.103',
    'huaweicloudsdkmapds==3.1.103',
    'huaweicloudsdkmas==3.1.103',
    'huaweicloudsdkmeeting==3.1.103',
    'huaweicloudsdkmetastudio==3.1.103',
    'huaweicloudsdkmoderation==3.1.103',
    'huaweicloudsdkmpc==3.1.103',
    'huaweicloudsdkmrs==3.1.103',
    'huaweicloudsdkmsgsms==3.1.103',
    'huaweicloudsdkmssi==3.1.103',
    'huaweicloudsdknat==3.1.103',
    'huaweicloudsdknlp==3.1.103',
    'huaweicloudsdkobs==3.1.103',
    'huaweicloudsdkocr==3.1.103',
    'huaweicloudsdkoctopus==3.1.103',
    'huaweicloudsdkoms==3.1.103',
    'huaweicloudsdkoptverse==3.1.103',
    'huaweicloudsdkorganizations==3.1.103',
    'huaweicloudsdkorgid==3.1.103',
    'huaweicloudsdkoroas==3.1.103',
    'huaweicloudsdkosm==3.1.103',
    'huaweicloudsdkpangulargemodels==3.1.103',
    'huaweicloudsdkprojectman==3.1.103',
    'huaweicloudsdkrabbitmq==3.1.103',
    'huaweicloudsdkram==3.1.103',
    'huaweicloudsdkrds==3.1.103',
    'huaweicloudsdkres==3.1.103',
    'huaweicloudsdkrgc==3.1.103',
    'huaweicloudsdkrms==3.1.103',
    'huaweicloudsdkrocketmq==3.1.103',
    'huaweicloudsdkroma==3.1.103',
    'huaweicloudsdksa==3.1.103',
    'huaweicloudsdkscm==3.1.103',
    'huaweicloudsdksdrs==3.1.103',
    'huaweicloudsdksecmaster==3.1.103',
    'huaweicloudsdkservicestage==3.1.103',
    'huaweicloudsdksfsturbo==3.1.103',
    'huaweicloudsdksis==3.1.103',
    'huaweicloudsdksmn==3.1.103',
    'huaweicloudsdksms==3.1.103',
    'huaweicloudsdksts==3.1.103',
    'huaweicloudsdkswr==3.1.103',
    'huaweicloudsdktics==3.1.103',
    'huaweicloudsdktms==3.1.103',
    'huaweicloudsdkugo==3.1.103',
    'huaweicloudsdkvas==3.1.103',
    'huaweicloudsdkvcm==3.1.103',
    'huaweicloudsdkvod==3.1.103',
    'huaweicloudsdkvpc==3.1.103',
    'huaweicloudsdkvpcep==3.1.103',
    'huaweicloudsdkvpn==3.1.103',
    'huaweicloudsdkwaf==3.1.103',
    'huaweicloudsdkworkspace==3.1.103',
    'huaweicloudsdkworkspaceapp==3.1.103',
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
