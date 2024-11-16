
from discounted import discounted

for number in range(3):
    print(f"Hello world {number}!")

print('')

example_string = "I study python programming language"
for word in example_string.split():
    print(f"Word lenth {word}: {len(word)}")

print('')

student_scores = [1, 21, 19, 6, 5]

print(f"Average score: {sum(student_scores)/len(student_scores)}")
print('')

for score in student_scores:
    print(score)

print('')

scores_sum = 0
for score in student_scores:
    scores_sum += score
    print(scores_sum)

print(f"Average score: {scores_sum/len(student_scores)}")

print('')

stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 1200, 'discount': 25},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 1000, 'discount': 10},
    {'name': '', 'stock': 18, 'price': 150, 'discount': 10}
]

for phone in stock:
    print(phone)
    phone["final_price"] = discounted(phone["price"], phone["discount"], name=phone["name"])
    print(phone)
    print("------")

print(stock)