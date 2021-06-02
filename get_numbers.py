phone = []                                                      
with open ('numbers.txt') as numbers_file:                    
    for line in numbers_file:
    	line=line.strip()
    	if len (line)==10:								   		
    		phone.append(str(line))
