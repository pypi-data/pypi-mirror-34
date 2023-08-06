# PrecisionMapper

[![Travis](https://img.shields.io/travis/tducret/precisionmapper-python.svg)](https://travis-ci.org/tducret/precisionmapper-python)
[![Coveralls github](https://img.shields.io/coveralls/github/tducret/precisionmapper-python.svg)](https://coveralls.io/github/tducret/precisionmapper-python)
[![PyPI](https://img.shields.io/pypi/v/precisionmapper.svg)](https://pypi.org/project/precisionmapper/)
![License](https://img.shields.io/github/license/tducret/precisionmapper-python.svg)

## Description

Python package to communicate with precisionmapper.com

# Requirements

- Python 3
- pip3

## Installation

```bash
pip3 install -U precisionmapper
```

## Package usage

```python
# -*- coding: utf-8 -*-
from precisionmapper import PrecisionMapper

pm = PrecisionMapper(login=_LOGIN, password=_PASSWORD)
pm.sign_in()
shared_surveys = pm.get_shared_surveys()

for survey in shared_surveys:
    print(survey)
```

Example output :

```bash
[High School Sample] (California, United States - 12/02/2017 23:52) : 103 images, 3.69 GB, sensor : RGB
[Neighborhood Construction Sample] (Virginia, United States - 10/02/2017 16:36) : 34 images, 1.56 GB, sensor : RGB
[Micasense RedEdge Sample] (N/A - 31/01/2017 21:24) : 505 images, 2.37 GB, sensor : Blue, Green, Red, NIR, Red edge
[Palm Tree Farm Sample] (Bahia, Brazil - 08/07/2016 17:30) : 175 images, 12.4 GB, sensor : RGB
[Solar Panel Farm Sample] (Georgia, United States - 27/05/2016 23:31) : 168 images, 3.12 GB, sensor : RGB
[Construction Site Sample] (Florida, United States - 03/02/2016 17:03) : 287 images, 6.52 GB, sensor : BGNIR
[Wheat Disease Sample] (Leicestershire, United Kingdom - 15/06/2015 12:45) : 121 images, 4.81 GB, sensor : RGB
[Wheat - Sample 1] (Leicestershire, United Kingdom - 15/06/2015 11:55) : 225 images, 10.5 GB, sensor : RGB
[Wheat - Sample 2] (Leicestershire, United Kingdom - 15/06/2015 11:04) : 242 images, 7.65 GB, sensor : BGNIR
[3D Sample] (City of Stoke-on-Trent, United Kingdom - 22/05/2015 13:20) : 477 images, 10.6 GB, sensor : RGB
```

## TODO
