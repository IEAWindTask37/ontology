import yaml
import os
from plant.examples.utils import plant_schemas_path, examples_data_path
from plant.examples.utils.yml_utils import validate_yaml, XrResourceLoader


if __name__ == '__main__':

    # ===================================================================================================================
    # # validate IEA case studies 1 and 2
    # ===================================================================================================================

    validate_yaml(data_file=examples_data_path + 'wind_energy_system/IEA37_case_study_1_2_wind_energy_system.yaml',
                  schema_file=plant_schemas_path + 'wind_energy_system.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/IEA37_case_study_1_2_energy_resource.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_site/IEA37_case_study_1_2_energy_site.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_site.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_wind_farm/IEA37_case_study_1_2_wind_farm.yaml',
                  schema_file=plant_schemas_path + 'plant_wind_farm.yaml')
   
    # ===================================================================================================================
    # # validate IEA case study 3
    # ===================================================================================================================

    validate_yaml(data_file=examples_data_path + 'wind_energy_system/IEA37_case_study_3_wind_energy_system.yaml',
                  schema_file=plant_schemas_path + 'wind_energy_system.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/IEA37_case_study_3_energy_resource.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_site/IEA37_case_study_3_energy_site.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_site.yaml')
    
    validate_yaml(data_file=examples_data_path + 'plant_wind_farm/IEA37_case_study_3_wind_farm.yaml',
                  schema_file=plant_schemas_path + 'plant_wind_farm.yaml')

    # ===================================================================================================================
    # # validate IEA case study 4
    # ===================================================================================================================

    validate_yaml(data_file=examples_data_path + 'wind_energy_system/IEA37_case_study_4_wind_energy_system.yaml',
                  schema_file=plant_schemas_path + 'wind_energy_system.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/IEA37_case_study_4_energy_resource.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_energy_site/IEA37_case_study_4_energy_site.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_site.yaml')

    validate_yaml(data_file=examples_data_path + 'plant_wind_farm/IEA37_case_study_4_wind_farm.yaml',
                  schema_file=plant_schemas_path + 'plant_wind_farm.yaml')

    # ===================================================================================================================
    # # validate IEA turbines
    # ===================================================================================================================

    validate_yaml(data_file=examples_data_path + 'plant_energy_turbine/IEA37_3.35MW_turbine.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_turbine.yaml')

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
