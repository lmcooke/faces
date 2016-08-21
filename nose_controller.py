import maya.cmds as cmds
import maya.mel as mel
import main2 as main

#suffix = main.suffix
suffix = ''


# scales the entire nose in specified x,y,z directions.
def scale_nose(x,y,z):
	cmds.select(cl=True)
	cmds.select('rt2_basic_nose_lattice%s' %(suffix))
	cmds.xform(s=(x,y,z), relative=True)

# translates the entire nose lattice in specified y,z direction.
def bulge_nose(y,z):
    cmds.select(cl=True)
    cmds.select('rt2_basic_nose_lattice%s' %(suffix))
    cmds.xform(t=(0,y,z), relative=True)

# translates the tip of the nose in specified y,z directions.
# essentially creates upturned/downturned noses.
def translate_nose_tip(y,z):
	select_outer_plane()
	cmds.xform(t=(0,y,z), relative=True)

# tranlates the nose without affecting the skin around the nose.
def translate_nose(y,z):
	select_outer_two_planes()
	cmds.xform(t=(0,y,z), relative=True)

# controls the flare of nostrils
def nose_flare(x):
	cmds.select(cl=True)
	for i in range(1,3):
		cmds.select('rt2_basic_nose_lattice%s.pt[%s][%s][%s]' %(suffix,str(2),str(0),str(i)), add=True)
		cmds.select('rt2_basic_nose_lattice%s.pt[%s][%s][%s]' %(suffix,str(0),str(0),str(i)), add=True)
	cmds.xform(s=(x,1,1), relative=True)

# helper function which selects outer-most plane of lattice
def select_outer_plane():
	cmds.select(cl=True)
	for i in range(0,3):
		for j in range(0,3):
			cmds.select('rt2_basic_nose_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(j),str(2)), add=True)

# helper function which selects the two outer-most planes of lattice
def select_outer_two_planes():
	cmds.select(cl=True)
	for i in range(0,3):
		for j in range(0,3):
			for k in range(1,3):
				cmds.select('rt2_basic_nose_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(j),str(k)), add=True)