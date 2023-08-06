# KnowEnG's Pipelines Library
This repository provides Python scripts to support Knowledge Engine for Genomics (KnowEnG) pipelines, an NIH BD2K Center of Excellence.

There are four modules that one can choose from:

| **Modules**                   | **Description**                             |
| ----------------------------- | ------------------------------------------- |
| toolbox.py                    | Contains basic computation functions for all pipelines |
| data_cleanup_toolbox.py       | Contains functions for data_cleanup_pipeline|
| distributed_computing_utils.py| Contains functions for parallel computing and distribute computing |
| redis_utilities.py            | Contains API to call redis database         |


* * * 
## How to use this library
* * * 

### 1. Install python3-pip in your local machine
```
apt-get install python3-pip
```

### 3. Install knpackage in your local machine
```
pip3 install knpackage
```
 
### 2. Import modules from knpackage in your Python script
```
import knpackage.<module_name>
```


