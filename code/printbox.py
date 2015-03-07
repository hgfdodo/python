sentence = raw_input("Sentence:")

screen_width = 80
txt_len = len(sentence)
box_width = txt_len +4;
kong = (screen_width-box_width)//2

print("\n")

print("+" + 78 *"-" + "+")
print(" " * (kong-1) + "|" + box_width*" " + "|" + (kong-1)*" ")
print(" " * (kong-1) + "|" + " " *2 + sentence + " " * 2 + "|" + (kong-1)*" ")
print(" " * (kong-1) + "|" + box_width*" " + "|" + (kong-1)*" ")
print("+" + 78 *"-" + "+")

print("\n")
