let serialdata = ""
serial.redirect(
SerialPin.USB_RX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
basic.forever(function () {
    if (serialdata == "0") {
        basic.showNumber(0)
    } else if (serialdata == "1") {
        basic.showNumber(1)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    serialdata = serial.readLine()
})
