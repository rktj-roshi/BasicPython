text = """

How I want a drink, alcoholic of course, after the heavy 
chapters involving 
quantum mechanics. 
All of thy geometry, Herr Planck, is fairly hard.

"""

# TODO

import re
sp=[s for s in re.split('[ ,.\n]',text)if s]

number=list(map(len,sp))

result= ''.join(str(num) for num in number)

print(result)