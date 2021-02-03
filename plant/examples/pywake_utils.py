import yaml
import os
import numpy as np
import xarray as xr
from plant.examples.utils import Loader, examples_data_path, load_yaml, XrResourceLoader
from py_wake.wind_turbines import OneTypeWindTurbines, cube_power
from py_wake.site.xrsite import XRSite


def yml2Site(yml, interp_method='nearest'):
    resource = load_yaml(yml, XrResourceLoader)
    data = resource['wind_resource']
    ds = xr.Dataset({k: (v['dims'], v['data']) for k, v in data.items() if hasattr(v, 'keys') and 'dims' in v},
                    coords={k: v for k, v in data.items() if not hasattr(v, 'keys')})
    return xr2Site(ds)


def xr2Site(ds, interp_method='nearest'):
    ds = ds.rename(**{k: v for k, v in [('wind_direction', 'wd'),
                                        ('wind_speed', 'ws'),
                                        ('wind_turbine', 'i'),
                                        ('probability', 'P'),
                                        ('weibull_a', 'Weibull_A'),
                                        ('weibull_k', 'Weibull_k'),
                                        ('sector_probability', 'Sector_frequency'),
                                        ('turbulence_intensity', 'TI')] if k in ds})
    if 'ws' in ds:
        return XRSite(ds, default_ws=ds.ws, interp_method=interp_method)
    else:
        return XRSite(ds, interp_method=interp_method)


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
            return np.interp(ws,
                             power['Ct_curve']['Ct_wind_speeds'],
                             power['Ct_curve']['Ct_values'])

    return OneTypeWindTurbines(name=wt['name'], diameter=wt['rotor_diameter'], hub_height=wt['hub_height'],
                               power_func=power_func, ct_func=ct_func, power_unit='w')


if __name__ == '__main__':
    wt = yml2WindTurbines(examples_data_path + "plant_energy_turbine/IEA37_10MW_turbine.yaml")
    u = np.arange(30)
    import matplotlib.pyplot as plt
    plt.plot(u, wt.power(u))
    plt.show()
