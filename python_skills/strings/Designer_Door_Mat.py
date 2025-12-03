"""
How to set text center
Ref: https://www.w3schools.com/python/ref_string_center.asp
txt = "banana"

x = txt.center(20, "O")

Result: OOOOOOObananaOOOOOOO
"""

# Example input: 7 21

input_size = input().split()
print(input_size)

N = int(input_size[0])
M = int(input_size[1])

harf_size = N//2

# print(harf_size)

texture = ".|."
number_texture = 1

#  Upper
for i in range(1, harf_size+1):
    # print("-")
    # print(f"DEBUG: {texture_print}")
    if i == 1:
        upper_result = texture.center(M, "-")

    else:
        number_texture +=2
        texture_print = (texture*(number_texture))

        upper_result = texture_print.center(M, "-")
    print(upper_result)

# Center
center_text = "WELCOME"
print(center_text.center(M, "-")) 

# Lower
for i in range(1, harf_size+1):

    if i == 1:
        lower_result = texture_print.center(M, "-")
    else:
        number_texture-=2
        texture_print = (texture*(number_texture))
        lower_result = texture_print.center(M, "-")
    print(lower_result)