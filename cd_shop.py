# Reference for insertion sort: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html

# Define create_database() function that stores the list of lists of the data
def create_database():
    # Reads the CD_Store text file
    CD = open("CD_Store.txt")
    data = []

    # Appending the data in the CD_Store to the new list called 'data'
    for line in CD:
        line = line.strip().split(',')
        data.append(line)

    # Changing the type of the price to float
    for i in range(len(data)):
        data[i][3] = float(data[i][3])

    # Returns the list of lists for CD_Store
    return data


# Define display_menu() function that displays the possible options for user to choose
def display_menu():
    menu = ["1. Print List of CDs", "2. Sort CDs by Title", "3. Sort CDs by Artist", "4. Sort CDs by Genre", "5. Sort CDs by Price", "6. Find All CDs by Title", "7. Find All CDs by Artist", "8. Find All CDs by Genre", "9. Find All CDs with Price at Most X", "10. Quit"]

    for option in menu:
        print(option)


# Define print_list() function that takes in a list as an argument to print
def print_list(alist):
    # Setting the labels for the CD_Store
    label = ['Title', 'Artist', 'Genre', 'Price']

    # Counting the length of each label
    # label_count = [title, artist, genre, price], where each label represents the length of it
    # Eg: the length of 'Title' is 5 and the value of 5 will be append into the label_count
    label_count = []
    for i in range(len(label)):
        label_count.append(len(label[i]))

    # Create a 'highest' variable that stores the maximum length of each data
    highest = []
    for j in range(4):
        track = []
        for i in range(len(alist)):
            # if the data found is not in the 'Price' column, it appends the length of the data to 'track'
            if type(alist[i][j]) != float:
                track.append(len(alist[i][j]))
            else:
                track.append(len(str(alist[i][j])))

        # computing the maximum length of the data and appending it to 'highest'
        # Eg: if highest = [9, 10, 15, 5]
        # then the maximum length of the data in the 'Title' column is 9, 'Artist' column is 10, 'Genre' column is 15 and 'Price' column is 5
        highest.append(max(track))

    # This section compares the maximum length of 'highest' and 'label count'
    maximum = []
    for k in range(len(highest)):
        # if the label_count[k] is greater and equals to highest[k], it appends the label_count[k] to 'maximum'
        if label_count[k] >= highest[k]:
            maximum.append(label_count[k])
        else:
            maximum.append(highest[k])

    # This section adds spacing to the end of each item in 'label' according to 'maximum'
    for u in range(len(label)-1):
        while True:
            if len(label[u]) <= maximum[u]:
                label[u] += " "
            else:
                label[u] += "| "
                break

    dash = ""
    for i in range(len(label)):
        dash += label[i]

    # Printing the header section which includes the label of each column and a line to separate the data and the header
    print(*label)
    print("-" * (len(dash)+4))

    # This section adds spacing to the end of each data in the column
    for i in range(len(alist)):
        string = []
        for j in range(len(alist[i])):
            if j != len(alist[i]) - 1:
                string.append(alist[i][j])
                while len(string[j]) <= maximum[j]:
                    string[j] += " "
                string[j] += "| "
            else:
                string.append(str(alist[i][j]))
                while len(string[j]) <= maximum[j]:
                    string[j] += " "
        print(*string)


# Define sort_by_title() that takes a list as input and sort according to the title
def sort_by_title(alist):
    for i in range(1, len(alist)):
        temp_value = alist[i][0]
        temp_list = alist[i]
        count = i

        while alist[count - 1][0] > temp_value and count > 0:
            alist[count] = alist[count - 1]
            count -= 1

        alist[count] = temp_list


# Define sort_by_genre() that takes a list as input and sort according to the genre
def sort_by_genre(alist):
    for i in range(1, len(alist)):
        temp_value = alist[i][2]
        temp_list = alist[i]
        count = i

        while alist[count - 1][2] > temp_value and count > 0:
            alist[count] = alist[count - 1]
            count -= 1

        alist[count] = temp_list


# Define sort_by_artist() that takes a list as input and sort according to the artist
def sort_by_artist(alist):
    for i in range(1, len(alist)):
        temp_value = alist[i][1]
        temp_list = alist[i]
        count = i

        while alist[count - 1][1] > temp_value and count > 0:
            alist[count] = alist[count - 1]
            count -= 1

        alist[count] = temp_list


