"""
Concepts: Loops
Level: Beginner
"""

# Example 1: for loop
print("\nExample 1: for loop")
for i in range(5):
    print(".", i)
    if i == 3:
        break


# Example 2: for loop with steps
print("\nExample 2: for loop with steps")
for i in range(0, 10, 2):
    print(".", i)


# Example 3: while loop
print("\nExample 3: while loop")
counter = 0
while counter < 5:
    print(".", counter)
    counter += 1


# Example 4: while loop with else statement
print("\nExample 4: while loop with else statement")
counter = 0
while counter < 5:
    print(".", counter)
    counter += 1
else:
    print(". Loop is complete")


# Example 5: break statement
print("\nExample 5: break statement")
for i in range(5):
    print(".", i)
    if i == 3:
        break

# Example 6: continue statement
print("\nExample 6: continue statement")
for i in range(5):
    if i == 3:
        continue
    print(".", i)


# Example 7: pass statement
print("\nExample 7: pass statement")
for i in range(5):
    pass
    print(".", i) # This will never be printed


# Example 8: loop and conditional statement combined
print("\nExample 8: loop and conditional statement combined")
for i in range(0, 33):
    if i % 3 == 0:
        print(". Number divisible by 3:", i)
    else:
        continue