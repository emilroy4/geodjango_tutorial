#!/Users/a35389/Library/CloudStorage/OneDrive-TechnologicalUniversityDublin/TU856.4/web mapping/AWMProjects/awmproject/geodjango_tutorial/awm-env/bin/python3

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.ogrmerge as a convenience to use as a script
from osgeo_utils.ogrmerge import *  # noqa
from osgeo_utils.ogrmerge import main

deprecation_warn("ogrmerge")
sys.exit(main(sys.argv))
