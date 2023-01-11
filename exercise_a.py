#1. Add "Edinburgh Waverley" to the end of the list
stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
print(stops)

#2. Add "Glasgow Queen St" to the start of the list
stops.append('Edinburgh Waverly')
print(stops)

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(0, 'Glasgow Queen Street')
print(stops)

#4. Print out the index position of "Linlithgow"
stops.insert(4, 'Polmont')
print(stops)

#5. Remove "Livingston" from the list using its name
print(stops.index('Linlithgow'))
print(stops)

#6. Delete "Cumbernauld" from the list by index
stops.remove('Livingston')
print(stops)

#7. Print the number of stops there are in the list
del stops[2]
print(stops)

#8. Sort the list alphabetically
stops.sort()
print(stops)

#9. Reverse the positions of the stops in the list
stops.reverse()
print(stops)

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)




