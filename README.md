Fallout Terminal
================

Forked version of (https://github.com/brunobraga/termsaver) configured for my raspberry pi 1. With the added exit.sh script that takes options and executes corresponding commands on the system afterwards. 

WARNING: This script reboots your system when you exceed your attempts or when a KeyboardInterrupt is detected!

Usage
================

```
python fallout.py
```

or for hard mode where the user must manually enter the correct input in the
boot and login scripts

```
python fallout.py hard
```

Passwords
================

To add your own lists of passwords, check out the passwords.txt file
