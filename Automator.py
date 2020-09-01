###install pywhatkit
import pywhatkit as wkit

wkit.add_driver_path('D:\chromedriver.exe')
##Point to the location where you have your chromedriver.
wkit.load_QRcode()
###This will open up the QR code screen on whatsapp web.

kit.sendwhatmsg("SendersNumber","Text to Send","HH","MM")

##HH = Hour in 24 hour format i.e., between 0 and 23
## MM = Minutes i.e., between 0 and 59
##Add 7-8 minutes ahead of running of code for smooth execution,less time may lead to module throwing errors.
