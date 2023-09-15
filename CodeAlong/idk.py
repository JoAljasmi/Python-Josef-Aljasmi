from colorama import Fore, Back, Style
user_input = input("Enter your prompt: ")
numbers = "0123456789"
initial_char = ""
char_index_1 = 0
for char_1 in user_input:
    if char_1 in numbers:
        initial_char = char_1
        substring_index = char_index_1+1
        char_index_2 = substring_index
        for char_2 in user_input[substring_index:]:
            if char_2 not in numbers:
                break
            else:
                if char_2 == char_1:
                    print(f'{Fore.WHITE+user_input[:char_index_1]}{Fore.RED+user_input[char_index_1:char_index_2+1]}{Fore.WHITE+user_input[char_index_2+1:]}')
                    break
                else:
                    char_index_2 += 1 
    char_index_1 += 1