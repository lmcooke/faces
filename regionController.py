import maya.mel as mel
import maya.cmds as cmds

# eye regions
eye_lid = [63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,135,136,137,138,139,140]
eye_ring1 = [51,52,53,54,55,56,57,58,59,60,61,62]
eye_ring2 = [119,120,121,122,123,124,150,151,152,153,154]
eye_ring3 = [155,258,259,260,261,262,263,264,268,269,270,271]

# forehead regions
lower_forehead = [159,160,161,162,163,258,268,269,270,271]
mid_forehead = [272,273,274,275,280]
upper_forehead = [167,168,169,170,171,281,282,283,288,289]
temple = [157,158,165,166,276,277,284,285]

# nose regions
nose_ball = [22,310]
nose_ball_circ1 = [19,20,21,266,267,311]
nose_ball_circ2 = [23,27,28,30,31,96,265,312]
septum = [23,34]
nostril = [24,29,30,31,32,33,89,92,93]
outer_nose = [27,28,97,98,312]
under_nose = [94,95]
nose_bridge = [25,26,124]

# cheek regions
upper_cheek = [125,127,134,261,262,263]
mid_cheek = [116,126,128,292,293,294]
lower_cheek = [102,110,115,129,133]
frown_line = [99,100,101,147,148,149,295,296]

# lip regions
moustache = [36,37,87,297]
fulcrum = [35,88]
beneath_lip = [38,39,40,304]

# chin regions
center_chin = [104, 309, 308, 132, 305, 105, 306, 307]
outer_chin = [103,106,107,108,130,131]

def offset_region(dist, region):
	for face in region:
		print face
		cmds.xform('face.f[%d]' %(face), t=(0,0,dist), relative=True)