Fallout Terminal
================

Forked version of (https://github.com/brunobraga/termsaver) configured for my raspberry pi 1. With the added exit.sh script that takes options and executes corresponding commands on the system afterwards. 

WARNING: This script reboots your system when you exceed your attempts or when a KeyboardInterrupt is detected!

Usage
================

```
python fallout.py
```

The following line can be added to your .bashrc to make the script run every time you start a shell:

```
python3 /path/to/fallout.py && cat /tmp/selection_output.txt | /path/to/exit.sh
```

Passwords
================

To add your own lists of passwords, check out the passwords.txt file
