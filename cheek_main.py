import maya.mel as mel
import maya.cmds as cmds
import cheek_controller as cc
import range_controller as rc
import random

# order: scale ...... tbd
def main(arg):
	if (arg == 0):
		cheek_size = mel.eval("floatSliderGrp -query -value $cheek_size")
		cheek_raise = mel.eval("floatSliderGrp -query -value $cheek_raise")
		cheek_protrusion = mel.eval("floatSliderGrp -query -value $cheek_protrusion")
		cheek_steepness = mel.eval("floatSliderGrp -query -value $cheek_steepness")
	else:
		cheek_size = random.uniform(0.0,1.0)
		cheek_raise = random.uniform(0.0,1.0)
		cheek_protrusion = random.uniform(0.0,1.0)
		cheek_steepness = random.uniform(0.0,1.0)

	scale_cheeks_main(cheek_size)
	trans_cheeks_main(cheek_raise, cheek_protrusion)
	rotate_cheeks_main(cheek_steepness)

# takes the user input scale measurement and translates it according to
# max/min range as determined by cheek_controller
def scale_cheeks_main(size):
	size_dif = rc.scale_cheeks_max - rc.scale_cheeks_min
	scaled_size = (size * size_dif) + rc.scale_cheeks_min

	rc.scale_cheeks = scaled_size
	cc.scale_cheeks(scaled_size)

def trans_cheeks_main(height, depth):
	height_dif = rc.trans_outer_cheeks_y_max - rc.trans_outer_cheeks_y_min
	scaled_height = (height * height_dif) + rc.trans_outer_cheeks_y_min

	depth_dif = rc.get_trans_outer_cheeks_z_max() - rc.trans_outer_cheeks_z_min
	scaled_depth = (depth * depth_dif) + rc.trans_outer_cheeks_z_min

	rc.trans_outer_cheeks_y = scaled_height
	cc.translate_outer_cheeks(scaled_height, scaled_depth)

def rotate_cheeks_main(rot):
	rot_dif = rc.get_cheeks_rot_max() - rc.get_cheeks_rot_min()
	scaled_rot = (rot * rot_dif) + rc.get_cheeks_rot_min()

	cc.rotate_upper_cheeks(scaled_rot)
