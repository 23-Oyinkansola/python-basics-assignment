name="Hello Everyone"
age=45
price=4.678
running=True
fruit=["Apple","Orange","Watermelon"]

print(type(name))
print(type(age))
print(type(price))
print(type(running))
print(type(fruit))
print("\n")

#Task 2
user=int(input("Enter your age"))
if user > 18:
    print("You are eligble to vote")
else:
    print("You are not eligble to vote")
print("\n")

#Task 3
for i in range(0,10):
    print(i + 1)
print("\n")
count=1
while count <=20:
    print(count)
    count +=1
print("\n")

fruits=["Apple","Orange","Watermelon","Banana","Mango","Cherry"]
for fruit in fruits:
    if fruit == "Banana":
        continue
    print(fruit)