import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtGui import QFontDatabase, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui-files/page_container.ui', self)    #Load widget container UI file, avoiding the spaghetti py code
        
        #-- Initialize window objects (these are QWidgets since the main window is this class) --#
        self.landingPageWindow = LandingPageWindow()
        self.simpleCalcWindow = SimpleCalcWindow()
        self.advancedCalcWindow = AdvancedCalcWindow()
        self.settingsWindow = SettingsWindow()
        self.helpWindow = HelpWindow()
        
        #-- Add the QWidget objects into the stacked widget hierarchy --#
        self.stackedWidget.addWidget(self.landingPageWindow)
        self.stackedWidget.addWidget(self.simpleCalcWindow)
        self.stackedWidget.addWidget(self.advancedCalcWindow)
        self.stackedWidget.addWidget(self.settingsWindow)
        self.stackedWidget.addWidget(self.helpWindow)
        
        #-- Connect the signals so we can control pages changes --#
        self.landingPageWindow.switch_to_landing_window.connect(self.go_to_landing_window)
        self.landingPageWindow.switch_to_simple_window.connect(self.go_to_simple_window)
        self.landingPageWindow.switch_to_adv_window.connect(self.go_to_advanced_window)
        self.landingPageWindow.switch_to_settings_window.connect(self.go_to_settings_window)
        self.landingPageWindow.switch_to_help_window.connect(self.go_to_help_window)
    
    #-- Functions for handling changing visible widget, changed from setCurrentIndex() to --#
    #-- setCurrentWidget() to avoid having to memorize order, and precisely switch using object --#
    def go_to_landing_window(self):
        self.stackedWidget.setCurrentWidget(self.landingPageWindow)
    
    def go_to_simple_window(self):
        self.stackedWidget.setCurrentWidget(self.simpleCalcWindow)
    
    def go_to_advanced_window(self):
        self.stackedWidget.setCurrentWidget(self.advancedCalcWindow)
    
    def go_to_settings_window(self):
        self.stackedWidget.setCurrentWidget(self.settingsWindow)
    
    def go_to_help_window(self):
        self.stackedWidget.setCurrentWidget(self.helpWindow)

class LandingPageWindow(QWidget):
    switch_to_landing_window = pyqtSignal()
    switch_to_simple_window = pyqtSignal()
    switch_to_adv_window = pyqtSignal()
    switch_to_settings_window = pyqtSignal()
    switch_to_help_window = pyqtSignal()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui-files/startup_screen.ui', self)
        
        self.simpleCalcBut.clicked.connect(self.on_simple_window_clicked)
        self.advancedCalcBut.clicked.connect(self.on_adv_window_clicked)
        self.settingsBut.clicked.connect(self.on_settings_window_clicked)
        self.helpBut.clicked.connect(self.on_help_window_clicked)
    
    def on_landing_window_clicked(self):
        self.switch_to_landing_window.emit()
    
    def on_simple_window_clicked(self):
        self.switch_to_simple_window.emit()
    
    def on_adv_window_clicked(self):
        self.switch_to_adv_window.emit()
    
    def on_settings_window_clicked(self):
        self.switch_to_settings_window.emit()
    
    def on_help_window_clicked(self):
        self.switch_to_help_window.emit()

class SimpleCalcWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('./ui-files/simple_calc.ui', self)
        
        # Test for trying to determine how to access labels and check if their object names match;
        # used for doing some layout work and trying to stylize things. Useful for other widgets too!
        labels = self.findChildren(QLabel)
        label_dict = {label.objectName(): label for label in labels} #Lambda function to make a dict of label names for lookup
        for i in range(1,6):
            label_name = f"col{i}_info"
            if label_name in label_dict:
                label = label_dict[label_name]
                print(f"Found QLabel: {label.objectName()}")
                label.setText(f"Info for Column {i}")
            else:
                print(f"No QLabel found with name: {label_name}")

class AdvancedCalcWindow(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #uic.loadUi('', self)

class SettingsWindow(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #uic.loadUi('', self)

class HelpWindow(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #uic.loadUi('', self)

def get_user_monitor_size(QApplication):
	screensize = QApplication.primaryScreen().geometry()
	return screensize
	
def find_and_update_widgets(self, widget_type, name_pattern, iterator_range=None, action=None):
    """
    Find and update widgets based on a name pattern and type.

    Parameters:
    - self: Reference to the parent widget or layout.
    - widget_type: Type of widget to search for (e.g., QLabel, QWidget, etc.).
    - name_pattern: Pattern for widget names, where '{}' can be used as a placeholder for an iterator.
    - iterator_range: Optional range (start, stop) for iterating over name patterns. If None, searches for a static name.
    - action: Optional function to perform on each matched widget. Should accept the widget and iterator as arguments.
              If None, a default print action will be used.

    Example Usage:
    find_and_update_widgets(self, QLabel, "col{}_info", range(1, 6), 
                            lambda widget, i: widget.setText(f"Info for Column {i}"))
    """
    # Find all widgets of the given type
    widgets = self.findChildren(widget_type)
    widget_dict = {widget.objectName(): widget for widget in widgets}

    # Handle optional iterator range for dynamic patterns
    if iterator_range:
        for i in iterator_range:
            widget_name = name_pattern.format(i)
            if widget_name in widget_dict:
                widget = widget_dict[widget_name]
                print(f"Found {widget_type.__name__}: {widget.objectName()}")
                if action:
                    action(widget, i)  # Perform the custom action
                else:
                    print(f"No action specified for {widget.objectName()}")
            else:
                print(f"No {widget_type.__name__} found with name: {widget_name}")
    else:
        # Static name pattern
        if name_pattern in widget_dict:
            widget = widget_dict[name_pattern]
            print(f"Found {widget_type.__name__}: {widget.objectName()}")
            if action:
                action(widget, None)  # No iterator, pass None
        else:
            print(f"No {widget_type.__name__} found with name: {name_pattern}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwindow = MainWindow()
    
    #PLACEHOLDER -- INIT CODE GOES HERE#
    screen_size = get_user_monitor_size(app)
    mwindow.setGeometry(0,0,screen_size.width()-20,screen_size.height()-20)
    
    mwindow.show()
    app.exec_()
