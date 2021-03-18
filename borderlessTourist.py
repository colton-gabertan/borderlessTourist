# @author Colton Gabertan
# @date 3/17/21
# @brief This program is a search engine used to help tourists based on parameters entered

# populating data and defining search functions

# destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

#attractions to be populated by function 
attractions = [[] for destination in destinations]

# search function for destinations list
def getDestinationIndex(destination):
  destinationIndex = destinations.index(destination)
  return destinationIndex

# search function to find the traveler's location
def getTravelerLocation(traveler):
  travelerDestination = traveler[1]
  travelerDestinationIndex = getDestinationIndex(travelerDestination)
  return travelerDestinationIndex

# function to populate data in attractions for each location
def addAttractions(destination, attraction):
  try:
    destinationIndex = getDestinationIndex(destination)
    attractionsForDestination = attractions[destinationIndex]
    attractionsForDestination.append(attraction)
    return attractionsForDestination
  except ValueError:
    return

# using function to populate pseudo database to be searched
addAttractions("Los Angeles, USA", ["Venice Beach", ["beach"]])
addAttractions("Paris, France", ["the Louvre", ["art", "museum"]])
addAttractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
addAttractions("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
addAttractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
addAttractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
addAttractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
addAttractions("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
addAttractions("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
addAttractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
addAttractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# search engine function 
def findAttractions(destination, interests):
  destinationIndex = getDestinationIndex(destination)
  attractionsInCity = attractions[destinationIndex]

  attractionsWithInterest = []
  for attraction in attractionsInCity:
    possibleAttraction = attraction
    attractionTags = attraction[1]
    for interest in interests:
      if interest in attractionTags:
        attractionsWithInterest.append(possibleAttraction[0])

  return attractionsWithInterest

# function to call search engine and display data
def getAttractionsForTraveler(traveler):
  travelerDestination = traveler[1]
  travelerInterests = traveler[2]

  travelerAttractions = findAttractions(travelerDestination, travelerInterests)

  interestsString = "Hi " + traveler[0] + ", we think you'll like these places around " + travelerDestination +": " 

  for attraction in travelerAttractions:
    interestsString += attraction

  return interestsString

# test 
print(getAttractionsForTraveler(['Dereck Smill', 'Paris, France', ['monument']]))
