# Aula-H510-RGB
A simple python script to control RGB on Aula H510 mouse

Depends on ```pyUSB``` install it using:
```
pip install pyUSB
```

Run using:
```
#color should be a hex RGB value without the # like ff067b
python3 AulaSetColor.py <color>
```

If you are on linux you might get ```USBError: [Errno 13] Access denied (insufficient permissions)``` to fix this either run the script as ```sudo``` or give access to current user using the following command: 
```
sudo nano /etc/udev/rules.d/99-aula.rules
```
and enter the following lines to the file :
```
SUBSYSTEMS=="usb", ATTRS{idVendor}=="258a", ATTRS{idProduct}=="0029", TAG+="uaccess"

# allow r/w access by users of the plugdev group
SUBSYSTEMS=="usb", ATTRS{idVendor}=="258a", ATTRS{idProduct}=="0029", GROUP="plugdev", MODE="0660"

# allow r/w access by all users
SUBSYSTEMS=="usb", ATTRS{idVendor}=="258a", ATTRS{idProduct}=="0029", MODE="0660"
```
and make sure your user is in ```plugdev``` group using:
```
sudo usermod -a -G plugdev [your user name]
```
