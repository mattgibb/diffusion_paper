#!/Users/matt/Code/imaging/ParaView/ParaView_release/bin/pvpython
from os.path import abspath, dirname
from paraview.simple import *
import sys

# import thesis contours module
contours_path = dirname(dirname(dirname(abspath(__file__)))) + "/thesis/figure_scripts/contours"
sys.path.append(contours_path)
import contours
import paths

# create contour in same directory as segmentation
def extract_contour(directory):
    segmentation_path = directory + "HiRes_segmentation.mha"
    contour_path      = directory + "HiRes_segmentation_contour.vtp"
    contours.extract_contour(segmentation_path, contour_path, rgb_data=True)

for i in (0,1,7,40):
    print "extracting noisy segmentation %d..." % i
    noisy_path = paths.noisy_path("200_alpha0.4rt", i)
    print noisy_path
    extract_contour(noisy_path)

extract_contour(paths.perfect_path("200_alpha0.4rt"))

banana_path = paths.dummy_root + "200_alpha0.4rt/HiResPairs/BananaTransforms/CenteredAffineTransform_1/"
print(banana_path)
extract_contour(banana_path)