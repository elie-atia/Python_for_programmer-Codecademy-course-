def greet_someone():
   name = input('What is your name?')
   hometown = input('And where are you from?')
   print('Very nice to meet you, {}!'.format(name), f'from {hometown}!')
 

if __name__ == "__main__":
    greet_someone()