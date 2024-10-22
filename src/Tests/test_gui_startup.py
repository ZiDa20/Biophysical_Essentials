import pytest
from PySide6.QtWidgets import QApplication
from Frontend.MainWindow.ui_py.main_window import Ui_MainWindow
from start import MainWindow
from PySide6.QtCore import QSize

@pytest.fixture()
def app(qtbot):
    """Fixture to initialize the application."""
    if not QApplication.instance():
        test_app = QApplication([])
    else:
        test_app = QApplication.instance()
    
    main_window = MainWindow()
    qtbot.addWidget(main_window)
    return main_window

def test_main_window_initialization(app):
    """Test to check if the main window initializes correctly."""
    # Check if the main window is visible
    print(app.isVisible())
    #assert app.isVisible()

    # Check if the main window has the correct title
    version = app.settings_file_handler.get_parameter("versioning","release")
    assert app.windowTitle() == (f"Biophysical Essentials (version {version})")  # Adjust version as needed
    assert app.ui.side_left_menu.isHidden()
    # Check if the central widget is set
    assert app.ui.offline.stackedWidget is not None
    assert app.ui.offline.stackedWidget.currentIndex() == 1
    assert app.centralWidget() is not None

    # Check if the status bar is showing the correct message
    assert app.statusBar().currentMessage() == "Program Started and Database Connected:"

    # Check if the main window has the correct minimum size
    assert app.minimumSize() == QSize(1600, 800)

    # Check if the background logo is set correctly
    expected_style_sheet = (
        "QFrame#frame {"
        "background-image: url(:/Frontend/Button/Logo/welcome_page_background_logo.png);"
        "background-repeat: no-repeat;"
        "background-position: center;"
        "}"
    )
    assert app.ui.frame.styleSheet() == expected_style_sheet

    # Check if the frontend style is set to light mode
    assert app.frontend_style.default_mode == 1  # Assuming 1 is light mode

    # Check if the database handlers are initialized
    assert app.local_database_handler is not None
    assert app.online_database is not None
    assert app.online_database is not None
    assert app.frontend_style is not None
    assert app.logger is not None
    

    
