import sys
import time

for i in range(101):
    sys.stdout.write("Progress: %d%% \r" % (i))
    sys.stdout.flush()
    time.sleep(0.1)