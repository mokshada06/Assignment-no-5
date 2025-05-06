#3 Task no 1

dict={'Alice':85, 'John':75, 'Dina':89}
name=input('Enter the students name :')
if name in dict:
    print(f"{name}'s marks: {dict[name]}")
else:
    print("Student not found")

Output :
Enter the students name : Alice
Alice's marks: 85

Enter the students name : Jiya
Student not found


#3 Task no 2

no=list(range(1,11))
no1=no[:5]
reverse_no=no1[::-1]

print('Original list :', no)
print('Extractes first five elements :', no1)
print('Reversed extracted elements :', reverse_no)

Output :
