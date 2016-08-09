import maya.mel as mel
import maya.cmds as cmds
import chin_controller as cc
import range_controller as rc
import random

# order: scale, bulge, translate_tip, translate, flare
def main2(arg):
	if (arg == 0):
		chin_scale_width = mel.eval("floatSliderGrp -query -value $chin_scale_width")
		chin_scale_height = mel.eval("floatSliderGrp -query -value $chin_scale_height")
		chin_scale_depth = mel.eval("floatSliderGrp -query -value $chin_scale_depth")

		chin_translate_height = mel.eval("floatSliderGrp -query -value $chin_translate_height")
		chin_translate_depth = mel.eval("floatSliderGrp -query -value $chin_translate_depth")

		chin_steepness = mel.eval("floatSliderGrp -query -value $chin_steepness")

		chin_point_height = mel.eval("floatSliderGrp -query -value $chin_point_height")
		chin_point_depth = mel.eval("floatSliderGrp -query -value $chin_point_depth")
	else:
		chin_scale_width = random.uniform(0.0,1.0)
		chin_scale_height = random.uniform(0.0,1.0)
		chin_scale_depth = random.uniform(0.0,1.0)

		chin_translate_height = random.uniform(0.0,1.0)
		chin_translate_depth = random.uniform(0.0,1.0)
		chin_steepness = random.uniform(0.0,1.0)

		chin_point_height = random.uniform(0.0,1.0)
		chin_point_depth = random.uniform(0.0,1.0)

	scale_chin_main(chin_scale_width, chin_scale_height, chin_scale_depth)
	trans_chin_main(chin_translate_height, chin_translate_depth)
	rotate_chin_main(chin_steepness)
	point_chin_main(chin_point_height, chin_point_depth)

def scale_chin_main(width, height, depth):
	width_dif = rc.scale_chin_x_max - rc.scale_chin_x_min
	scaled_width = (width_dif * width) + rc.scale_chin_x_min

	height_dif = rc.scale_chin_y_max - rc.scale_chin_y_min
	scaled_height = (height_dif * height) + rc.scale_chin_y_min

	depth_dif = rc.scale_chin_z_max - rc.scale_chin_z_min
	scaled_depth = (depth_dif * depth) + rc.scale_chin_z_min

	rc.scale_chin_z = scaled_depth
	cc.scale_chin(scaled_width, scaled_height, scaled_depth)

def trans_chin_main(height, depth):
	height_dif = rc.translate_chin_y_max - rc.translate_chin_y_min
	scaled_height = (height * height_dif) + rc.translate_chin_y_min

	depth_dif = rc.translate_chin_z_max - rc.translate_chin_z_min
	scaled_depth = (depth * depth_dif) + rc.translate_chin_z_min

	cc.translate_chin(scaled_height, scaled_depth)

def rotate_chin_main(rot):
	rot_dif = rc.chin_rot_max - rc.chin_rot_min
	scaled_rot = (rot_dif * rot) + rc.chin_rot_min

	cc.rotate_chin(scaled_rot)

def point_chin_main(height, depth):
	height_dif = rc.point_chin_y_max - rc.point_chin_y_min
	scaled_height = (height * height_dif) + rc.point_chin_y_min

	depth_dif = rc.get_point_chin_z_max() - rc.get_point_chin_z_min()
	scaled_depth = (depth * depth_dif) + rc.get_point_chin_z_min()

	cc.point_chin(scaled_height, scaled_depth)


