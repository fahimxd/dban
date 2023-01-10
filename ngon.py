import os
import threading
def ngrok():
    os.system('./ngrok tcp 9999 --log=stdout > port')
thread1 = threading.Thread(target=ngrok)
thread1.start()

