#!c:\users\katrii~1.wal\appdata\roaming\micros~1\windows\startm~1\programs\python~1.7\mysite\mysite\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django','console_scripts','django-admin'
__requires__ = 'Django'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django', 'console_scripts', 'django-admin')()
    )
