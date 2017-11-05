#programming assignment 1

def large_int_multiply(int_one, int_two):

	if int_one < 10 and int_two < 10:
		return int_one * int_one
	else:

		b1 = len(str(int_one))
		if b1 < 5:
			base1 = int((b1 / 2) ) -1
		else:
			base1 = int((b1 / 2) )

		b2 = len(str(int_two))
		if b2 < 5:
			base2 = int((b2 / 2) ) -1
		else:
			base2 = int((b2 / 2) )

		trailing1 = int(str(int_one)[int(base1):])
		trailing2 = int(str(int_two)[int(base2):])


		leading1 = int(str(int_one)[:int(base1)])
		leading2 = int(str(int_two)[:int(base2)])

		#now need to split leading into base case and front values

		bb1 = "1"

		for i in range(0,len(str(trailing1))):
			 bb1 = bb1 + str(0)

		bb1 = int(bb1)
		

		bb2 = "1"

		for i in range(0,len(str(trailing2))):
			 bb2= bb2 + str(0)

		bb2 = int(bb2)
		


		z2 = leading1 * leading2
		z0 = trailing1 * trailing2
		z1 = ( (leading1 + trailing1) * (leading2 + trailing2 ) ) -z2 - z0

		result = (z2 * (bb1 ** 2)) + (z1 * bb2) + z0
		
		return print(result)

		#print(str(z2) + " " + str(z0) + " " + str(z1) )


#testing outputs

#		return print(
#			str(trailing1) + " " + str(trailing2) + " " + 
#			str(leading1) + " " + str(leading2) + " " + 
#			str(bb1) + " " + str(bb2) + " " + str(front1) + " " 
#			+ str(front2)
#			)



print(large_int_multiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))

85397342226735670654635508695  667885680579578730042991771637944  067743044893204848617875072216249073013374895871952806582723184
85397342226735670654635508695 46574495034888535765114961879601127 067743044893204848617875072216249073013374895871952806582723184
