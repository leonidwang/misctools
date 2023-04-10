# misctools
Collection of random handy tools.

## cmdline-selection.py
This script uses the prompt_toolkit library to allow the user to interactively select strings from a list using a radio list or a checkbox list. 
Functions:
- select_from_radiolist(strings): 
    Prompts the user to select a single string from a list using a radio list. Returns the selected string.

- select_from_checkboxlist(strings): 
    Prompts the user to select one or more strings from a list using a checkbox list. Returns a list of selected strings.

## ping-network.py
Python script to ping all IPs in a range and report result(up/down) in a table.
- Ping each IP 3 times.
- 0 packet loss means it's up, otherwise it's down.
- multiprocess is used to do it in parallel.
