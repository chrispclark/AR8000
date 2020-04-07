#!/usr/bin/env python

class decode():
	def __init__(self,z): 
		self.z = z 
	def result(self):
		return self.z.split()















'''

class decode_responsea:
	def __init__(self,response):
		self.from_radio = response
	def result(self):
		response_length = len(from_radio)
		print "length" + response_length
		z=response.split()
		print "length" +" "+ str(len(z[0]))
		send_back_list = []
		print z[0]
		if z[0] == "SS":
			print "heer"
			mode = "Search Mode"
		elif z[0] == "SM":
			mode =  "Select Scan Mode"
		elif z[0] == "MS":
			mode =  "Scan Mode"
		elif z[0] == "MR":
			mode =  "Memo Channel Mode M.RE"
		elif z[0] == "VF":
			mode =  "2VFO Mode"
		elif z[0] == "DD":
			mode =  "VFO Mode"
		else:
			mode = "No Idea"
		return mode
		print mode
		send_back_list.append(mode)			
				
		print z[1]
		send_back_list.append(str(z[0])) # Frequency_response
		send_back_list.append(str(z[1]))  #sto_response
		send_back_list.append(str(z[2])) #au1_response
		send_back_list.append(str(z[3])) #md1_response
		send_back_list.append(str(z[4])) #AT_response
		send_back_list.append(str(z[5])) #TT_response
		return (send_back_list)
	'''

