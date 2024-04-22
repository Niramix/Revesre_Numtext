
Input_text = input("Input Text : ")
print(Input_text)

def remove_non_digit(s):
    no = ""
    for i in s:
        if i.isdigit():
            no += i
    return no

print("you number :", remove_non_digit(Input_text))

nontext = remove_non_digit(Input_text)

def my_function(x):
  return x[::-1]

reverse_text = my_function(nontext)

print(reverse_text)