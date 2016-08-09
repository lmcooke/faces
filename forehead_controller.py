import maya.mel as mel
import maya.cmds as cmds
import main2 as main
import decimal as dec

#suffix = main.suffix
suffix = ''

# scales the front forehead plane in the x and y direction as specified.
# acceptal normal ranges : 
# average of x,y = .7 : 1.15
# x/y = 7/11 : 2
def scale_forehead(x, y):
	cmds.select(cl=True)
	select_forehead_plane()
	cmds.xform(s=(x,y,1), relative=True)

# tranlates the forehead plane in the y and z direction
# y-range = -.1 : .2
# z-range = -.03 : .08
def translate_forehead(y,z):
	print("fc suffix : " + suffix)
	select_forehead_plane()
	cmds.xform(t=(0,y,z), relative=True)

# rotates the forehead plane about the x axis, with the center-bottom
# of the plane as the pivot point
# degree range = -20 : 15
def rotate_forehead(rot):
	pivotPoint = mel.eval('pointPosition rt2_basic_forehead_lattice%s.pt[1][0][2]' %(suffix))
	select_forehead_plane()
	cmds.rotate('%sdeg' %rot, 0, 0, r=True, pivot=(pivotPoint[0],pivotPoint[1],pivotPoint[2]))

# offsets the center line of the forehead in the y and z direction
# by a specified amount
def offset_mid_forehead(y,z):
	for point in range(0,3):
		cmds.xform('rt2_basic_forehead_lattice%s.pt[%s][%s][%s]' %(suffix,str(1),str(point),str(2)), t=(0,y,z), relative=True)

# offsets the outer lines of the forehead in the z-direction
# by a specified amount
def offset_side_forehead(x,y):
	for point in range(0,3):
		cmds.xform('rt2_basic_forehead_lattice%s.pt[%s][%s][%s]' %(suffix,str(0),str(point),str(2)), t=(0,0,dist), relative=True)
		cmds.xform('rt2_basic_forehead_lattice%s.pt[%s][%s][%s]' %(suffix,str(2),str(point),str(2)), t=(0,0,dist), relative=True)


# helper function that shouldn't be used outside of this 'class'. 
# selects all the lattice points of the base forehead controller.
def select_forehead_plane():
	cmds.select(cl=True)
	for i in range(0,3):
		for j in range(0,3):
			cmds.select('rt2_basic_forehead_lattice%s.pt[%s][%s][%s]' %(suffix,str(i),str(j),str(2)), add=True)



