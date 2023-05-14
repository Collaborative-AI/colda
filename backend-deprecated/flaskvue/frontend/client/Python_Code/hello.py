# import sys
# print('Hello from Python!')
# sys.stdout.flush()

import sys
for i in range(len(sys.argv)):
    print('arg'+str(i),sys.argv[i])