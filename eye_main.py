import maya.mel as mel
import maya.cmds as cmds
import eye_controller as ec
import range_controller as rc
import random

def main(arg):
	if (arg == 0):
		eye_width = mel.eval("floatSliderGrp -query -value $eye_width")
		eye_height = mel.eval("floatSliderGrp -query -value $eye_height")
		eye_closeness = mel.eval("floatSliderGrp -query -value $eye_closeness")
		eye_position_height = mel.eval("floatSliderGrp -query -value $eye_position_height")
		eye_position_width = mel.eval("floatSliderGrp -query -value $eye_position_width")
		eye_position_depth = mel.eval("floatSliderGrp -query -value $eye_position_depth")
		eye_rotation_y = mel.eval("floatSliderGrp -query -value $eye_rotation_y")
		eye_rotation_z = mel.eval("floatSliderGrp -query -value $eye_rotation_z")
		brow_furrow = mel.eval("floatSliderGrp -query -value $brow_furrow")
	else:
		eye_width = random.uniform(0.0,1.0)
		eye_height = random.uniform(0.0,1.0)
		eye_closeness = random.uniform(0.0,1.0)
		eye_position_height = random.uniform(0.0,1.0)
		eye_position_width = random.uniform(0.0,1.0)
		eye_position_depth = random.uniform(0.0,1.0)
		eye_rotation_y = random.uniform(0.0,1.0)
		eye_rotation_z = random.uniform(0.0,1.0)
		brow_furrow = random.uniform(0.0,1.0)

	scale_eyes_main(eye_width, eye_height)
	translate_eyes_main(eye_closeness, eye_position_height, eye_position_depth)
	rotate_eyes_main(eye_rotation_y, eye_rotation_z)

def scale_eyes_main(width, height):
	width_dif = rc.scale_eyes_x_max - rc.scale_eyes_x_min
	scaled_width = (width * width_dif) + rc.scale_eyes_x_min

	height_dif = rc.scale_eyes_y_max - rc.scale_eyes_y_min
	scaled_height = (height * height_dif) + rc.scale_eyes_y_min

	rc.scale_eyes_x = scaled_width
	ec.scale_eyes(scaled_width, scaled_height)

def translate_eyes_main(width, height, depth):
	width_dif = rc.trans_eyes_x_max - rc.trans_eyes_x_min
	scaled_width = (width * width_dif) + rc.trans_eyes_x_min

	height_dif = rc.trans_eyes_y_max - rc.trans_eyes_y_min
	scaled_height = (height * height_dif) + rc.trans_eyes_y_min

	depth_dif = rc.trans_eyes_z_max - rc.trans_eyes_z_min
	scaled_depth = (depth * depth_dif) + rc.trans_eyes_z_min

	ec.translate_eyes(scaled_width, scaled_height, scaled_depth)

def rotate_eyes_main(y_rot, z_rot):
	y_rot_dif = rc.rotate_eyes_y_max - rc.rotate_eyes_y_min
	scaled_y_rot = (y_rot * y_rot_dif) + rc.rotate_eyes_y_min

	z_rot_dif = rc.rotate_eyes_z_max - rc.rotate_eyes_z_min
	scaled_z_rot = (z_rot * z_rot_dif) + rc.rotate_eyes_z_min

	ec.rotate_eyes(scaled_y_rot, scaled_z_rot)

def furrow_brow_main(furrow):
	furrow_dif = rc.furrow_max - rc.furrow_min
	scaled_furrow = (furrow * furrow_dif) + rc.furrow_min

	ec.furrow_brow(scaled_furrow)






