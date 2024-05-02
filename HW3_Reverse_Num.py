
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

#Remove Zero
nontext0 = nontext.replace("0","")

print("you number no zero :",nontext0)

def my_function(x):
  return x[::-1]

reverse_text = my_function(nontext0)

print(reverse_text)
