# Tuple practice

location = (6.51, 3.39, "Lagos", "Nigeria",)

print(location[2])

latitude, longitude, city, country = location

print(latitude)
print(longitude)
print(city)
print(country)

my_name = tuple("Corinne")
print("x" in my_name)
my_name1 = my_name[1:]
print(my_name1)