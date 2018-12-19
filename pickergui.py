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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Random Episode Picker", pos = wx.DefaultPosition, size = wx.Size( 457,330 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_SHAPED|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 457,330 ), wx.Size( 457,330 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.collectFileButton = wx.Button( self, wx.ID_ANY, u"Collect Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.collectFileButton, 0, wx.ALL, 5 )

		self.pickEpsButton = wx.Button( self, wx.ID_ANY, u"Pick Episodes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.pickEpsButton, 0, wx.ALL, 5 )

		self.numEpsText = wx.StaticText( self, wx.ID_ANY, u"Number of Episodes to Pick:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.numEpsText.Wrap( -1 )

		bSizer1.Add( self.numEpsText, 0, wx.ALL, 5 )

		self.numEpsSpinner = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1024, 10.000000, 1 )
		self.numEpsSpinner.SetDigits( 0 )
		bSizer1.Add( self.numEpsSpinner, 0, wx.ALL, 5 )

		self.debugOutputBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH )
		bSizer1.Add( self.debugOutputBox, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.collectFileButton.Bind( wx.EVT_BUTTON, self.collectfiles )
		self.pickEpsButton.Bind( wx.EVT_BUTTON, self.pickepisodes )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def collectfiles( self, event ):
		event.Skip()

	def pickepisodes( self, event ):
		event.Skip()


