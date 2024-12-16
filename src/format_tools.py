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
    "Update Text for Dynamic Labels"
    find_and_update_widgets(
        self, 
        QLabel, 
        "col{}_info", 
        range(1, 6), 
        lambda widget, i: widget.setText(f"Info for Column {i}")
    )
    
    OR
    
    "Apply Styles to Widgets by Name"
    find_and_update_widgets(
        self, 
        QLabel, 
        "label_{}_title", 
        range(1, 10), 
        lambda widget, i: widget.setStyleSheet("color: blue; font-weight: bold;")
    )
    
    OR
    
    "Find a Single Widget by Static Name"
    find_and_update_widgets(
        self, 
        QLabel, 
        "static_label_name", 
        action=lambda widget, _: print(f"Found widget: {widget.objectName()}")
    )

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


def apply_style_to_widgets(self, widget_type, style, name_filter=None):
    """
    Apply a stylesheet to all widgets of a certain type, optionally filtering by name.

    Parameters:
    - self: Parent widget containing child widgets.
    - widget_type: Type of widget to search for (e.g., QLabel, QPushButton).
    - style: String containing the CSS-like stylesheet.
    - name_filter: Optional substring to filter widget names (e.g., "button" to match "submit_button").
    
    Examples:
    apply_style_to_widgets(self, QLabel, "font-weight: bold;", name_filter="title")
    &&
    apply_style_to_widgets(self, QPushButton, "background-color: green;", name_filter="save")
    """
    
    widgets = self.findChildren(widget_type)
    for widget in widgets:
        if name_filter is None or name_filter in widget.objectName():
            print(f"Applying style to {widget_type.__name__}: {widget.objectName()}")
            widget.setStyleSheet(style)


def adjust_widget_properties(self, widget_type, property_name, property_value, name_filter=None):
    """
    Adjust specific properties of widgets.

    Parameters:
    - self: Parent widget containing child widgets.
    - widget_type: Type of widget to search for (e.g., QLabel, QLineEdit).
    - property_name: Name of the property to modify (e.g., "enabled", "visible").
    - property_value: Value to set for the property.
    - name_filter: Optional substring to filter widget names.
    
    Examples:
    adjust_widget_properties(self, QLineEdit, "enabled", False, name_filter="config")
    &&
    adjust_widget_properties(self, QLabel, "visible", False)
    """
    widgets = self.findChildren(widget_type)
    for widget in widgets:
        if name_filter is None or name_filter in widget.objectName():
            print(f"Setting {property_name} for {widget.objectName()} to {property_value}")
            widget.setProperty(property_name, property_value)

def align_widgets(self, widget_type, alignment, name_filter=None):
    """
    Align widgets dynamically based on their type and optional name filter.

    Parameters:
    - self: Parent widget.
    - widget_type: Type of widget to align (e.g., QLabel, QPushButton).
    - alignment: Qt.AlignmentFlag (e.g., Qt.AlignCenter, Qt.AlignRight).
    - name_filter: Optional substring to filter widget names.
    
    Examples:
    align_widgets(self, QLabel, Qt.AlignCenter)
    """
    #from PyQt5.QtCore import Qt  # Or PySide2/PySide6 if applicable
    
    widgets = self.findChildren(widget_type)
    for widget in widgets:
        if name_filter is None or name_filter in widget.objectName():
            print(f"Aligning {widget_type.__name__}: {widget.objectName()} to {alignment}")
            widget.setAlignment(alignment)

def set_placeholder_text(self, widget_type, placeholder_text, name_filter=None):
    """
    Set placeholder text for input widgets like QLineEdit or QTextEdit.

    Parameters:
    - self: Parent widget.
    - widget_type: Input widget type (e.g., QLineEdit, QTextEdit).
    - placeholder_text: Text to set as placeholder.
    - name_filter: Optional substring to filter widget names.
    
    Examples:
    set_placeholder_text(self, QLineEdit, "Enter your username", name_filter="user")
    """
    widgets = self.findChildren(widget_type)
    for widget in widgets:
        if name_filter is None or name_filter in widget.objectName():
            print(f"Setting placeholder for {widget.objectName()}: {placeholder_text}")
            widget.setPlaceholderText(placeholder_text)

def update_widget_text(self, widget_type, text_function, name_filter=None):
    """
    Update the text of widgets dynamically using a provided function.

    Parameters:
    - self: Parent widget.
    - widget_type: Type of widget to update (e.g., QLabel, QPushButton).
    - text_function: Function to generate text, takes the widget object as input.
    - name_filter: Optional substring to filter widget names.
    
    Examples:
    update_widget_text(self, QLabel, lambda widget: f"Label: {widget.objectName()}", name_filter="info")
    """
    widgets = self.findChildren(widget_type)
    for widget in widgets:
        if name_filter is None or name_filter in widget.objectName():
            new_text = text_function(widget)
            print(f"Updating text for {widget.objectName()}: {new_text}")
            widget.setText(new_text)

def batch_resize_widgets(self, widget_type, width, height, name_filter=None):
    """
    Resize widgets or set their minimum size in batch.

    Parameters:
    - self: Parent widget.
    - widget_type: Type of widget to resize (e.g., QLabel, QPushButton).
    - width: Desired width.
    - height: Desired height.
    - name_filter: Optional substring to filter widget names.
    
    Examples:
    batch_resize_widgets(self, QPushButton, 100, 50, name_filter="nav")
    """
    widgets = self.findChildren(widget_type)
    for widget in widgets:
        if name_filter is None or name_filter in widget.objectName():
            print(f"Resizing {widget.objectName()} to ({width}, {height})")
            widget.setMinimumSize(width, height)

def group_widgets_into_layout(self, widget_type, layout, name_filter=None):
    """
    Add specific widgets to a layout dynamically.

    Parameters:
    - self: Parent widget.
    - widget_type: Type of widget to group (e.g., QLabel, QLineEdit).
    - layout: Target layout (e.g., QVBoxLayout, QGridLayout).
    - name_filter: Optional substring to filter widget names.
    
    Examples:
    group_widgets_into_layout(self, QLabel, self.verticalLayout, name_filter="info")
    """
    widgets = self.findChildren(widget_type)
    for widget in widgets:
        if name_filter is None or name_filter in widget.objectName():
            print(f"Adding {widget.objectName()} to layout")
            layout.addWidget(widget)

