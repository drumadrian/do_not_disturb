import time
import sys


DEFAULT_PERSON = "Someone IMPORTANT"

try:
	if len(sys.argv) != 0:
		person = sys.argv[1]
except IndexError as e:
	person = DEFAULT_PERSON


def main():

	x = 1
	while True:
		if x == 1:
			print  " " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " + "Do NOT Distub Please, holding for {}".format(person)
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			time.sleep(.6)
			x = 0
		else:
			print  " " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " 
			print  "\n ######### " + "Do NOT Distub, holding for {}".format(person)
			print  "\n ######### " 
			print  "\n ######### " 
			time.sleep(.4)
			x = 1




# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()

