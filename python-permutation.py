from random import choices
import itertools
import time
import psutil
star = time.time()
my_list= ["a", "A","b","B", "c","C", "d","D", "e","E", "f","F", "g","G", "h","H" ,"i","I", "j","J", "k","K", "l","L", "m","M",
           "n","N", "o","O", "p","P", "q","Q", "r","R", "s","S", "t","T", "u","U", "v","V", "w","W", "x","X", "y","Y", "z","Z","0","1","2","3","4","5","6","7","8","9"]
my_string = ""
def tupl(tup):
     str = ''.join(tup)
     return str

# perm = itertools.product(my_list, repeat=5)
counter = 0
text_file = open("6689.txt", "w")
for permutes in itertools.product(my_list, repeat=2):
      my_string += tupl(permutes)
      counter += 1
      if counter  == 100000:
          print(my_string)
          text_file.write(my_string)
          my_string = ""
          counter = 0
      
text_file.write(my_string)
text_file.close()
print("It took", time.time()-star, "seconds")
print(psutil.cpu_percent())
print(psutil.virtual_memory())