def say_message(message, num_times=1):
    for x in range(0, num_times):
        print(message)

say_message('once') # illustrates default parameters
say_message('twice', 2)
say_message('thrice', num_times=3) # illustrates named parameter