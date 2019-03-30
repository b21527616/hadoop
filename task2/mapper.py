import sys

import os
file_name = os.getenv('map_input_file')
file_name = file_name.split("/")[-1]

arg = sys.argv[0]
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    count = line.count()
    for i in range(count):
        print "%s\t%s" % (file_name, 1)