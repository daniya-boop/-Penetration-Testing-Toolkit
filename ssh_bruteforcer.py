import socket
import time

class SSHBruteForcer:
    def __init__(self, host, userlist, passlist, port=22):
        self.host = host
        self.userlist = userlist
        self.passlist = passlist
        self.port = port
        
    def check_ssh_open(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((self.host, self.port))
            s.close()
            return True
        except:
            print(f"[-] SSH port {self.port} is not accessible on {self.host}")
            return False
            
    def run(self):
        if not self.check_ssh_open():
            return
            
        print(f"[*] Starting SSH brute force simulation against {self.host}")
        
        with open(self.userlist) as users:
            user_lines = users.read().splitlines()
        with open(self.passlist) as passes:
            pass_lines = passes.read().splitlines()
            
        for user in user_lines:
            for password in pass_lines:
                print(f"[*] Trying: {user}:{password}")
                time.sleep(0.2)
        print("[-] No valid credentials found (simulation).")
