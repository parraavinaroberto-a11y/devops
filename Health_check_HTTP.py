import time, requests
url="https://example.com/health"
t=time.time()
r=requests.get(url, timeout=5)
print("status:", r.status_code, "ms:", int((time.time()-t)*1000))
r.raise_for_status()
