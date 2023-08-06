Datalab Utils
==
Datalab Utils is a collection of small Python functions and classes which simplify usage of GCP datalab. 

# Usage
```
from datalab_utils.bigquery import read_bq_table, read_bq_query, execute_bq
```

# Dev Guide
*Release*
```
# After changed version in __about__.py
python setup.py sdist upload
```