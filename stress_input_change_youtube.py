# Import Tkinter for GUI
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

# Import necessary tools for time pause and date
import time
import datetime
import threading

# Import the ADB_Action_Script.py
# This have all the core function to control the TV
from daaf.ADB_Action_Scipt import ActionScript

# Import the RC keys and App PKGs
# This is a supporting tools for ActionScript
# It has a list of RC key code and App PKGs
from daaf.RC_Code import SonyRCKey
from daaf.AppList import AppList
import daaf.Power_Tools as pt
from daaf.atvAuto import atvAuto


class TestScript(atvAuto):

    def __init__(self, tkRoot):
        """ Initialize the UI and then Set Title Header"""
        # Update the string "Template" to your desired Title
        super().__init__(tkRoot, "HDMI to YouTube input change")

        # this is in minutes
        self.playback_time = 1
        self.loopCount.set(50000)

    def testCaseInfo(self):
        """ 
        Set the test case info
        This is the one that shows on the left side of the screen
        Each call of the 'makeInstructionLabel' is one line
        """
        self.makeInstructionLabel("Tune to HDMI1")
        self.makeInstructionLabel("Wait 10 minutes")
        self.makeInstructionLabel("Tune to YouTube")
        self.makeInstructionLabel("Wait 10 minutes")

    def runThis(self):
        """
        Below is where you assemble test cases
        """
        self.launch_hdmi_input("HDMI1")
        self.wait_minute(10)

        self.launch_youtube()
        self.select_youtube_content()
        self.playback_youtube(10)


# Start the script
root = Tk()
TestScript(root).startApp()