# Define sort_by_price() that takes a list as input and sort according to the price
def sort_by_price(alist):
    for i in range(1, len(alist)):
        temp_value = alist[i][3]
        temp_list = alist[i]
        count = i

        while alist[count - 1][3] > temp_value and count > 0:
            alist[count] = alist[count - 1]
            count -= 1

        alist[count] = temp_list


# Define find_by_title() that takes a list and the title to search as input
def find_by_title(alist, title_search):
    title = []

    # searching for the title in the title column
    for i in range(len(alist)):
        # if the title given by the user matches with the title in the database, it appends the entire row into 'title'
        if title_search.lower() == alist[i][0].lower():
            title.append(alist[i])

    # if the 'title' is found to be empty, it means that the title given is not in the database, so returns False
    if title == []:
        return False
    # if the 'title' found is not empty, it prints the data
    else:
        print_list(title)


# Define find_by_genre() that takes a list and the genre to search as input
def find_by_genre(alist, genre_search):
    genre = []

    # searching for the genre in the genre column
    for i in range(len(alist)):
        # if the genre given by the user matches with the genre in the database, it appends the entire row in to 'genre'
        if genre_search.lower() == alist[i][2].lower():
            genre.append(alist[i])

    # if the 'genre' is found to be empty, it means that the genre given is not in the database, so returns False
    if genre == []:
        return False
    # if the 'genre' found is not empty, it prints the data
    else:
        print_list(genre)


# Define find_by_artist() that takes a list and the artist to search as input
def find_by_artist(alist, artist_search):
    artist = []

    # searching for the artist in the genre column
    for i in range(len(alist)):
        # if the artist given by the user matches with the artist in the database, it appends the entire row in to 'artist'
        if artist_search.lower() == alist[i][1].lower():
            artist.append(alist[i])

    # if the 'artist' is found to be empty, it means that the artist given is not in the database, so returns False
    if artist == []:
        return False
    # if the 'artist' found is not empty, it prints the data
    else:
        print_list(artist)


# Define find_by_price() that takes a list and the price to search as input
def find_by_price(alist, price_search):
    price = []

    # searching for the price in the genre column
    for i in range(len(alist)):
        # if the price given by the user matches with the price in the database, it appends the entire row in to 'price'
        if float(price_search) >= alist[i][3]:
            price.append(alist[i])

    # if the 'price' is found to be empty, it means that the price given is not in the database, so returns False
    if price == []:
        return False
    # if the 'price' found is not empty, it prints the data
    else:
        print_list(price)


#######################################################################################

# Storing the CD_Store to 'store'
store = create_database()


# Constantly asks the user to enter choice, until it reaches 'break' when user enter '10'
while True:
    # Display the menu for the user
    display_menu()
    print("")

    # Asks user to enter choice of 1 to 10 based on the menu
    choice = input("Enter a choice (from 1 to 10): ")
    print("")

    if choice == "1":
        print_list(store)
        print("")

    elif choice == "2":
        sort_by_title(store)

    elif choice == "3":
        sort_by_artist(store)

    elif choice == "4":
        sort_by_genre(store)

    elif choice == "5":
        sort_by_price(store)

    elif choice == "6":
        title_search = input("Enter full title name: ")
        title_result = find_by_title(store, title_search)

        # if the result found is empty, it will print no result found
        if title_result == False:
            print("Sorry, no result found")
        print("")

    elif choice == "7":
        artist_search = input("Enter full artist name: ")
        artist_result = find_by_artist(store, artist_search)

        # if the result found is empty, it will print no result found
        if artist_result == False:
            print("Sorry, no result found")
        print("")

    elif choice == "8":
        genre_search = input("Enter full genre name: ")
        genre_result = find_by_genre(store, genre_search)

        # if the result found is empty, it will print no result found
        if genre_result == False:
            print("Sorry, no result found")
        print("")

    elif choice == "9":
        price_search = input("Enter price figure (numbers only): ")
        result = find_by_price(store, price_search)

        # if the result found is empty, it will print no result found
        if result == False:
            print("Sorry, no result found")
        print("")

    # break the loop when user quits
    elif choice == "10":
        print("Thanks for using my service!")
        break

    # if the user enters choices out of 1 to 10, it will request the user to re-enter again
    else:
        print("Please enter only choice from 1 to 10")
        print("")
