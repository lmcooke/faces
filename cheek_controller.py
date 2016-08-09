import maya.cmds as cmds
import maya.mel as mel
import main2 as main

#suffix = main.suffix
suffix = ''

def scale_cheeks(s):
	cmds.select(cl=True)
	cmds.select('rt2_basic_cheek_lattice%s' %(suffix))
	cmds.xform(s=(s,s,s), relative=True)

def translate_outer_cheeks(y,z):
	select_upper_outer_cheeks();
	cmds.xform(t=(0,y,z), relative=True)

def rotate_upper_cheeks(rot):
	select_upper_outer_cheeks();
	top_pivot = mel.eval('pointPosition rt2_basic_cheek_lattice%s.pt[1][2][2]' %(suffix))
	bottom_pivot = mel.eval('pointPosition rt2_basic_cheek_lattice%s.pt[1][1][2]' %(suffix))
	x_piv = (top_pivot[0] + bottom_pivot[0])/2.0
	y_piv = (top_pivot[1] + bottom_pivot[1])/2.0
	z_piv = (top_pivot[2] + bottom_pivot[2])/2.0
	cmds.rotate('%sdeg' %rot, 0, 0, r=True, pivot=(x_piv,y_piv,z_piv))


def select_upper_outer_cheeks():
	cmds.select(cl=True)
	for i in range(0,3):
		cmds.select('rt2_basic_cheek_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(1),str(2)), add=True)
		cmds.select('rt2_basic_cheek_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(2),str(2)), add=True)