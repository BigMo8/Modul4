letter_list = []
def palindrom(word_given):
    for letter in word_given:
        letter_list.append(letter)
    a= len(letter_list)
    for i in range (0, a):
        first_letter=letter_list[i]
        last_letter=letter_list[-i-1] 
        print(first_letter, "and", last_letter)
    if first_letter == last_letter:
        print(word_given, "is palindrome")
    else:
        print(word_given, "isn't palindrome")
    
    print("word lenght:", a)

        
palindrom(word_given = "kaamaamaad")
    