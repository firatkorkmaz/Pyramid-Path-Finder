# Let's Replace the Second Row with 2 Prime Numbers Which will Block All the Paths and See the Result

import os
import shutil

if os.path.isfile('./random_pyramid.txt'):
    shutil.copy('random_pyramid.txt', 'random_pyramid_blocked.txt')

    # 2 Prime Numbers for the 2nd Row to Shut All the Ways to the Bottom
    line_2 = "613 647"

    filename = "random_pyramid_blocked.txt"
    with open(filename, 'r+') as file:
        file.seek(5)        # Going to the Head of the 2nd Line
        file.write(line_2)  # Replace the Existing Row with "613 647"
    
    print("\nAll the Paths are Blocked in: random_pyramid_blocked.txt")
    
else:
    print("\nFile Not Found: random_pyramid.txt")
