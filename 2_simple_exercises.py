# 1) print out the value for the key 'history' using the dictionary below

sampleDict = {    
   "class":{
      "student":{          
         "name":"Mike",         
         "marks":{             
               "physics":70,            
               "history":80      
         }      
      }   
   }
}

print(sampleDict["class"]["student"]["marks"]["history"])

#2) Add two inches to the son's height.

dict = {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

dict["son's height"] = 34

print(dict)

#3)Given a Python dictionary, change Brad's salary to 8500

sampleDict1 = {'emp1': {'name': 'Jhon', 'salary': 7500},
               'emp2': {'name': 'Emma', 'salary': 8000},
               'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict1['emp3']['salary'] = 8500

print(sampleDict1)

#4)Given the dictionary below, add a new key - 'work' with the values shown below:
dict1 = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

dict1["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]

print(dict1)
