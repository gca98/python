from os import system
def clear():
    system('cls')
def kelvinToC (suhu,satuan):
    "Kelvin to Celcius"
    if satuan=="Kelvin":
        return suhu-273.15
    else:
        return suhu
def cToKelvin (suhu,satuan):
    "Celcius to Kelvin"
    if satuan=="Celcius":
        return suhu+273.15
    else:
        return suhu
def toFahrenheit (suhu,satuan):
    "to Fahrenheit"
    if satuan=="Kelvin":
        
        suhu = kelvinToC(suhu,satuan)
        satuan = "Celcius"
        return (suhu*9/5)+32
    elif satuan=="Celcius":
        return (suhu*9/5)+32
    else:
        return suhu

def fromFahrenheit (suhu,satuan):
    "from Fahrenheit"
    if satuan=="Kelvin":
        suhu  = (suhu - 32) * 5/9
        return suhu+273.15
    elif satuan=="Celcius":
        suhu  = (suhu - 32) * 5/9
        satuan = "Celcius"
        return suhu
    else:
        return suhu

satuan = "Celcius"
suhu = input("Suhu Celcius: ")
# print("suhu awal:",suhu)
# print()

menu = {}
menu['0']="Exit"
menu['1']="Celcius to Kelvin" 
menu['2']="Kelvin to Celcius"
menu['3']="to Fahrenheit"
menu['4']="Fahrenheit to Celcius "
menu['5']="Fahrenheit to Kelvin"
while True: 
  clear()
  options=menu.keys()
  print("suhu Celcius:",suhu , satuan)
  print("===Menu===")
  for entry in options: 
      print (entry, menu[entry])
  selection=input("Please Select:") 
  if selection =='1': 
      if satuan == 'Celcius':
          suhu = cToKelvin(float(suhu),satuan)
          satuan = "Kelvin"
          print(suhu)
          print(cToKelvin.__doc__)
  elif selection == '2': 
      if satuan == 'Kelvin':
          suhu = kelvinToC(float(suhu),satuan)
          satuan="Celcius"
          print(suhu)
          print(kelvinToC.__doc__)
  elif selection == '3':
      suhu = toFahrenheit(float(suhu),satuan)
      satuan="Fahrenheit"
      print(suhu)
      print(toFahrenheit.__doc__)
  elif selection == '4':
      if satuan == 'Fahrenheit':
           satuan="Celcius"
           suhu = fromFahrenheit(float(suhu),satuan)
           print(suhu)
           print(fromFahrenheit.__doc__)
  elif selection == '5':
      if satuan == 'Fahrenheit':
          satuan="Kelvin"
          suhu = fromFahrenheit(float(suhu),satuan)
          print(suhu)
          print(fromFahrenheit.__doc__)
  elif selection == '0': 
      break
  else: 
      print ("Unknown Option")
  input("Press enter to continue")