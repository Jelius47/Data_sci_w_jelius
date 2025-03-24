import threading
import queue
import requests

# Create a queue object
q = queue.Queue()

# List to store valid proxies
valid_proxies = []

# Load proxies from file into the queue
with open("proxies.txt", "r") as f:
    proxies = f.read().strip().split("\n")
    for p in proxies:
        q.put(p)

def check_proxies():
    global q, valid_proxies
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy}, timeout=5)
            if res.status_code == 200:
                print(f"Valid proxy: {proxy}")
                valid_proxies.append(proxy)
        except Exception as e:
            print(f"Failed proxy: {proxy} - {e}")
        q.task_done()

# Start threads to check proxies
threads = []
for _ in range(8):
    t = threading.Thread(target=check_proxies)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# Save valid proxies to file
with open("valid_proxies.txt", "w") as f:
    f.write("\n".join(valid_proxies))

print(f"✅ Valid proxies saved to valid_proxies.txt")
