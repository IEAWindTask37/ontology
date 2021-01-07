import yaml
import os
import numpy as np
import xarray as xr
from plant.examples.utils import Loader, examples_data_path, load_yaml, XrResourceLoader
from py_wake.wind_turbines import OneTypeWindTurbines, cube_power
from py_wake.site.xrsite import XRSite


# class PyWakeXRSiteLoader(Loader):
#
#     def include(self, node):
#
#         filename = os.path.join(self._root, self.construct_scalar(node))
#         ext = os.path.splitext(filename)[1].lower()
#         if ext in ['.yaml', '.yml']:
#             with open(filename, 'r') as f:
#                 return yaml.load(f, PyWakeXRSiteLoader)
#         elif ext in ['.nc']:
#
#             def fmt(v):
#                 if isinstance(v, dict):
#                     return {k: fmt(v) for k, v in v.items() if fmt(v) != {}}
#                 elif isinstance(v, tuple):
#                     return list(v)
#                 else:
#                     return v
#
#             def ds2yml(ds):
#                 ds = ds.rename(**{k: v for k, v in [('wd', 'directions'),
#                                                     ('P', 'probability'),
#                                                     ('WS', 'wind_speed')] if k in ds})
#                 d = ds.to_dict()
#                 return fmt({**d['coords'], **d['data_vars']})
#             return ds2yml(xr.open_dataset(filename))
#
#
# PyWakeXRSiteLoader.add_constructor('!include', PyWakeXRSiteLoader.include)


def yml2Site(yml):
    resource = load_yaml(yml, XrResourceLoader)
    if 'general_resource' in resource['wind_resource']:
        print(resource['wind_resource']['general_resource'])
        data = resource['wind_resource']['general_resource']
        ds = xr.Dataset({k: (v['dims'], v['data']) for k, v in data.items()})
        ds = ds.rename(**{k: v for k, v in [('directions', 'wd'),
                                            ('probability', 'P'),
                                            ('weibull_a', 'Weibull_A'),
                                            ('weibull_k', 'Weibull_k'),
                                            ('sector_probability', 'Sector_frequency'),
                                            ('wind_speed', 'WS'),
                                            ('turbulence_intensity', 'TI')] if k in ds})
        return XRSite(ds)
    else:
        raise NotImplementedError()
    print(resource)


def yml2WindTurbines(yml):
    wt = load_yaml(yml)
    power = wt['power']
    if 'power_curve' in power:
        raise NotImplementedError()
    elif 'cp_curve' in power:
        raise NotImplementedError()
    else:
        power_func = cube_power(ws_cut_in=power['cutin_wind_speed'],
                                ws_cut_out=power['cutout_wind_speed'],
                                ws_rated=power['rated_wind_speed'],
                                power_rated=power['rated_power'])

        def ct_func(ws):
            return np.zeros_like(ws) + 8 / 9
    return OneTypeWindTurbines(name=wt['name'], diameter=wt['rotor_diameter'], hub_height=wt['hub_height'],
                               power_func=power_func, ct_func=ct_func, power_unit='w')


if __name__ == '__main__':
    wt = yml2WindTurbines(examples_data_path + "plant_energy_turbine/IEA37_10MW_turbine.yaml")
    u = np.arange(30)
    import matplotlib.pyplot as plt
    plt.plot(u, wt.power(u))
    plt.show()
