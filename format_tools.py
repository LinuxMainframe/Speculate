#import libraries in main file, not here. The libaries used depend on what the makeup of your Qt application

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


