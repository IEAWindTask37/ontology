
import yaml
import os
from plant.examples.utils import validate_yaml, plant_schemas_path
from plant.examples.utils import examples_data_path


if __name__ == '__main__':

    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/IEA37_case_study_energy_resource.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource2.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_site/IEA37_case_study_energy_site.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_site.yaml')
