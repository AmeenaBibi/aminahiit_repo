word = input("Enter word: ")
is_palindrome = word == word[::-1] 
print(f"Is the word {word} a palindrome?: {is_palindrome}")