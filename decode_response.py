#!/usr/bin/env python

class decode():
	def __init__(self,z): 
		self.z = z 
	def result(self):
		g=self.z.split()
		return g
	
		'''
		
		if z[0] == "SS":
								print "heer"
								self.label_mode.setText("Search Mode")
				elif z[0] == "SM":
								self.label_mode.setText("Select Scan Mode")
				elif z[0] == "MS":
								self.label_mode.setText("Scan Mode")
				elif z[0] == "MR":
								self.label_mode.setText("Memo Channel Mode M.RE")
				elif z[0] == "VF":
								self.label_mode.setText("2VFO Mode")
				elif z[0] == "DD":
								self.label_mode.setText("VFO Mode")
				else:
								self.label_mode.setText("No Idea")
				
				print z[1]
				self.label_Frequency_response.setText(str(z[0]))
				print z[2]
				self.label_sto_response.setText(str(z[1]))
				print z[3]
				self.label_au1_response.setText(str(z[2]))
				print z[4]
				self.label_md1_response.setText(str(z[3]))
				print z[5]
				self.label_AT_response.setText(str(z[4]))
				print z[6]
				self.label_TT_response.setText(str(z[5]))
				
				print "-----"
				print z[0]
				print z[1]
				print z[2]
				if response_length== 0:
								response = "Failed - Is the AR8000 Turned on. Is the serial cable connected ?"
		
		
		
		
		dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'} 
		return (dict) 
	#return "here i am " + "".join(self.z)

'''















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

