immutable_var = 1, "one", True
print(immutable_var)

#immutable_var[2] = False
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
#основа кортежа - НЕИЗМЕНЯЕМОСТЬ.

mutable_list = ["pen","pencil","ruler"]

mutable_list[2] = "eraser"
print(mutable_list)