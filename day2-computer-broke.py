with open('day2inputs.txt', 'r') as file:
    codes = file.read().split(",")

def fixProgram(program, noun, verb):
    i=0
    program[1]=noun
    program[2]=verb
    while int(program[i]) != 99:
        if int(program[i]) == 1:
            program[int(program[i + 3])] = int(program[int(program[i + 1])]) + int(program[int(program[i + 2])])
        if int(program[i]) == 2:
            program[int(program[i + 3])] = int(program[int(program[i + 1])]) * int(program[int(program[i + 2])])
        i += 4
    return program[0]

# print(fixProgram(codes,12,2))
print(fixProgram(codes,50,64))
