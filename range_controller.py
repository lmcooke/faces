import maya.cmds as cmds
import maya.mel as mel

#nose controls:

nose_scale_x_min = .8
nose_scale_x_max = 1.2
nose_scale_x = nose_scale_x_max - nose_scale_x_min

nose_scale_y_min = .82
nose_scale_y_max = 1.25
nose_scale_z_min = .6
nose_scale_z_max = 1.6
nose_scale_z = (nose_scale_z_max + nose_scale_z_min) / 2.0

nose_bulge_y_min = -.2
nose_bulge_y_max = .15
nose_bulge_z_min = -.25
nose_bulge_z_max = .2

nose_trans_nose_tip_y_min = -.15
nose_trans_nose_tip_y_max = .15

# trans_nose_tip_z_max as function of scale_z
nose_trans_nose_tip_z_min = -.2

def get_trans_nose_tip_z_min():
	if (nose_scale_z < 1.0):
		toReturn = ((nose_scale_z_min - nose_scale_z) / (1.0 - nose_scale_z_min)) * nose_trans_nose_tip_z_min
		print("point nose z min scaled: " + str(toReturn))
		return toReturn
	else:
		return nose_trans_nose_tip_z_min

#trans_nose_tip_z_max as function of scale_z
nose_trans_nose_tip_z_max = .3 

# nose_trans_nose_tip_y range is dependent upon nose_scale_z
def get_trans_nose_tip_z_max():
	if (nose_scale_z > 1.0):
		toReturn = ((nose_scale_z_max - nose_scale_z) / (nose_scale_z_max - 1.0)) * nose_trans_nose_tip_z_max
		return toReturn
	else:
		return nose_trans_nose_tip_z_max

nose_flare_min = .55
nose_flare_max = 1.55

######################################
# eye controls
######################################

scale_eyes_x_min = .8
scale_eyes_x_max = 1.2
scale_eyes_x = (scale_eyes_x_max + scale_eyes_x_min) / 2.0

scale_eyes_y_min = .5
scale_eyes_y_max = 1.35

trans_eyes_x_min = -.25
trans_eyes_x_max = .15

trans_eyes_y_min = -.45
trans_eyes_y_max = .45

trans_eyes_z_min = -.5
trans_eyes_z_max = .3

rotate_eyes_y_min = -15
rotate_eyes_y_max = 15

rotate_eyes_z_min = -10
rotate_eyes_z_max = 10

furrow_min = -.5
furrow_max = .8

######################################
# mouth controls
######################################

scale_mouth_x_min = .55
scale_mouth_x_max = 1.3
scale_mouth_x = (scale_mouth_x_max - scale_mouth_x_min) / 2.0

scale_mouth_y_min = .4
scale_mouth_y_max = 1.5
scale_mouth_y = (scale_mouth_y_max - scale_mouth_y_min) / 2.0

trans_mouth_y_min = -.1
trans_mouth_y_max = .15

trans_mouth_z_min = -.5
trans_mouth_z_max = .1

mouth_rot_min = -30
mouth_rot_max = 30

# min lips as function of average of scale_mouth_x_min and scale_mouth_y_min
scale_lips_min = .5
def get_scale_lips_min():
	ave_scale = (scale_mouth_x + scale_mouth_y) / 2.0
	ave_min = (scale_mouth_x_min + scale_mouth_y_min) / 2.0
	if (ave_scale < 1.0):
		toReturn = 1.0 - (((ave_scale - ave_min) / (1.0 - ave_min)) * scale_lips_min)
		print("min lip scale : " + str(toReturn))
		return toReturn
	else:
		return scale_lips_min

scale_lips_max = 1.5
def get_scale_lips_max():
	ave_scale = (scale_mouth_x + scale_mouth_y) / 2.0
	ave_max = (scale_mouth_x_max + scale_mouth_y_max) / 2.0
	if (ave_scale > 1.0):
		toReturn = (((ave_max - ave_scale) / (ave_max - 1.0)) * scale_lips_max) + 1.0
		return toReturn
	else:
		return scale_lips_max

arch_lip_y_min = -.2
arch_lip_y_max = .2

arch_lip_z_min = -.4
arch_lip_z_max = .4

scale_top_lip_x_min = 1
scale_top_lip_x_max = 1.5

