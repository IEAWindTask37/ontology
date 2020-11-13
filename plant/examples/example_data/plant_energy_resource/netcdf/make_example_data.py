import xarray as xr
import numpy as np
import yaml
from pathlib import Path
import matplotlib.pyplot as plt


def xr2yml(ds, filename=None):
    def fmt(v):
        if isinstance(v, dict):
            return {k: fmt(v) for k, v in v.items() if fmt(v) != {}}
        elif isinstance(v, tuple):
            return list(v)
        else:
            return v
    yml = yaml.dump(fmt(ds.to_dict()))
    if filename:
        Path(filename).write_text(yml)
    return yml


if __name__ == '__main__':

    # uniform site (https://github.com/byuflowlab/iea37-wflo-casestudies/blob/master/cs1-2/iea37-windrose.yaml)
    f = [.025, .024, .029, .036, .063, .065, .100, .122, .063, .038, .039, .083, .213, .046, .032, .022]
    WS = 9.8
    ds = xr.Dataset(
        data_vars={'WS': WS, 'P': ('wd', f)},
        coords={'wd': np.linspace(0, 360, len(f), endpoint=False)})
    ds.to_netcdf("UniformSite.nc")
    xr2yml(ds, "UniformSite.yml")

    # WeibullSite
    f = [3.597152, 3.948682, 5.167395, 7.000154, 8.364547, 6.43485,
         8.643194, 11.77051, 15.15757, 14.73792, 10.01205, 5.165975]
    A = [9.176929, 9.782334, 9.531809, 9.909545, 10.04269, 9.593921,
         9.584007, 10.51499, 11.39895, 11.68746, 11.63732, 10.08803]
    k = [2.392578, 2.447266, 2.412109, 2.591797, 2.755859, 2.595703,
         2.583984, 2.548828, 2.470703, 2.607422, 2.626953, 2.326172]
    ds = xr.Dataset(
        data_vars={'Sector_frequency': ('wd', f), 'Weibull_A': ('wd', A), 'Weibull_k': ('wd', k)},
        coords={'wd': np.linspace(0, 360, len(f), endpoint=False)})
    ds.to_netcdf("UniformWeibullSite.nc")
    xr2yml(ds, "UniformWeibullSite.yml")

    # NonGridded site. 16 WT with speedup = 1+.01*wt_index
    f = [.025, .024, .029, .036, .063, .065, .100, .122, .063, .038, .039, .083, .213, .046, .032, .022]
    wt_index = np.arange(16)
    ds = xr.Dataset(
        data_vars={'Speedup': ('i', 1 + .01 * wt_index), 'P': ('wd', f)},
        coords={'wd': np.linspace(0, 360, len(f), endpoint=False),
                'i': wt_index})
    if 0:
        ds.SpeedUp.plot()
        plt.show()
    ds.to_netcdf("NonGriddedSite.nc")
    xr2yml(ds, "NonGriddedSite.yml")

    # GriddedSite.
    f = [.025, .024, .029, .036, .063, .065, .100, .122, .063, .038, .039, .083, .213, .046, .032, .022]
    x = y = np.arange(-2000, 2500, 500)
    X, Y = np.meshgrid(x, y)

    ds = xr.Dataset(
        data_vars={'Speedup': (['x', 'y'], 1 + 0.1 * x / x.max() + 0.1 * np.cos(Y / y.max())), 'P': ('wd', f)},
        coords={'wd': np.linspace(0, 360, len(f), endpoint=False),
                'x': x,
                'y': y})
    ds.Speedup.plot(x='x')
    plt.show()
    ds.to_netcdf("GriddedSite.nc")
    xr2yml(ds, "GriddedSite.yml")
