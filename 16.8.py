'''
16.8
English Int: Given an integer, print an  English phrase that describes the integer 
(e.g. One Thousand Two Hundred Thirty Four)
'''

teens = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
		15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

digits = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
		  6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}

tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 
		7: "Seventy", 8: "Eighty", 9: "Ninety"}

def english_int(num):
	sign = ""
	if num < 0:
		sign += "Negative "

	num = abs(num)
	if num in digits:
		return sign + digits[num]
	if num in teens:
		return sign + teens[num]
	if num in tens:
		return sign + tens[num]

	num = str(num)
	result = sign
	if len(num) == 4:
		result += digits[int(num[0])] + " Thousand "
		num = num[1:]

	if int(num[0]) == 0:
		num = num[1:]

	if len(num) == 3:
		result += digits[int(num[0])] + " Hundred " 
		num = num[1:]

	if int(num[0]) == 0:
		num = num[1:]

	if len(num) == 2:
		if int(num) in teens:
			result += teens[0]
		else:
			result += tens[int(num[0])] + " " + digits[int(num[1])]
		num = num[2:]	

	if len(num) == 1:
		result += digits[int(num[0])]

	return result

lst = [1123, 1024, 139, 108, 27, 9]
for num in lst:
	print(english_int(num))
