from pynfc import Nfc, Desfire, Timeout

n = Nfc("pn532_uart:/dev/ttyS0:115200")


class Rfid:
    def read_uid532(self):
        for target in n.poll():
            try:
                targetaid = target.uid.decode("ascii").upper()
                return targetaid
            except TimeoutException:
                pass
        
        
if __name__ == "__main__":
     rf = Rfid()
     uid = rf.read_uid532()
     print(uid)
    

