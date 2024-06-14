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
VERSION = "3.1.101"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.101',
    'huaweicloudsdkaad==3.1.101',
    'huaweicloudsdkantiddos==3.1.101',
    'huaweicloudsdkaom==3.1.101',
    'huaweicloudsdkaos==3.1.101',
    'huaweicloudsdkapig==3.1.101',
    'huaweicloudsdkapm==3.1.101',
    'huaweicloudsdkas==3.1.101',
    'huaweicloudsdkasm==3.1.101',
    'huaweicloudsdkbcs==3.1.101',
    'huaweicloudsdkbms==3.1.101',
    'huaweicloudsdkbss==3.1.101',
    'huaweicloudsdkbssintl==3.1.101',
    'huaweicloudsdkcae==3.1.101',
    'huaweicloudsdkcampusgo==3.1.101',
    'huaweicloudsdkcbh==3.1.101',
    'huaweicloudsdkcbr==3.1.101',
    'huaweicloudsdkcbs==3.1.101',
    'huaweicloudsdkcc==3.1.101',
    'huaweicloudsdkcce==3.1.101',
    'huaweicloudsdkccm==3.1.101',
    'huaweicloudsdkcdm==3.1.101',
    'huaweicloudsdkcdn==3.1.101',
    'huaweicloudsdkces==3.1.101',
    'huaweicloudsdkcfw==3.1.101',
    'huaweicloudsdkcgs==3.1.101',
    'huaweicloudsdkclassroom==3.1.101',
    'huaweicloudsdkcloudide==3.1.101',
    'huaweicloudsdkcloudpond==3.1.101',
    'huaweicloudsdkcloudrtc==3.1.101',
    'huaweicloudsdkcloudtable==3.1.101',
    'huaweicloudsdkcloudtest==3.1.101',
    'huaweicloudsdkcodeartsartifact==3.1.101',
    'huaweicloudsdkcodeartsbuild==3.1.101',
    'huaweicloudsdkcodeartscheck==3.1.101',
    'huaweicloudsdkcodeartsdeploy==3.1.101',
    'huaweicloudsdkcodeartsinspector==3.1.101',
    'huaweicloudsdkcodeartspipeline==3.1.101',
    'huaweicloudsdkcodecraft==3.1.101',
    'huaweicloudsdkcodehub==3.1.101',
    'huaweicloudsdkconfig==3.1.101',
    'huaweicloudsdkcph==3.1.101',
    'huaweicloudsdkcpts==3.1.101',
    'huaweicloudsdkcse==3.1.101',
    'huaweicloudsdkcsms==3.1.101',
    'huaweicloudsdkcss==3.1.101',
    'huaweicloudsdkcts==3.1.101',
    'huaweicloudsdkdas==3.1.101',
    'huaweicloudsdkdataartsstudio==3.1.101',
    'huaweicloudsdkdbss==3.1.101',
    'huaweicloudsdkdc==3.1.101',
    'huaweicloudsdkdcs==3.1.101',
    'huaweicloudsdkddm==3.1.101',
    'huaweicloudsdkdds==3.1.101',
    'huaweicloudsdkdeh==3.1.101',
    'huaweicloudsdkdevsecurity==3.1.101',
    'huaweicloudsdkdevstar==3.1.101',
    'huaweicloudsdkdgc==3.1.101',
    'huaweicloudsdkdis==3.1.101',
    'huaweicloudsdkdlf==3.1.101',
    'huaweicloudsdkdli==3.1.101',
    'huaweicloudsdkdns==3.1.101',
    'huaweicloudsdkdris==3.1.101',
    'huaweicloudsdkdrs==3.1.101',
    'huaweicloudsdkdsc==3.1.101',
    'huaweicloudsdkdwr==3.1.101',
    'huaweicloudsdkdws==3.1.101',
    'huaweicloudsdkec==3.1.101',
    'huaweicloudsdkecs==3.1.101',
    'huaweicloudsdkedgesec==3.1.101',
    'huaweicloudsdkeg==3.1.101',
    'huaweicloudsdkeihealth==3.1.101',
    'huaweicloudsdkeip==3.1.101',
    'huaweicloudsdkelb==3.1.101',
    'huaweicloudsdkeps==3.1.101',
    'huaweicloudsdker==3.1.101',
    'huaweicloudsdkevs==3.1.101',
    'huaweicloudsdkfrs==3.1.101',
    'huaweicloudsdkfunctiongraph==3.1.101',
    'huaweicloudsdkga==3.1.101',
    'huaweicloudsdkgaussdb==3.1.101',
    'huaweicloudsdkgaussdbfornosql==3.1.101',
    'huaweicloudsdkgaussdbforopengauss==3.1.101',
    'huaweicloudsdkgeip==3.1.101',
    'huaweicloudsdkges==3.1.101',
    'huaweicloudsdkgsl==3.1.101',
    'huaweicloudsdkhilens==3.1.101',
    'huaweicloudsdkhss==3.1.101',
    'huaweicloudsdkiam==3.1.101',
    'huaweicloudsdkiamaccessanalyzer==3.1.101',
    'huaweicloudsdkidentitycenter==3.1.101',
    'huaweicloudsdkidentitycenterstore==3.1.101',
    'huaweicloudsdkidme==3.1.101',
    'huaweicloudsdkidmeclassicapi==3.1.101',
    'huaweicloudsdkiec==3.1.101',
    'huaweicloudsdkief==3.1.101',
    'huaweicloudsdkimage==3.1.101',
    'huaweicloudsdkimagesearch==3.1.101',
    'huaweicloudsdkims==3.1.101',
    'huaweicloudsdkiotanalytics==3.1.101',
    'huaweicloudsdkiotda==3.1.101',
    'huaweicloudsdkiotedge==3.1.101',
    'huaweicloudsdkivs==3.1.101',
    'huaweicloudsdkkafka==3.1.101',
    'huaweicloudsdkkms==3.1.101',
    'huaweicloudsdkkoomessage==3.1.101',
    'huaweicloudsdkkps==3.1.101',
    'huaweicloudsdklakeformation==3.1.101',
    'huaweicloudsdklive==3.1.101',
    'huaweicloudsdklts==3.1.101',
    'huaweicloudsdkmapds==3.1.101',
    'huaweicloudsdkmas==3.1.101',
    'huaweicloudsdkmeeting==3.1.101',
    'huaweicloudsdkmetastudio==3.1.101',
    'huaweicloudsdkmoderation==3.1.101',
    'huaweicloudsdkmpc==3.1.101',
    'huaweicloudsdkmrs==3.1.101',
    'huaweicloudsdkmsgsms==3.1.101',
    'huaweicloudsdkmssi==3.1.101',
    'huaweicloudsdknat==3.1.101',
    'huaweicloudsdknlp==3.1.101',
    'huaweicloudsdkobs==3.1.101',
    'huaweicloudsdkocr==3.1.101',
    'huaweicloudsdkoctopus==3.1.101',
    'huaweicloudsdkoms==3.1.101',
    'huaweicloudsdkoptverse==3.1.101',
    'huaweicloudsdkorganizations==3.1.101',
    'huaweicloudsdkorgid==3.1.101',
    'huaweicloudsdkoroas==3.1.101',
    'huaweicloudsdkosm==3.1.101',
    'huaweicloudsdkpangulargemodels==3.1.101',
    'huaweicloudsdkprojectman==3.1.101',
    'huaweicloudsdkrabbitmq==3.1.101',
    'huaweicloudsdkram==3.1.101',
    'huaweicloudsdkrds==3.1.101',
    'huaweicloudsdkres==3.1.101',
    'huaweicloudsdkrgc==3.1.101',
    'huaweicloudsdkrms==3.1.101',
    'huaweicloudsdkrocketmq==3.1.101',
    'huaweicloudsdkroma==3.1.101',
    'huaweicloudsdksa==3.1.101',
    'huaweicloudsdkscm==3.1.101',
    'huaweicloudsdksdrs==3.1.101',
    'huaweicloudsdksecmaster==3.1.101',
    'huaweicloudsdkservicestage==3.1.101',
    'huaweicloudsdksfsturbo==3.1.101',
    'huaweicloudsdksis==3.1.101',
    'huaweicloudsdksmn==3.1.101',
    'huaweicloudsdksms==3.1.101',
    'huaweicloudsdksts==3.1.101',
    'huaweicloudsdkswr==3.1.101',
    'huaweicloudsdktics==3.1.101',
    'huaweicloudsdktms==3.1.101',
    'huaweicloudsdkugo==3.1.101',
    'huaweicloudsdkvas==3.1.101',
    'huaweicloudsdkvcm==3.1.101',
    'huaweicloudsdkvod==3.1.101',
    'huaweicloudsdkvpc==3.1.101',
    'huaweicloudsdkvpcep==3.1.101',
    'huaweicloudsdkvpn==3.1.101',
    'huaweicloudsdkwaf==3.1.101',
    'huaweicloudsdkworkspace==3.1.101',
    'huaweicloudsdkworkspaceapp==3.1.101',
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
