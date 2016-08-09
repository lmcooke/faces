import maya.cmds as cmds


def create_window():
	print 'opening create_face_window'
	winID = 'create_face_window'

	#delete previous create_face_window if it exists
	if cmds.window(winID, exists=True):
		cmds.deleteUI(winID)
		print 'here'
	print 'previous create_face_window deleted'

	#create window
	cmds.window(winID)
	parent_window = cmds.window(title='Create New Face', iconName='create_face_window', widthHeight=(400,255))
	cmds.scrollLayout(width=300, height=300)

	cmds.frameLayout(label='Proportions', collapsable=True, cl=True, mh=35, w=400)

	#create frame one
	frame_one = cmds.columnLayout()
	cmds.text(label='Face Height')
	cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 200)

	cmds.text(label='Face Width')
	cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 200)

	cmds.text(label='Eye Size')
	cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 200)

	cmds.text(label='Nose Size')
	cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 200)

	cmds.text(label='Mouth Size')
	cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 200)

	cmds.setParent(parent_window)

	#create frame two
	cmds.frameLayout(label='Attributes', collapsable=True, cl=True, mh=20, w=400)
	frame_two = cmds.columnLayout()


	cmds.rowLayout( numberOfColumns=3, columnWidth3=(140, 9, 140), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[(1, 'left', 84), (2, 'both', 0), (3, 'right', 0)] )

	cmds.text(label='Pointy')
	cmds.text(label='')
	cmds.text(label='Rounded')

	cmds.setParent('..')
	cmds.columnLayout()
	cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 300)

	# cmds.rowColumnLayout()

	# cmds.text(label='Pointiness')
	# cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 200)

	cmds.text(label='')

	cmds.rowLayout( numberOfColumns=3, columnWidth3=(140, 9, 140), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[(1, 'left', 84), (2, 'both', 0), (3, 'right', 0)] )
	# cmds.intField()
	cmds.text(label='Masculine')
	cmds.text(label='')
	cmds.text(label='Feminine')

	cmds.setParent('..')
	cmds.columnLayout()
	cmds.floatSliderGrp(field=True,min=0.0,max=1.0,value=0.5, step = .001, width = 300)

	#create final options area
	#TODO: create 'editable checkbox'
	#TODO: create 'random checkbox' --> if random, rest of options should be greyed out
	cmds.setParent(parent_window)
	cmds.columnLayout()

	cmds.button(label='Create and Close', command=('createFaceMenu.execute_face_creation()'))
	# cmds.button(label='Create and Close', command=('cmds.deleteUI(\"' + window + '\", window=True) createFaceMenu.execute_window'))
	cmds.showWindow()

def create_edit_window():
	print 'opening edit_window'
	winID = 'edit_face_window'
	#delete previous edit_face_window if it exists
	if cmds.window(winID, exists=True):
		cmds.deleteUI(winID)
		print 'here2'
	print 'previous edit_face_window deleted'

	cmds.window(winID)
	parent_window = cmds.window(title='Edit Face', iconName='edit_face_window', widthHeight=(500,500))
	
	# create scrollbars and tabs
	#cmds.scrollLayout(width=800, height=800)
	tabControls = cmds.tabLayout()

	# create first tab
	tab_one = cmds.columnLayout()

	cmds.frameLayout(label='Parameters', collapsable=True, cl=True, mh=35, w=900)

	cmds.textField()
	cmds.button(label='do nuthin')

	cmds.setParent(tab_one)
	cmds.frameLayout(label='tab 2', collapsable=True, cl=True, mh=35, w=900)
	cmds.button(label='do nuthin 2')


	# second frame
	cmds.setParent(tab_one)
	cmds.frameLayout(label='tab 3', collapsable=True, cl=True, mh=35, w=900)



	cmds.setParent(parent_window)


	# create second tab
	tab_two = cmds.columnLayout()

	cmds.frameLayout(label='Forehead', collapsable=True, cl=True, mh=35, w=900)

	cmds.setParent(tab_two)
	cmds.frameLayout(label='Cheeks', collapsable=True, cl=True, mh=35, w=900)

	cmds.setParent(tab_two)
	cmds.frameLayout(label='Eyes', collapsable=True, cl=True, mh=35, w=900)

	cmds.setParent(tab_two)
	cmds.frameLayout(label='Nose', collapsable=True, cl=True, mh=35, w=900)

	cmds.setParent(tab_two)
	cmds.frameLayout(label='Mouth', collapsable=True, cl=True, mh=35, w=900)

	cmds.setParent(tab_two)
	cmds.frameLayout(label='Chin', collapsable=True, cl=True, mh=35, w=900)


	# cmds.setParent(parent_window)
	cmds.setParent('..')

	cmds.tabLayout(tabControls, edit=True, tabLabel=( (tab_one, 'Face Options'), (tab_two, 'Advanced Controls') ))

	cmds.setParent(parent_window)
	cmds.columnLayout()
	cmds.button(label='Create and Close', command=('createFaceMenu.execute_face_creation()'))

	cmds.showWindow()


def execute_face_creation():
	print "yay executing"
	cmds.deleteUI(window, window=True)
	print 'hi luc'

	#TODO create the face

	#TODO : see if 'editable' checkbox was checked
	create_edit_window()
	print 'deleted?'