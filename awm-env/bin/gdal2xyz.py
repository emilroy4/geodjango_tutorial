#!/Users/a35389/Library/CloudStorage/OneDrive-TechnologicalUniversityDublin/TU856.4/web mapping/AWMProjects/awmproject/geodjango_tutorial/awm-env/bin/python3

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdal2xyz as a convenience to use as a script
from osgeo_utils.gdal2xyz import *  # noqa
from osgeo_utils.gdal2xyz import main

deprecation_warn("gdal2xyz")
sys.exit(main(sys.argv))
