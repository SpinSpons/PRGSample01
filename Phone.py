character = [' ',
             'a','b','c','d','e','f',
             'g','h','i','j','k','l','m','n','o',
             'p','q','r','s','t','u','v','w','x','y','z']
mapping = ['0',
           '2','22','222','3','33','333',
           '4','44','444','5','55','555','6','66','666',
           '7','77','777','7777','8','88','888','9','99','999','9999']

f = open('TextMessage.txt','r')
line = f.read().strip().lower()
print(line)
f.close()

# for i in range(len(line)):
#     char = line[i]
#     digit = mapping[character.index(char)]
#     print(digit, end='')
#     if i < len(line)-1 and char == line[i+1]:
#         print(' ', end='')

# Initialize variables
output = ""
index = 0

# Use while loop to convert each character
while index < len(line):
    char = line[index]
    
    # Find the index of the character in the character list
    i = 0
    while i < len(character):
        if char == character[i]:
            output += mapping[i]
            break
        i += 1
    
    # Check for pause: if current and next char are the same
    if index < len(line) - 1:
        next_char = line[index + 1]
        if char == next_char:
            output += ' '  # add pause

    index += 1

# Display the result
print(output)