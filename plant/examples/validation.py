import yaml
import os
from plant.examples.utils import validate_yaml, plant_schemas_path, XrResourceLoader
from plant.examples.utils import examples_data_path


if __name__ == '__main__':

    validate_yaml(data_file=examples_data_path + 'wind_energy_system/IEA37_case_study12_wind_energy_system.yaml',
                  schema_file=plant_schemas_path + 'wind_energy_system.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/IEA37_case_study_energy_resource.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_site/IEA37_case_study_energy_site.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_site.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_wind_farm/IEA37_case_study_wind_farm.yaml',
                  schema_file=plant_schemas_path + 'plant_wind_farm.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_turbine/IEA37_10MW_turbine.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_turbine.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_turbine/IEA37_15MW_turbine.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_turbine.yaml')

    # ===================================================================================================================
    # # validate energy resources
    # ===================================================================================================================

    # Uniform Resource
    validate_yaml(data_file=examples_data_path + "plant_energy_resource/UniformResource.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml")

    validate_yaml(data_file=examples_data_path + "plant_energy_resource/UniformResource_nc.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml",
                  loader=XrResourceLoader)

    # UniformWeibull Resource
    validate_yaml(data_file=examples_data_path + "plant_energy_resource/UniformWeibullResource.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml")

    validate_yaml(data_file=examples_data_path + "plant_energy_resource/UniformWeibullResource_nc.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml",
                  loader=XrResourceLoader)

    # WT distributed Resource
    validate_yaml(data_file=examples_data_path + "plant_energy_resource/WTResource.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml")

    validate_yaml(data_file=examples_data_path + "plant_energy_resource/WTResource_nc.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml",
                  loader=XrResourceLoader)

    # Gridded Resource
    validate_yaml(data_file=examples_data_path + "plant_energy_resource/GriddedResource.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml")

    validate_yaml(data_file=examples_data_path + "plant_energy_resource/GriddedResource_nc.yaml",
                  schema_file=plant_schemas_path + "plant_energy_resource.yaml",
                  loader=XrResourceLoader)
