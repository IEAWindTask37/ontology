from plant.examples.utils import examples_data_path, load_yaml
from py_wake.examples.data.iea37._iea37 import IEA37_WindTurbines, IEA37Site
from plant.examples.pywake_utils import yml2Site, yml2WindTurbines
from py_wake.deficit_models.gaussian import IEA37SimpleBastankhahGaussian
import numpy as np
import numpy.testing as npt

from py_wake.examples.data.iea37.iea37_reader import read_iea37_windfarm


def test_IEA37_case_study1():
    plant_site = load_yaml(examples_data_path + 'plant_energy_site/IEA37_case_study_energy_site.yaml')
    x, y = [plant_site['layouts']['initial_layout']['coordinates'][xy] for xy in 'xy']
    wt = yml2WindTurbines(examples_data_path + "plant_energy_turbine/IEA37_3.35MW_turbine.yaml")
    site = yml2Site(examples_data_path + "/plant_energy_resource/IEA37_case_study_energy_resource.yaml")
    ref = np.array([9444.60012, 8497.90004, 11383.32869, 14173.40367,
                    20979.36776, 25590.86774, 39252.85757, 43197.65856,
                    23800.39229, 13539.36766, 15022.89800, 32644.44314,
                    71157.32322, 18092.10102, 12326.48041, 7838.58128])

    print(ref.sum())
    sim_res = IEA37SimpleBastankhahGaussian(site, wt)(x, y, wd=np.arange(0, 360, 22.5))
    aep = sim_res.aep(normalize_probabilities=True)
    print(aep.sum())
    npt.assert_array_almost_equal(aep.sum(['wt', 'ws']) * 1e3, ref, 5)
