will = ["will", 28, ["Python", "c#", "JavaScript"]]
wilber = will
print(id(will))
print(will)
print([id(ele for ele in will)])
print(id(wilber))
print(wilber)
print([id(ele for ele in wilber)])

will[0] = "Wilber"
will[2].append("CSS")
print(id(will))
print(will)
print([id(ele for ele in will)])
print(id(wilber))
print(wilber)
print([id(ele for ele in wilber)])