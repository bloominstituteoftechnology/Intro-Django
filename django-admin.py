#!/Users/bradyfukumoto/.local/share/virtualenvs/Intro-Django-CS13-l7vZlwvX/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from django.core.management import execute_from_command_line
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(execute_from_command_line())

