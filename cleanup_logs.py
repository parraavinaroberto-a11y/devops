from pathlib import Path
import time, os
root=Path("/var/log/myapp"); days=7
cut=time.time()-days*86400
for p in root.rglob("*.log"):
    if p.stat().st_mtime < cut:
        p.unlink(missing_ok=True); print("deleted", p)
