import os
import xarray as xr
from py_wake.site.xrsite import XRSite
import matplotlib.pyplot as plt
import yaml
import numpy as np
from make_example_data import xr2yml

xr2yml


def yml2xr(file):
    pass

example_data_path ='../'
if __name__ == '__main__':

    def load(f):
        ds = xr.open_dataset(example_data_path + f + ".nc",engine='netcdf4')
        yml_site = XRSite(ds)
        with open(example_data_path + f + '.yml') as fid:
            xr_site = XRSite(xr.Dataset.from_dict(yaml.safe_load(fid)))
        assert yml_site.ds.equals(xr_site.ds)
        return yml_site

    # UniformSite
    site = load('UniformResource')
    plt.figure()
    site.plot_wd_distribution(ws_bins=4)
    plt.title('UniformSite')

    # UniformWeibullSite
    f = 'UniformWeibullSite'
    site = load(f)
    plt.figure()
    site.plot_wd_distribution(ws_bins=4)
    plt.title(f)
    plt.figure()
    site.plot_ws_distribution()
    plt.title(f)

    # NonGriddedSite
    f = 'NonGriddedSite'
    site = load(f)
    x = y = np.arange(16)  # dummy positions
    lw = site.local_wind(x, y, wd=0, ws=10)
    plt.figure()
    plt.title(f)
    lw.WS.plot()

    # GriddedSite
    f = 'GriddedSite'
    site = load(f)
    x = y = np.arange(-2000, 2500, 500)
    X, Y = np.meshgrid(x, y)
    lw = site.local_wind(X.flatten(), Y.flatten(), wd=0, ws=10)
    plt.figure()
    plt.title(f)
    plt.contourf(X, Y, np.reshape(lw.WS, X.shape))

    plt.show()
