import os
import sys

LICENCE_DISLAIMER = """
{}  Copyright (C) 2016-2018 Lars Klitzke, lars@klitzke-web.de

This program comes with ABSOLUTELY NO WARRANTY; for details type --help.
This is free software, and you are welcome to redistribute it
under certain conditions; --help for details.
""".format(os.path.basename(sys.argv[0]))

print(LICENCE_DISLAIMER)