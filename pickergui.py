# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainscreen
###########################################################################

class mainscreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Random Episode Picker", pos = wx.DefaultPosition, size = wx.Size( 457,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_SHAPED|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 457,400 ), wx.Size( 457,400 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.collectFileButton = wx.Button( self, wx.ID_ANY, u"Collect Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.collectFileButton, 0, wx.ALL, 5 )

		self.pickEpsButton = wx.Button( self, wx.ID_ANY, u"Pick Episodes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.pickEpsButton, 0, wx.ALL, 5 )

		self.numEpsText = wx.StaticText( self, wx.ID_ANY, u"Number of Episodes to Pick:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.numEpsText.Wrap( -1 )

		bSizer1.Add( self.numEpsText, 0, wx.ALL, 5 )

		self.numEpsSpinner = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 1024, 10.000000, 1 )
		self.numEpsSpinner.SetDigits( 0 )
		bSizer1.Add( self.numEpsSpinner, 0, wx.ALL, 5 )

		self.dirpickertxt = wx.StaticText( self, wx.ID_ANY, u"Directory to choose files from:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dirpickertxt.Wrap( -1 )

		bSizer1.Add( self.dirpickertxt, 0, wx.ALL, 5 )

		self.dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer1.Add( self.dirPicker, 0, wx.ALL|wx.EXPAND, 5 )

		self.subdirCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Include Subdirectories", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.subdirCheckBox.SetValue(True)
		bSizer1.Add( self.subdirCheckBox, 0, wx.ALL, 5 )

		self.debugOutputBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH )
		bSizer1.Add( self.debugOutputBox, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.collectFileButton.Bind( wx.EVT_BUTTON, self.collectfiles )
		self.pickEpsButton.Bind( wx.EVT_BUTTON, self.pickepisodes )
		self.dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.setNewPath )
		self.subdirCheckBox.Bind( wx.EVT_CHECKBOX, self.changeSubdir )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def collectfiles( self, event ):
		event.Skip()

	def pickepisodes( self, event ):
		event.Skip()

	def setNewPath( self, event ):
		event.Skip()

	def changeSubdir( self, event ):
		event.Skip()


