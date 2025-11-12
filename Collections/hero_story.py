story1 = {
    "start": "Sam found a cave",
    "middle": "Sam explored the cave",
    "end": "Sam found treasure!"}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())

print(story1["start"])
print(story1["middle"])
print(story1["end"])

story1["character"] = "Sam"

print(f"The end. I hope you enjoyed the story about {story1["character"]}")