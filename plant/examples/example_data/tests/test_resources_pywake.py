from plant.examples.utils import examples_data_path
from plant.examples.pywake_utils import yml2Site
import numpy.testing as npt
import numpy as np
import pytest


@pytest.mark.parametrize('yml', ['UniformResource.yaml', 'UniformResource_nc.yaml'])
def test_uniform_resource(yml):
    site = yml2Site(examples_data_path + "/plant_energy_resource/%s" % yml)
    wd = np.arange(0, 360, 22.5)
    npt.assert_array_equal(site.ds.P.sel(wd=wd), [0.025, 0.024, 0.029, 0.036, 0.063, 0.065, 0.1,
                                                  0.122, 0.063, 0.038, 0.039, 0.083, 0.213, 0.046, 0.032, 0.022])
    npt.assert_array_equal(site.ds.WS, [9.8])
    npt.assert_array_equal(site.ds.TI, [0.075])


@pytest.mark.parametrize('yml', ['UniformWeibullResource.yaml', 'UniformWeibullResource_nc.yaml'])
def test_uniform_weibull_resource(yml):
    site = yml2Site(examples_data_path + "/plant_energy_resource/%s" % yml)
    wd = np.arange(0, 360, 30)

    f = [3.597152, 3.948682, 5.167395, 7.000154, 8.364547, 6.43485,
         8.643194, 11.77051, 15.15757, 14.73792, 10.01205, 5.165975]
    A = [9.176929, 9.782334, 9.531809, 9.909545, 10.04269, 9.593921,
         9.584007, 10.51499, 11.39895, 11.68746, 11.63732, 10.08803]
    k = [2.392578, 2.447266, 2.412109, 2.591797, 2.755859, 2.595703,
         2.583984, 2.548828, 2.470703, 2.607422, 2.626953, 2.326172]

    npt.assert_array_equal(site.ds.Weibull_A.sel(wd=wd), A)
    npt.assert_array_equal(site.ds.Weibull_k.sel(wd=wd), k)
    npt.assert_array_equal(site.ds.Sector_frequency.sel(wd=wd), f)
    npt.assert_array_equal(site.ds.TI, [0.075])
