

brojevi = ["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
           "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33",
           "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"]

print("Original List : " , brojevi) 

broj = []

broj = input(str("Insert numbers from 1 to 50: "))


brojevi = [ele for ele in brojevi if ele not in broj] 
  
# printing modified list 
print("New list after removing unwanted numbers: ", brojevi) 


