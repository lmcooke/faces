import maya.mel as mel
import maya.cmds as cmds

nose_dropoff_rate = .5

def main():
	nose_length = mel.eval("floatSliderGrp -query -value $nose_length")
	nose_width = mel.eval("floatSliderGrp -query -value $nose_width")
	nose_size = mel.eval("floatSliderGrp -query -value $nose_size")
	print("nose main. nose_length : " + str(nose_length))
	print("nose main. nose_width : " + str(nose_width))


def noseController(noseLength):
	print("testing take 2 : " + str(noseLength))
	# cmds.polyMoveVertex('face.vtx[31]', t=(0,0,1))

