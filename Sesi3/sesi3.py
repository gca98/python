def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)


def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

my_function(5,3)
print(my_function.__doc__)


def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("\nValues inside the function : ", mylist)
   return mylist

# Now you can call changeme function
mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme( mylist )
print("\nValues outside the function - after  : ", mylist)


def penjumlahan(a=1,b=1,c=1):
    return a+b+c


print("\n",penjumlahan())

def savedata(name,age):
    print(f"nama :{name}")
    print(f"age :{age}")

savedata('adi',20)

savedata( age=4, name="a" )

def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

import sys
sys.path.append(r'Sesi3/a')
import person
# person

person.display('Good Morning')

print(person.name)