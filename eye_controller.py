import maya.cmds as cmds
import maya.mel as mel
import main2 as main


#suffix = main.suffix
suffix = ''

def scale_eyes(x,y):
	cmds.select(cl=True)
	cmds.select('rt2_basic_eye_latticeR%s' %(suffix), add=True)
	cmds.select('rt2_basic_eye_latticeL%s' %(suffix), add=True)
	cmds.xform(s=(x,y,1), relative=True)

# translates eyes up/down and forward/backward using y,z inputs.
# translates the eyes closer/farther from the center of the face 
# using the x input. the x input corresponds to the right eye.
def translate_eyes(x,y,z):
	cmds.select(cl=True)
	cmds.select('rt2_basic_eye_latticeR%s' %(suffix))
	cmds.xform(t=(x,y,z), relative=True)

	cmds.select(cl=True)
	cmds.select('rt2_basic_eye_latticeL%s' %(suffix))
	cmds.xform(t=(-x,y,z), relative=True)

# creates a slant in both eyes (in opposite directions)
def rotate_eyes(y_rot, z_rot):
	cmds.select(cl=True)
	pivotPointR = mel.eval('pointPosition rt2_basic_eye_latticeR%s.pt[1][1][1]' %(suffix))
	cmds.select('rt2_basic_eye_latticeR%s' %(suffix))
	cmds.rotate(0, '%sdeg' %y_rot, '%sdeg' %z_rot, r=True, pivot=(pivotPointR[0],pivotPointR[1],pivotPointR[2]))

	cmds.select(cl=True)
	pivotPointR = mel.eval('pointPosition rt2_basic_eye_latticeL%s.pt[1][1][1]' %(suffix))
	cmds.select('rt2_basic_eye_latticeL%s' %(suffix))
	cmds.rotate(0, '%sdeg' %-y_rot, '%sdeg' %-z_rot, r=True, pivot=(pivotPointR[0],pivotPointR[1],pivotPointR[2]))

def furrow_brow(furrow):
	select_top_plane("L")
	cmds.xform(t=(0,0,furrow), relative=True)
	select_top_plane("R")
	cmds.xform(t=(0,0,furrow), relative=True)

# select the top plane of either eye lattice, depending on if the input is "L" or "R".
def select_top_plane(side):
	cmds.select(cl=True)
	for i in range(0,3):
		for j in range(0,3):
			cmds.select('rt2_basic_eye_lattice%s.pt[%s][%s][%s]' %((side + suffix),str(i),str(2),str(j)), add=True)