import psutil
print("cpu%", psutil.cpu_percent(1))
print("mem%", psutil.virtual_memory().percent)
print("disk%", psutil.disk_usage("/").percent)
