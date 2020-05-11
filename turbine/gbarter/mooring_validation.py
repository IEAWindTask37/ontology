"""
Script to validate the example `mooring.yaml` file against the
`mooring_schema.yaml` file.
"""

from jsonschema import validate
import yaml
import os
import sys


with open('mooring.yaml', 'r') as myfile:
  inputs = myfile.read()

with open('mooring_schema.yaml', 'r') as myfile:
  schema = myfile.read()

try:
    validate(yaml.safe_load(inputs), yaml.safe_load(schema))
    print("Validated correctly!")
except:
    print("Validation failed:", sys.exc_info()[0])
    raise
