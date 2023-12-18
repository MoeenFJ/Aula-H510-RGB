import usb.core
import usb.util
import sys




def detachDevice(device):

    if device.is_kernel_driver_active(1):
        try:
            device.detach_kernel_driver(1)
        except usb.core.USBError as e:
            sys.exit("Could not detach kernel driver: %s" % str(e))

def attachDevice(device):
    
    if not device.is_kernel_driver_active(1):
        try:
            usb.util.release_interface(device, 1)
            device.attach_kernel_driver(1)
        except usb.core.USBError as e:
            sys.exit("Could not detach kernel driver: %s" % str(e))

def setColor(device,color):

    detachDevice(device)

    packet1 = "\x05\x11\x00\x00\x00\x00"
    res = device.ctrl_transfer(0x21, 0x09, 0x0305, 1, packet1)


    #Get current config
    res = device.ctrl_transfer(0xa1, 0x01, 0x0304, 1, 520)


    #New config
    res[3] = 0x7b

    #DPI Colors (Mouse wheel and logo)
    for i in range(6):
        res[29+i*3] = color[0] #R
        res[30+i*3] = color[1] #G
        res[31+i*3] = color[2] #B

    #Ring Color
    res[57] = color[0] #R
    res[58] = color[1] #G
    res[59] = color[2] #B

    #Append zeros to reach the size of 520 bytes
    for i in range(520-len(res)):
        res.append(0x00)

    #Send Req
    device.ctrl_transfer(0x21, 0x09, 0x0304, 1, res)

    attachDevice(device)

if __name__ == "__main__":
    color = sys.argv[1]

    if len(color) != 6:
        print("Enter 6 digit hex color like ff06f8")
        exit()

    device = usb.core.find(idVendor=0x258a, idProduct=0x0029)
    if device is None:
        print('Device not found')
        exit()
        
    
    color = (int(color[0:2],16),int(color[2:4],16),int(color[4:6],16))
    setColor(device,color)

