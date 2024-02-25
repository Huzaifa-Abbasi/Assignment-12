'''Design a program that lets users rate movies on a scale from 1 to 5. Use a dictionary to store 
movie titles and their average ratings.'''

dict = {}
while True:
    movie = input("Enter the title of movie: ")
    rating = float(input("Enter the rating: ")) >= 5
    dict[movie] = rating
    user_input = input("Do You want to add more movies: ")
    if user_input == "no":
        break
print(dict)
