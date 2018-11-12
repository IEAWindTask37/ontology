from jsonschema import validate
import yaml
import os

clear = lambda: os.system('cls')
clear()

with open('IEAturbine.yaml', 'r') as myfile:
  inputs = myfile.read()

with open('IEAturbine_schema.yaml', 'r') as myfile:
  schema = myfile.read()

validate(yaml.load(inputs), yaml.load(schema))
