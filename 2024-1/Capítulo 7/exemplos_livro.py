names = ["ana", "beatriz", "carla", "daiana"]
 
for name in names:
    name = name.upper()
 
print(names)
 
for i in range(len(names)):
    names[i] = names[i].upper()
 
print(names)
 
for i, v in enumerate(names):
    names[i] = v.lower()
 
print(names)