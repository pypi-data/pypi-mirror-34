# Python-ADB-Tools

Installation
======
You can install this package via pip
`pip install python_adb_utils`

or

`pip3 install python_adb_utils`


Usage:
======

To use these tools you only need to import and create an instance of AdbUtils()

`from adb_utils import adb_utils as adb`

`adb.get_connected_devices()`

___

Available Methods
======

### **get_connected_devices()**
This method will return you a list of tuples having the device name and Android version for that specific version.

### **install_app(device=device_name, apk=path_to_apk)**
Installs an app to the chosen device.


### **unistall_app(device=device_name, package=package_name)**
Uninstalls an app


### **is_device_connected(device=device)**
Returns True if a device is connected.


### **is_app_installed(device=device_name, package=package_name)**
Check if an app is installed on a specific device.

### **unlock_device(device=device_name, password=password)**
Unlocks a device with the correct password. 