song_library = [
("Phantom Of The Opera", "Sarah Brightman"),
("Knocking On Heaven's Door", "Guns N' Roses"),
("Captain Nemo", "Sarah Brightman"),
("Patterns In The Ivy", "Opeth"),
("November Rain", "Guns N' Roses"),
("Beautiful", "Sarah Brightman"),
("Mal's Song", "Vixy and Tony"),
]
 
artists = set()
for song, artist in song_library:
    artists.add(artist)
 
print(artists)
 
if "Opeth" in artists:
    print("Opeth in artists")
 
for artist in artists:
    print(artist, "plays good music")

print("--------------------------------------------------------------------------------------------------")

my_collection = {
"Sarah Brightman",
"Guns N' Roses",
"Opeth",
"Vixy and Tony",
}
 
your_collection = {"Nickelback", "Guns N' Roses", "Savage Garden"}
 
print("All:", my_collection.union(your_collection))
print("Both:", your_collection.intersection(my_collection))
print("Either but not both:", my_collection.symmetric_difference(your_collection))

print("--------------------------------------------------------------------------------------------------")

mine = {"Sarah Brightman", "Guns N' Roses", "Opeth", "Vixy and Tony"}
 
yours = {"Guns N' Roses", "Opeth"}
 
print("first_artists is to bands:")
print("issuperset:", mine.issuperset(yours))
print("issubset:", mine.issubset(yours))
print("difference:", mine.difference(yours))
 
print("*" * 20)
 
print("bands is to first_artists:")
print("issuperset:", yours.issuperset(mine))
print("issubset:", yours.issubset(mine))
print("difference:", yours.difference(mine))