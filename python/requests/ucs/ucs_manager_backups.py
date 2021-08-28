from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils.ucsbackup import backup_ucs

handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")
backup_ucs(handle,"config-all","/home/nmiles","config-all.xml")