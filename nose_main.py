import maya.mel as mel
import maya.cmds as cmds
import nose_controller as nc
import range_controller as rc
import random

# order: scale, bulge, translate_tip, translate, flare
def main(arg):
	if (arg == 0):

		nose_height = mel.eval("floatSliderGrp -query -value $nose_height")
		nose_width = mel.eval("floatSliderGrp -query -value $nose_width")
		nose_depth = mel.eval("floatSliderGrp -query -value $nose_depth")
		nose_raise = mel.eval("floatSliderGrp -query -value $nose_raise")
		nose_protrusion = mel.eval("floatSliderGrp -query -value $nose_protrusion")
		nose_pointiness = mel.eval("floatSliderGrp -query -value $nose_pointiness")
		nose_upturn = mel.eval("floatSliderGrp -query -value $nose_upturn")
		nose_flare = mel.eval("floatSliderGrp -query -value $nose_flare")
	else:
		nose_height = random.uniform(0.0,1.0)
		nose_width = random.uniform(0.0,1.0)
		nose_depth = random.uniform(0.0,1.0)
		nose_raise = random.uniform(0.0,1.0)
		nose_protrusion = random.uniform(0.0,1.0)
		nose_pointiness = random.uniform(0.0,1.0)
		nose_upturn = random.uniform(0.0,1.0)
		nose_flare = random.uniform(0.0,1.0)

	scale_main(nose_width, nose_height, nose_depth)
	bulge_main(nose_raise, nose_protrusion)
	trans_nose_tip_main(nose_upturn, nose_protrusion)
	nose_flare_main(nose_flare)

# scales the user inputted measurements for scaling the nose
# according to the max and min measurements specified by nose_controller
def scale_main(width, height, depth):
	width_dif = rc.nose_scale_x_max - rc.nose_scale_x_min
	scaled_width = (width * width_dif) + rc.nose_scale_x_min

	height_dif = rc.nose_scale_y_max - rc.nose_scale_y_min
	scaled_height = (height * height_dif) + rc.nose_scale_y_min

	depth_dif = rc.nose_scale_z_max - rc.nose_scale_z_min
	scaled_depth = (depth * depth_dif) + rc.nose_scale_z_min

	rc.nose_scale_z = scaled_depth
	nc.scale_nose(scaled_width, scaled_height, scaled_depth)

# scales user inputted measurements for creating the 'bulge' of nose.
def bulge_main(height, depth):
	height_dif = rc.nose_bulge_y_max - rc.nose_bulge_y_min
	scaled_height = (height * height_dif) + rc.nose_bulge_y_min

	depth_dif = rc.nose_bulge_z_max - rc.nose_bulge_z_min
	scaled_depth = (depth * depth_dif) + rc.nose_bulge_z_min

	nc.bulge_nose(scaled_height, scaled_depth)

# scales user measurements to apply to translating the tip of the nose
def trans_nose_tip_main(height, depth):
	height_dif = rc.nose_trans_nose_tip_y_max - rc.nose_trans_nose_tip_y_min
	scaled_height = (height * height_dif) + rc.nose_trans_nose_tip_y_min

	depth_dif = rc.get_trans_nose_tip_z_max() - rc.get_trans_nose_tip_z_min()
	scaled_depth = (depth * depth_dif) + rc.get_trans_nose_tip_z_min()

	print("scaled depth : " + str(scaled_depth))
	nc.translate_nose_tip(scaled_height, scaled_depth)

def nose_flare_main(flare):
	flare_dif = rc.nose_flare_max - rc.nose_flare_min
	scaled_flare = (flare * flare_dif) + rc.nose_flare_min
	nc.nose_flare(scaled_flare)

