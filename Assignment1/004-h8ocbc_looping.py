


numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949
  ]
# a = len(numbers)
# print(a)


# for
print("FOR")
for number in numbers:
    if number%2==0:
        print(number, end=' ')
    elif number == 237:
      print("Done")
      break
    else:
      continue
# While
print("======================================================")
print("WHILE")
i=0
while i < len(numbers):
  if numbers[i]%2==0:
    print(numbers[i], end=' ')
  elif numbers[i] == 237:
    print("Done")
    break

  i += 1