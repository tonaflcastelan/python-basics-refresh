# -- Difference between two sets --

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# local_friends = ...
# If there are 3 friends, and 2 are abroad, that means that 1 friend is local.
# We can easily calculate which names are in `friends` but not in `abroad` by using `.difference`

local = friends.difference(abroad)
print(local)

print(abroad.difference(friends))  # This returns an empty set

# -- Union of two sets --

local = {"Rolf"}
abroad = {"Bob", "Anne"}

# friends = ...
# If we have 1 local friend and 2 abroad friends, we could calculate the total friends by using `.union`

friends = local.union(abroad)
print(friends)

# -- Intersection of two sets --

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# Given these two sets of students, we can calculate those who do both art and science by using `.intersection`

both = art.intersection(science)
print(both)


set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 12, 9}

both2 = set1.intersection(set2)
print(both2)