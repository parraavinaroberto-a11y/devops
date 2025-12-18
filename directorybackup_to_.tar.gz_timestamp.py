import tarfile, time
src="/etc/myapp"
out=f"/backups/myapp_{time.strftime('%Y%m%d_%H%M%S')}.tar.gz"
with tarfile.open(out,"w:gz") as t:
    t.add(src, arcname="myapp")
print(out)
