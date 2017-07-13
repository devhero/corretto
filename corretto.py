def pyFix(coffee):
   return {'coffee': coffee['coffee']/2, 'alchool': coffee['coffee']/2}

coffee = {'coffee': 1}
corretto = pyFix(coffee)
print(corretto)