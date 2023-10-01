text = input('Enter your string: ')
revText = text[::-1]  # Reverse slice

if text.lower() == revText.lower():  # Catch capitals
    print(f'{text} IS a palindrome ')
else:
    print(f'{text} is NOT a palindrome')
