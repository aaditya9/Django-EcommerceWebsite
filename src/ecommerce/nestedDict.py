def findVal(data,path):
	for i in path:
		if i not in data.keys():
			return None
	
		else:
			c = path[0]
			if c in data.keys():
				temp_data = data[i]
			elif:

			else:
				return None	 

data={'foo':{'brr':3,'a':1},'joo':{'abc':1,'x':'xyz'}}
inp=['foo','brr','c']
result = findVal(data,inp)
print(result)