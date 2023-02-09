from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class SideBarParentItem(QTreeWidgetItem):
    """Should Create the SideBarParentItem and 
    should set the data accordingly
    """
    def __init__(self, treeview_widget):
        """_summary_

        Args:
            treeview_widget (Qt.TreeWidget): Widget that holds the offline analysis overview
        """
        super().__init__()
        self.treeview_widget = treeview_widget
        
    def setting_data(self, series_name, tab_widget, stacked_widget, index, appended_childs):
        """Should set the Data necessary to retrieve information about 
        the analysis for each individual parent item

        Args:
            series_name (str): Name of the Series analyzed e.g IV
            tab_widget (Qt.StackedWidget): Widget that holds the Configurator 
            stacked_widget (Qt.StackedWidget): Nested Widget to simulate tree like structure
            index (int): Current index of the parent
            appended_childs (bool, default -> False): Checks if the childs plot, table ect. are already appended
        """
        self.setText(0, series_name + " Analysis")
        self.setData(1, Qt.UserRole, "self")  # check if self
        self.setData(2, Qt.UserRole, tab_widget)  # save the widget
        self.setData(4, Qt.UserRole, stacked_widget)  # save the child notebook
        self.setData(5, Qt.UserRole, 0)
        self.setData(6, Qt.UserRole, series_name)  # specific series name
        self.setData(7, Qt.UserRole, index)  # save the index
        self.setData(8, Qt.UserRole, appended_childs)  # data to check if additional childs like plot ect are already drawn
        self.treeview_widget.addTopLevelItem(self)
        
    def __str__(self) -> str:
        return self.series_name
              
class SideBarConfiguratorItem(QTreeWidgetItem):
    """Should create the Child Items for the Series Parents holding
    the Configurator

    """
    def __init__(self,parent_widget, child_text, reload = False):
        """_summary_

        Args:
            parent_widget (QTreeWidgetItem): Parent as initialized in SideBarParentItem
            child_text (str): Text that is shown as label e.g. Analysis Configurator
        """
        super().__init__()
        self.setText(0, child_text)
        self.parent_widget = parent_widget
        
    def setting_data(self, tab_widget, stacked_widget, index, parent_count):
        """Sets the Data to detect which child is selected

        Args:
            tab_widget (_type_): _description_
            stacked_widget (_type_): _description_
            index (_type_): _description_
            parent_count (_type_): _description_
        """
        self.setData(2, Qt.UserRole, tab_widget)  # save the widget
        self.setData(4, Qt.UserRole, stacked_widget)  # save the child notebook
        self.setData(5, Qt.UserRole, 1)
        self.setData(6, Qt.UserRole, parent_count)  # specific series name
        self.setData(7, Qt.UserRole, index)
        self.setData(8, Qt.UserRole, False)
        self.parent_widget.addChild(self)
        
    def __str__(self) -> str:
        return self.text()
    

class SideBarAnalysisItem(QTreeWidgetItem):
    """Should add the Items Plot, Tables, Statistics and Advanced Analysis
    """
    
    def __init__(self, text, parent):
        """_summary_

        Args:
            text (str): text that acts as label e.g Plot
            parent (Qt.TreeWidgetItem): Parent as initialized in SideBarAnalysisItem e.g IV
        """
        super().__init__()
        self.setText(0, text)
        parent.addChild(self)
        
    def setting_data(self, stacked_widget = None):
        """_summary_

        Args:
            stacked_widget (_type_, optional): _description_. Defaults to None.
        """
        self.setData(4, Qt.UserRole, stacked_widget)
        self.setData(6, Qt.UserRole, 0)# save the child notebook
        self.setData(5, Qt.UserRole, 1)
   
             
    