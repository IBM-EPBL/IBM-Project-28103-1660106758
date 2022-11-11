import random as rand

print("welcome to Smart farming Application")
temperature = float(rand.uniform(15,50))
if(temperature>22 and temperature<40):
    humidity = int(rand.randint(45,65))
elif(temperature<22):
    humidity = int(rand.randint(60,70))
elif(temperature>40):
    humidity = int(rand.randint(25,35))
moisture = int(rand.randint(00,70))
print("temperature:",temperature,"C","\n","humidity:",humidity,"\n","moisture:",moisture)
if(temperature>35 or moisture<20 ):
    print("Irrigation required")
    print("activate irrigation ?")
    decision = input()
    if(decision == 'yes'):
        print("irrigation activated")
    else:
        print('irrigation not activated')
else:
    print("irrigation not required")
