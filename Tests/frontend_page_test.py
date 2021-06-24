import sys
import os
sys.path.append(os.getcwd()[:-5] + "src")
import unittest
from frontend import *
import asyncio
import tkinter as tk
from matplotlib.figure import Figure
from backend_manager import *
"hello"


class TestFrontPage(unittest.TestCase):
    """ Author MZ --> test the frontend page
    unittests """
    # this will run on a separate thread.
    async def _start_app(self):
        """ asynchronous starting of the mainloop to check for tests """
        print("this thread is running:")
        self.app.mainloop()

    def setUp(self):
        """ set up the testing enviroment """
        self.appearance = "azure"
        self.app = GuiEtools(appearance = self.appearance)
        self._start_app()

    def tearDown(self):
        """ quit the application at the end of the test """

        if self.app.window:
            self.app.window.destroy()

    def test_startup(self):
        """ starting and testing of the window and check for the windows title """

        print("testing the title of the screen")
        title = self.app.window.title()
        expected = "Intra Cellular Recording Mode"
        self.assertEqual(title, expected)

    def test_appearance(self):
        """ check for the light mode in the beginning """
        print("...testing the appearance of the app")
        appearance = self.app.appearance
        self.assertEqual(appearance, self.appearance)

    def test_button_calling(self):
        """ check for the button loaded in the frontend """
        button_texts = [i["text"] for i in [self.app.button_conf, self.app.button_ana, self.app.button_off, self.app.button_stat]]
        print(button_texts)
        self.assertListEqual(button_texts, ['Start configuration', ' Online Analysis', 'Offline Analysis', 'Report/Statistics'])

    def test_button_configuration(self):
        """ check for the notebook oaded in the configuration """
        self.app.draw_analysis(self.app.configuration, func = 1)
        self.assertEqual(len(self.app.Note.frames),4)
        notes_names = [self.app.Note.note.tab(i, option = "text") for i in self.app.Note.note.tabs()]
        self.assertListEqual(notes_names, ["Experiment Initialization","Batch Settings","Communication Log", "Camera"])

    def test_button_online(self):
        """ check for the notebook loaded in the online analysis """
        self.app.draw_analysis(self.app.online_analysis, func = 2)
        self.assertEqual(len(self.app.Note.frames),2)
        notes_names = [self.app.Note.note.tab(i, option = "text") for i in self.app.Note.note.tabs()]
        self.assertListEqual(notes_names, ["Live Data","Labbook"])

    def test_button_offline(self):
        """ check for the notebook loaded in the offline analysis """
        self.app.draw_analysis(self.app.offline_analysis, func = 0)
        self.assertEqual(len(self.app.Note.frames),4)
        notes_names = [self.app.Note.note.tab(i, option = "text") for i in self.app.Note.note.tabs()]
        self.assertListEqual(notes_names, ["Metadata","Start an Analysis","Visualization","Report"])

    def test_button_statistics(self):
        """ check for the notebook in the statistics tab """
        self.app.draw_analysis(self.app.statistics, func = 3)
        self.assertEqual(len(self.app.Note.frames),3)
        notes_names = [self.app.Note.note.tab(i, option = "text") for i in self.app.Note.note.tabs()]
        self.assertListEqual(notes_names, ["Statistical tests", "Parameter", "Quality Control"])

    def test_online_tree(self):
        """ check if the treeview is loaded properly """
        self.app.draw_analysis(self.app.online_analysis, func = 2)
        path = os.getcwd()[:-6]
        self.app.online_manager.dat_file_name = path + "/Data/Raw_digi/201229_01.dat"
        self.app.ona.read_dat_file(self.app.ona.tree, "new")
        children = self.app.ona.tree.get_children()
        self.assertEqual(children[0], "Group1")

    def test_heka_struct_sizes(self):
        """ needs a rework """
        self.app.draw_analysis(self.app.online_analysis, func = 2)
        path = os.getcwd()[:-6]
        self.app.online_manager.dat_file_name = path + "/Data/Raw_digi/201229_01.dat"
        self.app.ona.read_dat_file(self.app.ona.tree, "new")

    def test_length_of_series(self):
        """ Check for the length of the series of the example file"""
        self.app.draw_analysis(self.app.online_analysis, func = 2)
        path = os.getcwd()[:-6]
        self.app.online_manager.dat_file_name = path + "/Data/Raw_digi/201229_01.dat"
        self.app.ona.read_dat_file(self.app.ona.tree, "new")
        #self.assertListEqual(self.app.online_manager.bundle,['.dat', '.pul', '.pgf', '.amp', '', '.mrk', '.mth'])
        self.assertEqual(len(self.app.online_manager.get_pgf_voltage("Group1_Series2")[1]), 21)
        self.assertEqual(len(self.app.online_manager.get_pgf_voltage("Group1_Series3")[1]), 25)
        self.assertEqual(len(self.app.online_manager.get_pgf_voltage("Group1_Series4")[1]), 23)
        self.assertEqual(len(self.app.online_manager.get_pgf_voltage("Group1_Series5")[1]), 1)
        self.assertEqual(len(self.app.online_manager.get_pgf_voltage("Group1_Series6")[1]), 5)

    def test_item_ids(self):
        """ Check item_ids """
        self.app.draw_analysis(self.app.online_analysis, func = 2)
        path = os.getcwd()[:-6]
        self.app.online_manager.dat_file_name = path + "/Data/Raw_digi/201229_01.dat"
        self.app.ona.read_dat_file(self.app.ona.tree, "new")
        self.assertEqual(self.app.online_manager.read_series_from_dat_file(self.app.ona.tree, "Group1_Series2"),21)

    def test_metadata(self):
        """ Check MetaData for the raw analysis file 2"""
        self.app.draw_analysis(self.app.online_analysis, func = 2)
        path = os.getcwd()[:-6]
        self.app.online_manager.dat_file_name = path + "/Data/Raw_digi/201229_01.dat"
        self.app.ona.read_dat_file(self.app.ona.tree, "new")
        self.app.online_manager.get_series_recording_mode("Group1_Series1")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series2_Sweep1_Trace1","Label"), "Imon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series1_Sweep1_Trace1","Label"), "Imon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series3_Sweep1_Trace1","Label"), "Imon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series4_Sweep1_Trace1","Label"), "Imon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series5_Sweep1_Trace1","Label"), "Vmon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series6_Sweep1_Trace1","Label"), "Vmon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series7_Sweep1_Trace1","Label"), "Vmon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series8_Sweep1_Trace1","Label"), "Vmon")
        self.assertEqual(self.app.online_manager.get_metadata("Group1_Series9_Sweep1_Trace1","Label"), "Vmon")


if __name__ == '__main__':
    unittest.main()
