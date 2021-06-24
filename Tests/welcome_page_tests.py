import sys
import os
sys.path.append(os.getcwd()[:-5] + "src")

import unittest
from welcome_page_elements import *
import asyncio
import tkinter as tk


class TestWelcome(unittest.TestCase):
    """ Author MZ --> test the welcome pages """
    # this will run on a separate thread.
    async def _start_app(self):
        print("this thread is running:")
        self.app.mainloop()

    def setUp(self):
        """ set up the welcome page and determine the appearance """
        self.appearance = "azure"
        self.app = FrontPage(self.appearance)
        self._start_app()

    def tearDown(self):
        # destroy the window after runnning the tests
        if self.app.welcome_window:
            self.app.welcome_window.destroy()

    def test_startup(self):
        # test the name of the loaded window
        print("testing the title of the screen")
        title = self.app.welcome_window.title()
        expected = "Welcome to ETools"
        self.assertEqual(title, expected)

    def test_appearance(self):
        # test the appearance of the app
        print("...testing the appearance of the app")
        appearance = self.app.appearance
        self.assertEqual(appearance, self.appearance)

    def test_switch(self):
        # test the switch mode for the darkmode
        print("testing the correct state of the switch button at startup")
        switch_state = self.app.switch_mode.get()
        self.assertEqual(switch_state, False)

    "trial_End"
if __name__ == '__main__':
    unittest.main()
