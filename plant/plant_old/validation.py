from jsonschema import validate
import yaml
# import os

# clear = lambda: os.system('cls')
# clear()

with open('IEA37_case_study_adaptation2.yaml', 'r') as myfile:
  inputs = myfile.read()

with open('plant_energy_resource.yaml', 'r') as myfile:
  schema = myfile.read()

validate(
    yaml.load(inputs, Loader=yaml.FullLoader),
    yaml.load(schema, Loader=yaml.FullLoader)
)

wind_res = yaml.load(inputs, Loader=yaml.FullLoader)

print(wind_res)