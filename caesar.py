import sys

try:
        global mode, dec, key

	keyw = sys.argv[1]
	key = sys.argv[2]
	mode = sys.argv[3]

	if mode == "-d":
        	dec = True

	elif mode == "-e":
        	dec = False

	else:
        	print "Invalid Operation"
        	exit(0)

	if key == "-a":
        	all = True

	else:
		all = False
        	key = int(key)
        	if key > 24:
        	        print 'Invalid Key'
	                exit(0)


except:
	print "Use: python",sys.argv[0]," <DATA> <KEY NUMBER> <OPERATION>\n\nKey number options:\n-a\tTry all keynumbers\n\nOperations:\n-d\tDecrypt data\n-e\tEncrypt data\n"
	exit(0)



print "\n"+"#"*len(keyw)+"########"+"\nKEY\tDATA\n"+"#"*len(keyw)+"########"
def run():

        sys.stderr.write("\n["+str(key)+"]\t")
	for i in keyw:
		if i == "a":
			alphabet = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		        old = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

			if dec == True:
				alphabet = []
				for i in range(24, 0, -1):
					alphabet.append(old[i])
		                alphabet.append(old[0])

		        count = 0
			for i in alphabet:
		                    count += 1
		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "b":
			alphabet = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]
		        old = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]

		        if dec == True:
		                alphabet = []
		                for i in range(24, 0, -1):
		                        alphabet.append(old[i])
		                alphabet.append(old[0])

			count = 0
			for i in alphabet:
				count += 1

				if key == count:
					sys.stderr.write(i)
		                        break


		elif i == "c":
		            alphabet = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b"]
		            old = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b"]


		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "d":
		            alphabet = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
		            old = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "e":
		            alphabet = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"]
		            old = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "f":
		            alphabet = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"]
		            old = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "g":
		            alphabet = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"]
		            old = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "h":
		            alphabet = ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g"]
		            old = ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "i":
		            alphabet = ["j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h"]
		            old = ["j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "j":
		            alphabet = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i"]
		            old = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "k":
		            alphabet = ["l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j"]
		            old = ["l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "l":
		            alphabet = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k"]
		            old = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "m":
		            alphabet = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l"]
		            old = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "n":
		            alphabet = ["o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
		            old = ["o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]


		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "o":
		            alphabet = ["p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
		            old = ["p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

			    count = 0
		            for i in alphabet:
		            	count += 1

		                if key == count:
		                    	sys.stderr.write(i)
		                        break


		elif i == "p":
		            alphabet = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
		            old = ["q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "q":
		            alphabet = ["r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
		            old = ["r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1
		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "r":
		            alphabet = ["s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
		            old = ["s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "s":
		            alphabet = ["t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
		            old = ["t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]


		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "t":
		            alphabet = ["u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
		            old = ["u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "u":
		            alphabet = ["v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
		            old = ["v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "v":
		            alphabet = ["w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]
		            old = ["w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "w":
		            alphabet = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]
		            old = ["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "x":
		            alphabet = ["y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
		            old = ["y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "y":
		            alphabet = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
		            old = ["z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]


		            if dec == True:
		                   alphabet = []
		                   for i in range(24, 0, -1):
		                   		alphabet.append(old[i])
		                   alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break

		elif i == "z":
		            alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
		            old = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]

		            if dec == True:
		                    alphabet = []
		                    for i in range(24, 0, -1):
		                            alphabet.append(old[i])
		                    alphabet.append(old[0])

		            count = 0
		            for i in alphabet:
		                    count += 1

		                    if key == count:
		                            sys.stderr.write(i)
		                            break
		elif i == " ":
			sys.stderr.write(" ")





if all == True:
	for i in range(1,25):
		key = i
		run()
	print "\n\n"

else:
	run()
	print "\n"
