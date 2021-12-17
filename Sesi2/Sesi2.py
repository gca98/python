if 'bar' in ['bar', 'baz','qux']:
    print('ada bar')
if 'foo' in ['bar', 'baz','qux']:
    print('ada foo')   

a = "abc"

if "a" in a and "b" in a:
    print("ada")


raining =True
print("Let's go to the","beach" if not raining else 'library')

print()


total_purchase = 1000
if a in 'bar':
    print('foo')
elif total_purchase > 850:
    print('Discount 30%')
elif 1/0:
    print('this wont\'t happen')
elif var:
    print('this wont\'t either')

print()
n = 5
while n > 0:    
    n -= 1    
    if n == 2:        
        break 
    print(n)
print('Loop ended.')
print()
n = 5
while n > 0 :    
    n -= 1    
    if n == 2:        
        continue    
    print(n)
print('Loop ended.')
print()

a = ['foo', 'bar']
while len(a):    
    print(a.pop(0))    
    b = ['baz', 'qux']    
while len(b):        
    print('>', b.pop(0))
print()

