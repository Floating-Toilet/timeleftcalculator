# timeleftcalculator
A simple Python script to find how much time is left based on a schedule (School, Work, Event)

## Usage
Run ```python timeleft.py``` in your terminal, although you will need to rerun the script to update the current block
## Configuration
Change lines ```14, 16, 38,``` and ```38``` to fit your schedule
```
timeEndOne = datetime.combine(datetime.today(), time(XX, XX, XX)) # CHANGE ME

timeEndTwo = datetime.combine(datetime.today(), time(XX, XX, XX)) # CHANGE ME

...

if current_time < timeEndOne: # CHANGE ME
	print("It's before time end one\n")
	current_blk = timeEndOne
	time_remaining()
elif current_time < timeEndTwo: # CHANGE ME
	print("It's before time end one\n")
	current_blk = timeEndTwo
	time_remaining()
# Feel free to add more as needed

```
