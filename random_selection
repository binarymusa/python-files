# random selection n addition.computer selects 2 random numbers in a common list array
#and tests if the sum is equal to sum

import random

while True:
    def num():
       a,b = random.choice(list),random.choice(list)
       sum_tested = a + b

       if a + b != sum:
        print(f'{a},{b} = {sum_tested}') 
        #print(sum_tested)
        print('failed attempt')
       else:
        print(f'{a},{b} = {sum_tested}') 
        print('lucky guess') 

    sum = 8
    list = (4,4,2,1)
    num()

    play_again = input('play again: (yes/no)').lower()
    if play_again != 'yes':
      break
print('exiting......')
