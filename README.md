# Automatic-configuration-of-IP-address-and-proxy-

# Network Configuration Tools

This repository contains Python scripts for configuring network settings and proxy server.

## console_network_configurator.py

This script provides a command-line interface for configuring network settings such as IP address, subnet mask, default gateway, and DNS servers. It utilizes the `wmi` and `winreg` modules to interact with the Windows Management Instrumentation (WMI) and Windows Registry, respectively.

### Usage

To use this script, simply execute it using a Python interpreter. Make sure to run it with administrative privileges.

```
python console_network_configurator.py
```

# GUI_network_configurator.py

This script offers a graphical user interface (GUI) for configuring network settings (The GUI only has an IP setting) and a proxy server. It uses tkinter, wmi and winreg modules to create a graphical interface and interact with system components.

## Usage

To launch the GUI, execute the script using a Python interpreter.

```
python GUI_network_configurator.py
```

Requirements
  - Python 3.x
  - wmi module (install via pip install wmi)
  - tkinter module (should be included in standard Python distribution)
