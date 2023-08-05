# VACUMM data (vacumm-data)

[![Build Status](https://travis-ci.org/VACUMM/vacumm-data.svg?branch=master)](https://travis-ci.org/VACUMM/vacumm-data)

Data used by the [vacumm](http://wwwifremer.fr/vacumm) python library
and its tutorials and test scripts.


## Sources

On GitHub: https://github.com/VACUMM/vacumm-data


## Installation

```bash
$ python setup.py install # from sources
$ pip install vacumm-data
$ conda install vacumm-data
```

Files are typically installed in the `<prefix>share/vacumm` folder.

## Access to the data paths

The main directory can be accessed with the
`vacumm_data.get_vacumm_data_dir()` function:

```python

base_path = get_vacumm_data_dir()
```
A particular file path is accessible with the
`vacumm_data.get_vacumm_data_file()` function:

```python

ncfile = get_vacumm_data_file('samples/menor.nc')
```

## Data

### Samples (`samples`)

Theses files are used by the vacumm tutorials and test scripts.

### Shorelines (`shorelines`)

Shapefiles used by the `vacumm.bathy.shorelines` module.

#### Histolitt

See: https://www.data.gouv.fr/fr/datasets/shom-ign-trait-de-cote-histolitt-r

#### GSHHS

See: https://www.ngdc.noaa.gov/mgg/shorelines/gshhs.html

### Sea level (`sea_level`)

Data used by the `vacumm.bathy.tide` module.
