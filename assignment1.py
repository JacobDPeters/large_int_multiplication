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
