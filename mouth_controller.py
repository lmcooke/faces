import maya.cmds as cmds
import maya.mel as mel
import main2 as main

#suffix = main.suffix
suffix = ''

def scale_mouth(x,y):
	print("scaling mouth")
	cmds.select(cl=True)
	cmds.select('rt2_basic_mouth_lattice%s' %(suffix))
	cmds.xform(s=(x,y,1), relative=True)

def translate_mouth(y,z):
	cmds.select(cl=True)
	cmds.select('rt2_basic_mouth_lattice%s' %(suffix))
	cmds.xform(t=(0,y,z), relative=True)

def rotate_mouth(rot):
	cmds.select(cl=True)
	cmds.select('rt2_basic_mouth_lattice%s' %(suffix))
	pivotPoint = mel.eval('pointPosition rt2_basic_mouth_lattice%s.pt[1][1][1]' %(suffix))
	cmds.rotate('%sdeg' %rot, 0, 0, r=True, pivot=(pivotPoint[0],pivotPoint[1],pivotPoint[2]))

def scale_lips(scale):
	select_inner_plane()
	cmds.xform(s=(scale,1,scale), relative=True)

def arch_lip(y,z):
	select_center_line()
	cmds.xform(t=(0,y,z), relative=True)

def scale_top_lip(x,z):
	select_top_plane()	
	cmds.xform(s=(x,1,z), relative=True)

def translate_top_lip(y,z):
	select_top_plane()	
	cmds.xform(t=(0,y,z), relative=True)

def select_top_plane():
	cmds.select(cl=True)
	for i in range(0,3):
		for j in range(0,3):
			cmds.select('rt2_basic_mouth_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(2),str(j)), add=True)	

# selects the inner middle horizontal plane of the mouth lattice.
# The targets specifically the lips
def select_inner_plane():
	cmds.select(cl=True)
	for i in range(0,3):
		for j in range(0,3):
			cmds.select('rt2_basic_mouth_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(1),str(j)), add=True)	
		# cmds.select('rt2_basic_mouth_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(1),str(0)), add=True)
		# cmds.select('rt2_basic_mouth_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(1),str(1)), add=True)
		# cmds.select('rt2_basic_mouth_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(1),str(2)), add=True)

def select_center_line():
	cmds.select(cl=True)
	for i in range(0,3):
		cmds.select('rt2_basic_mouth_lattice%s.pt[%s][%s][%s]' %(suffix,str(1),str(i),str(2)), add=True)	
