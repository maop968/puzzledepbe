from pynfc import Nfc
n = Nfc("pn532_uart:/dev/ttyS0:115200")
class Rfid:
    def __init__(self):
        n = Nfc("pn532_uart:/dev/ttyS0:115200")

    def read_uid532(self):
        for target in n.poll():
            try:               
                targetaid = target.uid.decode("ascii").upper()
                return targetaid
            except:
                pass
        
        
if __name__ == "__main__":
     rf = Rfid()
     uid = rf.read_uid532()
     print(uid)
    

