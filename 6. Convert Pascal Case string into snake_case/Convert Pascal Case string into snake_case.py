def snake(string):
    string = str(string)
    snake_c = ""
    for i,l in enumerate(string):
        if "A" <= l <= "Z" and i > 0:
            snake_c += "_" + l.lower()
        else:
            snake_c += l.lower()
    
    return snake_c

print(snake("TestController"))
print(snake("MoviesAndBooks"))
print(snake("App7 Test"))
print(snake(1))