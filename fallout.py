##! /usr/bin/env python
import fallout_login as login
import fallout_boot as boot
import fallout_locked as locked
import fallout_hack as hack
import fallout_selection as select
import sys
import os
import signal

def signal_handler(sig, frame):
    """
    Handle the interrupt signal and reboot the system.
    """
    print('Interrupt received, rebooting the system...')
    os.system('reboot')

signal.signal(signal.SIGINT, signal_handler)

hard = len(sys.argv) == 2 and sys.argv[1].lower() == 'hard'

try:
    if boot.beginBoot(hard):
        pwd = hack.beginLogin()
        if pwd != None:
            login.beginLogin(hard, 'ADMIN', pwd)
            print(select.beginSelection())
        else:
            locked.beginLocked()
            print('Login failed')

except KeyboardInterrupt:
    print('Interrupt received, performing cleanup...')
    # Perform any necessary cleanup here
    print('Rebooting the system...')
    os.system('reboot')
