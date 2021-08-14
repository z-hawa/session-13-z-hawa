# Session 13 Generators and Iterator tools

# Returning a namedtuple of the parking tickets
This was achieved by using a generator function to open the file. The first line was skipped as it contained the field names.A for loop was initialised and every iterated line was sent to a namedtuple returning function. This function split the column by `,` and returned a namedtuple containing all the column values. This final namedtuple was then yielded by the base function thus creating a lazy iterator.

# Returning the dictionary of car make violations
This was achieved by using the first function as an iterator and then using the dict.get() method to use a dict to store the number of violations. The dictionary was pre initialised and used as a global variable. For each line iterated, the dictionary would be updated. 
```py
# Initialise the dictionary as an empty one
global dictionary
dictionary={}

# Get the number of violations if the carmake exists in the dictionary otherwise initialise it as a zero
count=dict.get(tickets.VehicleMake,0)

# Update the count in the dictionary with the vehicle carmake as the key.
dictionary.update({tickets.VehicleMake:count+1})
```