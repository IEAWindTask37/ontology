import yaml
import os
from plant.examples.utils import validate_yaml, plant_schemas_path, Loader
from plant.examples.utils import examples_data_path
import xarray as xr


class PyWakeXRSiteLoader(Loader):

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))
        ext = os.path.splitext(filename)[1].lower()
        if ext in ['.yaml', '.yml']:
            with open(filename, 'r') as f:
                return yaml.load(f, PyWakeXRSiteLoader)
        elif ext in ['.nc']:

            def fmt(v):
                if isinstance(v, dict):
                    return {k: fmt(v) for k, v in v.items() if fmt(v) != {}}
                elif isinstance(v, tuple):
                    return list(v)
                else:
                    return v

            def ds2yml(ds):
                ds = ds.rename(**{k: v for k, v in [('wd', 'directions'),
                                                    ('P', 'probability'),
                                                    ('WS', 'wind_speed')] if k in ds})
                d = ds.to_dict()
                return fmt({**d['coords'], **d['data_vars']})
            return ds2yml(xr.open_dataset(filename))


PyWakeXRSiteLoader.add_constructor('!include', PyWakeXRSiteLoader.include)


if __name__ == '__main__':

    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/uniformSite_nc_data.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource.yaml')
    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/uniformSite_nc_file.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource.yaml',
                  loader=PyWakeXRSiteLoader)

    validate_yaml(data_file=examples_data_path + 'plant_energy_resource/IEA37_case_study_energy_resource.yaml',
                  schema_file=plant_schemas_path + 'plant_energy_resource.yaml')
