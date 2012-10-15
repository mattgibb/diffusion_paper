#!/Users/matt/Code/imaging/ParaView/ParaView_release/bin/pvpython

from os.path import abspath, dirname
import sys
from paraview.simple import *

# import thesis modules
contours_path = dirname(dirname(dirname(abspath(__file__)))) + "/thesis/figure_scripts/contours"
sys.path.append(contours_path)
from paths import *
from state import *

figures_dir = dirname(dirname(abspath(__file__))) + "/2_methods/Figs/"

paraview.simple._DisableFirstRenderCameraReset()

view = create_render_view()
view.ViewSize = [680, 2000] #[width, height]

experiment = "200_alpha0.4rt"
# for iteration in (0,1,7,40):
#     print "iteration: " + str(iteration)
# 
#     # load contours
#     noisy_contour   = XMLPolyDataReader( guiName="noisy_contour",   PointArrayStatus=['MetaImage', 'Normals'], CellArrayStatus=[], FileName=[noisy_path(experiment, iteration) + 'HiRes_segmentation_contour.vtp'] )
#     perfect_contour = XMLPolyDataReader( guiName="perfect_contour", PointArrayStatus=['MetaImage', 'Normals'], CellArrayStatus=[], FileName=[perfect_path(experiment)  + 'HiRes_segmentation_contour.vtp'] )
# 
#     # set display properties
#     noisy_dp   = set_display_properties(noisy_contour)
#     perfect_dp = set_display_properties(perfect_contour)
#     noisy_dp.ScaleFactor = perfect_dp.ScaleFactor = 3980.0
#     noisy_dp.DiffuseColor   = [1.0, 0.3568627450980392, 0.0]
#     perfect_dp.DiffuseColor = [0.0, 1.0, 0.19215686274509805]
#     noisy_dp.Opacity   = 1.0
#     perfect_dp.Opacity = 1.0
# 
#     Show(noisy_contour)
#     Show(perfect_contour)
# 
#     Render()
# 
#     # save figures
#     WriteImage( figures_dir + "whole_surface_%d.png" % iteration )
# 
#     # clean up
#     Delete(noisy_contour)
#     Delete(perfect_contour)
# 
# banana contour
# load contours
banana_path = dummy_root + "200_alpha0.4rt/HiResPairs/BananaTransforms/CenteredAffineTransform_1/"
banana_contour = XMLPolyDataReader( guiName="noisy_contour",   PointArrayStatus=['MetaImage', 'Normals'], CellArrayStatus=[], FileName=[banana_path + 'HiRes_segmentation_contour.vtp'] )

# set display properties
banana_dp   = set_display_properties(banana_contour)
banana_dp.ScaleFactor = 3980.0
banana_dp.DiffuseColor = [0.0, 1.0, 0.19215686274509805]
banana_dp.Opacity   = 1.0

Show(banana_contour)

Render()

# save figures
WriteImage( figures_dir + "whole_surface_banana.png")

# clean up
Delete(banana_contour)

