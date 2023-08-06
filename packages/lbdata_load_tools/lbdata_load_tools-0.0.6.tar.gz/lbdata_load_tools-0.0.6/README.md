# lbdata_load_tools

Reusable utility functions for manipulating and loading data into Redshift

## Contents

`presets` contains presets to easily load data from a csv to a Redshift table

`helpers` contains a bunch of helper functions to prepare files, load them to s3, create staging tables, COPY to a Redshift table, ...


## Install

The package is available on Pypi : `pip install lbdata_load_tools`


# Development

## Unit tests

- Complete and rename .env.example into .env


```
cd lbdata_load_tools
source venv/bin/activate
python test.py
```


## Deploy new version to Pypi

- Update `version` number in `setup.py`
