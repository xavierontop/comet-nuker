import threading, queue, random, os, sys, time
from pystyle import Colors, Colorate
from requests_futures.sessions import FuturesSession

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.005)

slow_write("\u001b[38;5;159m-> Insert Token; ")
token = input()
slow_write("\u001b[38;5;159m-> Insert Guild ID; ")
guild = input()

headers = {"Authorization": f"Bot {token}"}

q = queue.Queue()

def requestsender():
    try:
        while True:
            req, url, headers = q.get()
            s = req(url, headers=headers).result()
            print(s.text)
            q.task_done()
    except Exception:
        pass
    

def massban_worker():   
    session = FuturesSession()
    for x in open("users.txt"):
        q.put((session.put, f"https://discord.com/api/v{random.randint(6, 9)}/guilds/{guild}/bans/{x}", headers))
    q.join()

logo = """
\t\t\t\t\t\t  /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$$
\t\t\t\t\t\t /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/|__  $$__/
\t\t\t\t\t\t| $$  \__/| $$  \ $$| $$$$  /$$$$| $$         | $$   
\t\t\t\t\t\t| $$      | $$  | $$| $$ $$/$$ $$| $$$$$      | $$   
\t\t\t\t\t\t| $$      | $$  | $$| $$  $$$| $$| $$__/      | $$   
\t\t\t\t\t\t| $$    $$| $$  | $$| $$\  $ | $$| $$         | $$   
\t\t\t\t\t\t|  $$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$$   | $$   
\t\t\t\t\t\t \______/  \______/ |__/     |__/|________/   |__/                                                                                                         
"""

if __name__ == "__main__":
    os.system("cls; clear && title Comet Nuker - Slowest Mass Ban Tool")
    for x in range(100):
        threading.Thread(target=requestsender, daemon=True).start() 
    os.system("cls; clear")
    print(Colorate.Vertical(Colors.cyan_to_blue, logo, 1))    
    print()
    slow_write("\t\t\t\t\t\u001b[38;5;159mPress Enter To Start; "); input()
    massban_worker()