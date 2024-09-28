serialdata = ""
serial.redirect(SerialPin.USB_RX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)

def on_forever():
    global serialdata
    if serialdata == "0":
        basic.show_number(0)
    elif serialdata == "1":
        basic.show_number(1)
    else:
        basic.show_icon(IconNames.HAPPY)
    serialdata = serial.read_line()
basic.forever(on_forever)
