from datetime import datetime, time
import sys
import time as tim
import os; clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Python is a lot easier than I thought

current_time = datetime.now()
print("\nCurrent Time:", current_time.strftime("%Y-%m-%d %A %I:%M:%S %p"), "\n")

# Stored in Hour Minute Second. 24 Hour time.
# datetime.combine() Solves TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.datetime'

timeEndOne = datetime.combine(datetime.today(), time(8, 40, 0)) # CHANGE ME

timeEndTwo = datetime.combine(datetime.today(), time(20, 5, 0)) # CHANGE ME

def time_remaining():
	while True:

		# Get Delta
		current_time = datetime.now()
		delta = current_blk - current_time
		print(f"Time difference: {delta} \n")

		# Divide into a more understandable form
		total_seconds = int(delta.total_seconds())
		hours, remainder = divmod(total_seconds, 3600)
		minutes, seconds = divmod(remainder, 60)
		print(f"Time Left: {hours} hours, {minutes} minutes, {seconds} seconds\n")

		tim.sleep(1)
		clear()


# the large if/elif block works, ok?

if current_time < timeEndOne: # CHANGE ME
	print("It's before time end one\n")
	current_blk = timeEndOne
	time_remaining()
elif current_time < timeEndTwo: # CHANGE ME
	print("It's before time end one\n")
	current_blk = timeEndTwo
	time_remaining()
else:
	print("Its joever")
