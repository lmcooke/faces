import maya.mel as mel
import maya.cmds as cmds
import mouth_controller as mc
import range_controller as rc
import random

# order: scale ...... tbd
def main(arg):

	if (arg == 0):
		mouth_scale_height = mel.eval("floatSliderGrp -query -value $mouth_scale_height")
		mouth_scale_width = mel.eval("floatSliderGrp -query -value $mouth_scale_width")

		mouth_translate_height = mel.eval("floatSliderGrp -query -value $mouth_translate_height")
		mouth_translate_depth = mel.eval("floatSliderGrp -query -value $mouth_translate_depth")

		mouth_orientation = mel.eval("floatSliderGrp -query -value $mouth_orientation")
		lip_size = mel.eval("floatSliderGrp -query -value $lip_size")

		lip_upward_arch = mel.eval("floatSliderGrp -query -value $lip_upward_arch")
		lip_inward_arch = mel.eval("floatSliderGrp -query -value $lip_inward_arch")

		upper_lip_width = mel.eval("floatSliderGrp -query -value $upper_lip_width")
		upper_lip_depth = mel.eval("floatSliderGrp -query -value $upper_lip_depth")

		upper_lip_height = mel.eval("floatSliderGrp -query -value $upper_lip_height")
		upper_lip_protrusion = mel.eval("floatSliderGrp -query -value $upper_lip_protrusion")
	else:
		mouth_scale_height = random.uniform(0.0,1.0)
		mouth_scale_width = random.uniform(0.0,1.0)

		mouth_translate_height = random.uniform(0.0,1.0)
		mouth_translate_depth = random.uniform(0.0,1.0)

		mouth_orientation = random.uniform(0.0,1.0)
		lip_size = random.uniform(0.0,1.0)

		lip_upward_arch = random.uniform(0.0,1.0)
		lip_inward_arch = random.uniform(0.0,1.0)

		upper_lip_width = random.uniform(0.0,1.0)
		upper_lip_depth = random.uniform(0.0,1.0)

		upper_lip_height = random.uniform(0.0,1.0)
		upper_lip_protrusion = random.uniform(0.0,1.0)

	scale_mouth_main(mouth_scale_width, mouth_scale_height)

	translate_mouth_main(mouth_translate_height, mouth_translate_depth)

	rotate_mouth_main(mouth_orientation)

	scale_lips_main(lip_size)

	arch_lip_main(lip_upward_arch, lip_inward_arch)

	scale_top_lip_main(upper_lip_width, upper_lip_depth)

	trans_top_lip_main(upper_lip_height, upper_lip_protrusion)

def scale_mouth_main(width, height):
	width_dif = rc.scale_mouth_x_max - rc.scale_mouth_x_min
	scaled_width = (width * width_dif) + rc.scale_mouth_x_min

	height_dif = rc.scale_mouth_y_max - rc.scale_mouth_y_min
	scaled_height = (height * height_dif) + rc.scale_mouth_y_min


	rc.scale_mouth_x = scaled_width
	rc.scale_mouth_y = scaled_height
	mc.scale_mouth(scaled_width, scaled_height)

def translate_mouth_main(height, depth):
	height_dif = rc.trans_mouth_y_max - rc.trans_mouth_y_min
	scaled_height = (height * height_dif) + rc.trans_mouth_y_min

	depth_dif = rc.trans_mouth_z_max - rc.trans_mouth_z_min
	scaled_depth = (depth * depth_dif) + rc.trans_mouth_z_min

	mc.translate_mouth(scaled_height, scaled_depth)

def rotate_mouth_main(rot):
	rot_dif = rc.mouth_rot_max - rc.mouth_rot_min
	scaled_rot = (rot * rot_dif) + rc.mouth_rot_min

	mc.rotate_mouth(scaled_rot)

def scale_lips_main(scale):
	scale_dif = rc.get_scale_lips_max() - rc.get_scale_lips_min()
	scaled_scale = (scale * scale_dif) + rc.get_scale_lips_min()

	mc.scale_lips(scaled_scale)

def arch_lip_main(height, depth):
	height_dif = rc.arch_lip_y_max - rc.arch_lip_y_min
	scaled_height = (height * height_dif) + rc.arch_lip_y_min

	depth_dif = rc.arch_lip_z_max - rc.arch_lip_z_min
	scaled_depth = (depth * depth_dif) + rc.arch_lip_z_min

	mc.arch_lip(scaled_height, scaled_depth)

def scale_top_lip_main(width, depth):
	width_dif = rc.scale_top_lip_x_max - rc.scale_top_lip_x_min
	scaled_width = (width * width_dif) + rc.scale_top_lip_x_min

	depth_dif = rc.scale_top_lip_z_max - rc.scale_top_lip_z_min
	scaled_depth = (depth * depth_dif) + rc.scale_top_lip_z_min

	print("width : " + str(scaled_width))
	print("depth : " + str(scaled_depth))
	mc.scale_top_lip(scaled_width, scaled_depth)

def trans_top_lip_main(height, depth):
	height_dif = rc.get_trans_top_lip_y_max() - rc.trans_top_lip_y_min
	scaled_height = (height * height_dif) + rc.trans_top_lip_y_min

	depth_dif = rc.trans_top_lip_z_max - rc.trans_top_lip_z_min
	scaled_depth = (depth * depth_dif) + rc.trans_top_lip_z_min

	mc.translate_top_lip(scaled_height, scaled_depth)


