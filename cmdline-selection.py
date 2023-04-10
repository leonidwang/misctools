from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.shortcuts import checkboxlist_dialog

"""
This script uses the prompt_toolkit library to allow the user to interactively select strings from a list using a radio list or a checkbox list. 

Functions:
- select_from_radiolist(strings): 
    Prompts the user to select a single string from a list using a radio list. Returns the selected string.

- select_from_checkboxlist(strings): 
    Prompts the user to select one or more strings from a list using a checkbox list. Returns a list of selected strings.
"""

def select_from_radiolist(strings):
    # Use radiolist_dialog from prompt_toolkit to let the user select lines interactively
    selected_strings = radiolist_dialog(
        values=[(string, string) for string in strings],
        title='Select strings',
        text='Press space to select a line',
    ).run()

    # Return the selected string
    return selected_strings

def select_from_checkboxlist(strings):
    # Use checkboxlist_dialog from prompt_toolkit to let the user select lines interactively
    selected_strings = checkboxlist_dialog(
        values=[(string, string) for string in strings],
        title='Select strings',
        text='Press space to select/un-select a line',
    ).run()

    # Return the selected strings in a list
    return [string for string in selected_strings]

strings_radiolist = ['foo', 'bar', 'baz', 'qux']
strings_checkbox = ['foo1', 'bar1', 'baz1', 'qux1']
selected_strings_radio = select_from_radiolist(strings_radiolist)
selected_strings_checkbox = select_from_checkboxlist(strings_checkbox)
if selected_strings_radio:
    print(f"Selected from radio list: {selected_strings_radio}")
if select_from_checkboxlist:
    print(f"Selected from checkbox list: {' '.join(selected_strings_checkbox)}")
