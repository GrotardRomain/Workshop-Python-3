# Tuples

tup = ()
tup = ("abc", "abc")
print(tup, " this was Tuples 01")

tup = ("2",
    ("another one...", "... yeah another one"),
    "1")
print(tup, " this was Tuples 02")

tup = (
    ("another","another"),
    ("more", "more"),
    )
print(tup)
print (tup[0])
print (tup[0][0], " this was Tuples 03")

tup += ("yetAnother", 123)
print(tup)
tup += (("yetAnother", 123))
print(tup, " this was Tuples 04")