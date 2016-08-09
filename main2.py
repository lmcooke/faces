import maya.mel as mel
import maya.cmds as cmds
import noseController as noseController

import forehead_controller
import forehead_main

import nose_controller
import nose_main

import cheek_controller
import cheek_main

import chin_controller
import chin_main

import mouth_controller
import mouth_main

import eye_controller
import eye_main

suffix = ''

# arg = 1 if random button was selected
def mainny(arg):
	print("arg: " + str(arg))
	suffix = getFaceName()
	# mel.eval("file -import -type \"mayaAscii\"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace \"face\" -options \"v=0;\"  -pr \"/Users/lucicooke/Documents/School Work/Brown University/Semester 6/animation/final_project/3_base_face/half_face_base.ma\";")
	mel.eval("file -import -type \"mayaAscii\"  -ignoreVersion -ra true -mergeNamespacesOnClash false -options \"v=0;\"  -pr \"/Users/lucicooke/Documents/School Work/Brown University/Semester 6/animation/final_project/rigging_test1/rt2.ma\";")

	eye_width = mel.eval("floatSliderGrp -query -value $eye_width")

	# set suffix as needed
	forehead_controller.suffix = suffix
	nose_controller.suffix = suffix
	cheek_controller.suffix = suffix
	chin_controller.suffix = suffix
	mouth_controller.suffix = suffix
	eye_controller.suffix = suffix
	
	# adjust geometry based on input measurements
	forehead_main.main(arg)
	nose_main.main(arg)
	cheek_main.main(arg)
	chin_main.main2(arg)
	mouth_main.main(arg)
	eye_main.main(arg)



# an attempt to solve the re-numbering problem of importing faces
# returns a string representing the suffix number of the next face
# to import.
# note: this only checks the name of the mesh, so will run into problems
# if lattices are renamed but meshs is not (or vice versa...)
def getFaceName():
	if(cmds.objExists('rt2_basic_forehead_lattice')):
		i = 1
		while(cmds.objExists('rt2_basic_forehead_lattice%s' % (i))):
			i = i + 1

		return str(i)
	else:
		return ''

# necessary if altering mesh directly, instead of lattices
def mirrorFinalFace():
	cmds.polyMirrorFace('face', direction=0, mergeMode=1)