# def get_scale_top_lip_x_min():
# 	mouth_width = mouth_scale_width = mel.eval("floatSliderGrp -query -value $mouth_scale_width")
# 	if (mouth_width < 0.5):
# 		print "hi"
# 		#TODO

scale_top_lip_z_min = .55
scale_top_lip_z_max = 2.5

trans_top_lip_y_min = -.25
trans_top_lip_y_max = .2

# trans_top_lip_y_max should decrease as mouth_width decreases
def get_trans_top_lip_y_max():
	mouth_width = mouth_scale_width = mel.eval("floatSliderGrp -query -value $mouth_scale_width")
	if (mouth_width < 0.5):
		print "small mouth width"
		max_min_dif = trans_top_lip_y_max - trans_top_lip_y_min
		new_max = (mouth_width * max_min_dif) + trans_top_lip_y_min
		print new_max
		return new_max
	else:
		return trans_top_lip_y_max

trans_top_lip_z_min = -.1
trans_top_lip_z_max = .3

######################################
# cheek controls
######################################

scale_cheeks_min = .85 
scale_cheeks_max = 1.15
scale_cheeks = (scale_cheeks_min + scale_cheeks_max) / 2.0

trans_outer_cheeks_y_min = -.15
trans_outer_cheeks_y_max = .2
trans_outer_cheeks_y = (trans_outer_cheeks_y_max + trans_outer_cheeks_y_min) / 2.0

trans_outer_cheeks_z_min = -.3

# trans_outer_cheeks_z_max as function of cheeks size
trans_outer_cheeks_z_max = .3

def get_trans_outer_cheeks_z_max():
	if (scale_cheeks > 1.0):
		toReturn = ((scale_cheeks_max - scale_cheeks) / (scale_cheeks_max - 1.0)) * trans_outer_cheeks_z_max
		return toReturn
	else:
		return trans_outer_cheeks_z_max

# rot_min as function of trans_outer_cheeks_y_min
cheeks_rot_min = -45

def get_cheeks_rot_min():
	if (trans_outer_cheeks_y < 0.0):
		toReturn = ((trans_outer_cheeks_y_min - trans_outer_cheeks_y) / (trans_outer_cheeks_y_min)) * cheeks_rot_min
		return toReturn
	else:
		return cheeks_rot_min 


cheeks_rot_max = 70
def get_cheeks_rot_max():
	if (trans_outer_cheeks_y > 0.0):
		toReturn = ((trans_outer_cheeks_y_max - trans_outer_cheeks_y) / (trans_outer_cheeks_y_max) * cheeks_rot_max)
		return toReturn
	else:
		return cheeks_rot_max

######################################
# forehead controls
######################################

forehead_scale_ave_min = .7
forehead_scale_ave_max = 1.15
forehead_scale_ratio_min = 7.0 / 11.0
forehead_scale_ratio_max = 2.0

forehead_trans_y_min = -.1
forehead_trans_y_max = .2
forehead_trans_z_min = -.03
forehead_trans_z_max = .08

forehead_rotate_min = -20.0
forehead_rotate_max = 15.0

######################################
# chin controls
######################################

scale_chin_x_min = .8
scale_chin_x_max = 1.15

scale_chin_y_min = .5
scale_chin_y_max = 1.35

scale_chin_z_min = .2
scale_chin_z_max = 1.6
scale_chin_z = (scale_chin_y_max + scale_chin_y_min) / 2.0

translate_chin_y_min = -.3
translate_chin_y_max = .16

translate_chin_z_min = -.5
translate_chin_z_max = .35

chin_rot_min = -35
chin_rot_max = 20

point_chin_y_min = -.3
point_chin_y_max = .2


# as function of scale_z_chin
point_chin_z_min = -.7
def get_point_chin_z_min():
	if (scale_chin_z < 1.0):
		toReturn = ((scale_chin_z_min - scale_chin_z) / (1.0 - scale_chin_z_min)) * -point_chin_z_min
		return toReturn
	else:
		return point_chin_z_min



# as function of scale_z_chin
point_chin_z_max = .25
def get_point_chin_z_max():
	if (scale_chin_z > 1.0):
		toReturn = ((scale_chin_z_max - scale_chin_z) / (scale_chin_z_max - 1.0)) * point_chin_z_max
		return toReturn
	else:
		return point_chin_z_max








