# Copyright 2018   Tim McNamara

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="detect_delimiter",
    version="0.1.1",
    description='Detects the delimiter used in CSV, TSV and other ad hoc file formats.',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://git.nzoss.org.nz/tim-mcnamara/detect-delimiter",
    author="Tim McNamara",
    author_email="paperless@timmcnamara.co.nz",
    py_modules=[
        "detect_delimiter",
    ],

    tests_require=[
        "pytest",
        "hypothesis"
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ]
)