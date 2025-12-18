import subprocess, sys
svc="nginx"
ok = subprocess.run(["systemctl","is-active","--quiet",svc]).returncode==0
if not ok:
    subprocess.run(["sudo","systemctl","restart",svc], check=False)
    print("restarted", svc); sys.exit(1)
print("ok", svc)
