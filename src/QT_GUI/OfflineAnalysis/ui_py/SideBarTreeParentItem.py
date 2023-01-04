from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class SideBarParentItem(QTreeWidgetItem):
    """Should Create the SideBarParentItem and 
    should set the data accordingly

    Args:
        QTreeWidgetItem (_type_): _description_
    """
    def __init__(self, treeview_widget):
        super().__init__()
        self.treeview_widget = treeview_widget
        
    def setting_data(self, series_name, tab_widget, stacked_widget, index, appended_childs):
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
    """_summary_

    Args:
        QTreeWidgetItem (_type_): _description_
    """
    def __init__(self,parent_widget, child_text):
        super().__init__()
        self.setText(0, child_text)
        self.parent_widget = parent_widget
        
    def setting_data(self, tab_widget, stacked_widget, index, parent_count):
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
    """_summary_

    Args:
        QTreeWidgetItem (_type_): _description_
    """
    
    def __init__(self, text, parent):
        super().__init__()
        self.setText(0, text)
        parent.addChild(self)
        
    def setting_data(self, stacked_widget = None):
        # save the widget
        self.setData(4, Qt.UserRole, stacked_widget)
        self.setData(6, Qt.UserRole, 0)# save the child notebook
        self.setData(5, Qt.UserRole, 1)
   
             
    