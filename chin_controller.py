import maya.cmds as cmds
import maya.mel as mel
import main2 as main

#suffix = main.suffix
suffix = ''

def scale_chin(x,y,z):
	cmds.select(cl=True)
	cmds.select('rt2_basic_chin_lattice%s' %(suffix))
	cmds.xform(s=(x,y,z), relative=True)

def translate_chin(y,z):
	
	cmds.select(cl=True)
	cmds.select('rt2_basic_chin_lattice%s' %(suffix))
	cmds.xform(t=(0,y,z), relative=True)

def rotate_chin(rot):
	cmds.select(cl=True)
	select_bottom_planes()
	pivotPoint = mel.eval('pointPosition rt2_basic_chin_lattice%s.pt[1][1][1]' %(suffix))
	cmds.rotate('%sdeg' %rot, 0, 0, r=True, pivot=(pivotPoint[0],pivotPoint[1],pivotPoint[2]))

def point_chin(y,z):
	select_mid_chin()
	cmds.xform(t=(0,y,z), relative=True)

def select_mid_chin():
	cmds.select(cl=True)
	for i in range(0,2):
		cmds.select('rt2_basic_chin_lattice%s.pt[%s][%s][%s]' %(suffix,str(1),str(i),str(2)), add=True)

def select_bottom_planes():
	cmds.select(cl=True)
	for i in range(0,3):
		for j in range(0,3):
			for k in range(0,2):
				cmds.select('rt2_basic_chin_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(k),str(j)), add=True)