import os
import psutil
import time

# Function to get human readable memory string
def readable_size(size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    while size >= 1024 and i < len(units)-1:
        size /= 1024
        i += 1
    return f"{size:.2f} {units[i]}"

mem = os.urandom(1024*1024*1024)
try:
    while True:
        # Allocate 1 GB of memory
        mem += os.urandom(1024*1024*1024)

        # Get current resident memory usage
        mem_usage = psutil.Process().memory_info().rss

        # Print allocated memory in human readable format
        print(f"Allocated: {readable_size(mem_usage)}")

        # Sleep for 1 second
        time.sleep(1)
except MemoryError:
    print("Out of memory!")
