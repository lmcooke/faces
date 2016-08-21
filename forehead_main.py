import maya.mel as mel
import maya.cmds as cmds
import forehead_controller as fc
import range_controller as rc
import random as random

# order: scale, translate, rotate
def main(arg):
	if (arg == 0):
		forehead_width = mel.eval("floatSliderGrp -query -value $forehead_width")
		forehead_height = mel.eval("floatSliderGrp -query -value $forehead_height")
		forehead_bulge = mel.eval("floatSliderGrp -query -value $forehead_bulge")
		forehead_raise = mel.eval("floatSliderGrp -query -value $forehead_raise")
		forehead_slant = mel.eval("floatSliderGrp -query -value $forehead_slant")
	else:
		forehead_width = random.uniform(0.0,1.0)
		forehead_height = random.uniform(0.0,1.0)
		forehead_bulge = random.uniform(0.0,1.0)
		forehead_raise = random.uniform(0.0,1.0)
		forehead_slant = random.uniform(0.0,1.0)
	
	scale_main(forehead_width, forehead_height)
	translate_main(forehead_raise, forehead_bulge)
	rotate_main(forehead_slant)

# given the input width and height, adjusts measurements so they fall
# within the correct range, and then scales forehead
def scale_main(width, height):
	if (height == 0):
		height = .001
	scale_ave_dif = (rc.forehead_scale_ave_max - rc.forehead_scale_ave_min)
	input_ave = (width + height) / 2
	scaled_input_ave = rc.forehead_scale_ave_min + (input_ave * scale_ave_dif)

	input_ratio = width/height
	if (input_ratio < rc.forehead_scale_ratio_min):
		input_ratio = rc.forehead_scale_ratio_min
	elif (input_ratio > rc.forehead_scale_ratio_max):
		input_ratio = rc.forehead_scale_ratio_max

	scaled_height = (2 * scaled_input_ave) / (input_ratio + 1)
	scaled_width = scaled_height * input_ratio
	fc.scale_forehead(scaled_width, scaled_height)

# given the input raise and bulge of the forehead, adjusts those 
# measurements so the fall within the correct range according to
# those given in forehead_controller
def translate_main(height, depth):
	height_dif = rc.forehead_trans_y_max - rc.forehead_trans_y_min
	scaled_height = (height * height_dif) + rc.forehead_trans_y_min

	depth_dif = rc.forehead_trans_z_max - rc.forehead_trans_z_min
	scaled_depth = (depth * depth_dif) * rc.forehead_trans_z_min
	fc.translate_forehead(scaled_height, scaled_depth)

# given the user inputted slant measurements, scales it according to
# forehead_controller specified max/min measurements
def rotate_main(slant):
	rot_dif = rc.forehead_rotate_max - rc.forehead_rotate_min
	scaled_rot = (slant * rot_dif) + rc.forehead_rotate_min
	fc.rotate_forehead(scaled_rot)


	




