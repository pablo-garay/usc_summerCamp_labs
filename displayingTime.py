import sys
from math import floor

if (len(sys.argv) != 2):
    print("""Usage: Provide an integer argument corresponding to the number of seconds you want to convert to
          the format (hours, minutes, seconds).
          You should provide one and only one numeric command-line parameter""")
else:
    num_seconds = int(sys.argv[1])
    print("%d seconds = %d hours, %d minutes, %d seconds"
          %(num_seconds,
            floor(num_seconds / 3600),
            floor((num_seconds % 3600) / 60),
            floor((num_seconds % 3600) % 60) )
          )