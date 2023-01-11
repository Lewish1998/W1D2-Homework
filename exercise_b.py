users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# Jonathon's Twitter Handle
jonathon_twitter_handle = users["Jonathan"]['twitter']

# Erik's Hometown
erik_hometown = users["Erik"]["home_town"]

# Erik's Lotto Numbers
erik_lotto_num = users["Erik"]["lottery_numbers"]

# Avrils Pet Species
avril_pet_species = users["Avril"]["pets"][0]["species"]

# Smallest of Erics Number
erik_smallest_lotto = min(erik_lotto_num)

# Avrils even lotto numbers
even_numbers = []
avril_lotto_num = users["Avril"]["lottery_numbers"]
for num in avril_lotto_num:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)


# Add to Erik's lotto numbers
erik_lotto_num.append(7)

# Change Eriks Hometown
erik_hometown = users["Erik"]["home_town"] = ["Edinburgh"]

# Add pet to Erik 
users["Erik"]["pets"].insert(0, {'name': 'fluffy', 'species': 'dog'})
print(users["Erik"]["pets"])

# Add another person
users["Lewis"] = {
    "twitter": "lewh98",
    "lottery_numbers": [1, 2, 3, 4, 5, 6],
    "home_town": "Glasgow",
    "pets": [
    {
      "name": "Big Steve",
      "species": "Dragon"
    }
  ]
}

print(users)