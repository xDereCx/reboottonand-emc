# -*- coding: utf-8 -*-
# check for script and reboot to nand if present
import xbmc
import os
import subprocess

nandscript = '/usr/sbin/rebootfromnand'
if os.path.exists(nandscript):
    xbmc.executebuiltin('Notification(Rebooting, to android)')
    subprocess.call('/usr/sbin/rebootfromnand')
    xbmc.sleep(300)
    xbmc.executebuiltin('Reboot')
else:
    xbmc.executebuiltin('Notification(rebootfromnand, not available)')
exit()