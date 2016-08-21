import maya.mel as mel

def main():
	testVariable = mel.eval("floatSliderGrp -query -value $measure1_float")
	print(testVariable)
	print ("hi there luci things are working hey ")

print("done")