A = [1, 30, "text", True, 30, 100, False]
print(f"List A: {A}")
B = set(A)
print(f"Tuple B: {B}")
C = {True, 30, "text", 1, 30, 100, False}
print(f"Tuple C: {C}")
print(f"equivalents of tuples : {B==C}")
print(f"element 1 in tuple C: {1 in C}")

print(len(C))
D = B.copy()
print(D)

