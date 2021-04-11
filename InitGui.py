# -*- coding: utf-8 -*-
###################################################################################
#
#  InitGui.py
#  
#  Copyright 2019 Mark Ganson <TheMarkster> mwganson at gmail
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
###################################################################################

import threadprofilewb_locator
threadprofileWBPath = os.path.dirname(threadprofilewb_locator.__file__)
threadprofileWB_icons_path = os.path.join(threadprofileWBPath,'Resources','icons')

global main_threadprofileWB_Icon

main_threadprofileWB_Icon = os.path.join(threadprofileWB_icons_path , 'ThreadProfileLogo.svg')

#def myFunc(string):
#    print (string)
#    global act
#    act.setVisible(True)

#mw=Gui.getMainWindow()
#bar=mw.menuBar()
#act=bar.addAction("MyCmd")
#mw.workbenchActivated.connect(myFunc)

####################################################################################
# Initialize the workbench 
class ThreadProfileWorkbench(Workbench):
 

    global main_threadprofileWB_Icon

    MenuText = "ThreadProfile"
    ToolTip = "ThreadProfile workbench"
    Icon = main_threadprofileWB_Icon
    
    def __init__(self):
        pass

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import ThreadProfileCmd #needed files for FreeCAD commands
        self.list = ["ThreadProfileCreateObject", "ThreadProfileCreateButtressObject", "ThreadProfileCreateBottleObject", "ThreadProfileCreateAdvancedObject",
                    "ThreadProfileMakeHelix", "ThreadProfileDoSweep", "ThreadProfileOpenOnlineCalculator",
                    "ThreadProfileSettings"] # A list of command names created in the line above
        self.appendToolbar("ThreadProfile Commands",self.list[:-1]) # leave settings off toolbar
        self.appendMenu("&ThreadProfile",self.list) # creates a new menu
        #considered putting the menu inside the Edit menu, but decided against it
        #self.appendMenu(["&Edit","ThreadProfile"],self.list) # appends a submenu to an existing menu


 
    def Activated(self):
        "This function is executed when the workbench is activated"
        #global act
        #act.setVisible(True)
        return
 
    def Deactivated(self):
        "This function is executed when the workbench is deactivated"

        #FreeCAD will hide our menu and toolbar upon exiting the wb, so we setup a singleshot
        #to unhide them once FreeCAD is finished, 2 seconds later
        from PySide import QtCore
        QtCore.QTimer.singleShot(2000, self.showMenu)
        return 
        
    def showMenu(self):
        from PySide import QtGui
        window = QtGui.QApplication.activeWindow()
        #freecad hides wb toolbars on leaving wb, we unhide ours here to keep it around
        #if the user has it set in parameters to do so
        pg = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/ThreadProfile")
        keep = pg.GetBool('KeepToolbar',True)
        if not keep:
            return
        tb = window.findChildren(QtGui.QToolBar) 
        for bar in tb:
            if "ThreadProfile Commands" in bar.objectName():
                bar.setVisible(True)

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("ThreadProfile",self.list) # add commands to the context menu
 
    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
wb = ThreadProfileWorkbench()
Gui.addWorkbench(wb)





