classes = [
    {'school_class': '4a', 'scores': [4, 5, 5, 2, 3, 4, 5, 5, 4, 4]},
    {'school_class': '4b', 'scores': [3, 5, 4, 2, 3, 4, 5, 4, 4, 1]},
    {'school_class': '4c', 'scores': [5, 5, 3, 2, 3, 4, 2, 5, 4, 4]},
    {'school_class': '4d', 'scores': [4, 5, 3, 2, 3, 4, 3, 5, 2, 4]}
]

school_average_score = 0

for s_class in classes:
    s_class["average_score"] = sum(s_class['scores'])/len(s_class['scores'])

    school_average_score += sum(s_class['scores'])/len(s_class['scores'])
#print(classes)

print(f"School average score: {school_average_score/len(classes)}")

for s_class in classes:
    print(f"Class {s_class['school_class']} average score {s_class['average_score']}")
