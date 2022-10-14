#Cesar Giner
#CS-101L
#LAB 7
#10-14-2022




# asking user to enter min mpg to check vehicles, and setting (try except) statements to only calculate numbers, while loop until correct inputs 
user_mpg = -1
while user_mpg < 0 or user_mpg > 100:
    try:
        user_mpg = float(input('Enter the minimum mpg ==> '))
        if user_mpg < 0:
            print('Fuel economy given must be greater than 0')
        if user_mpg > 100:
            print('Fuel economy given must be less than 100')
    except ValueError:
        print('You must enter a number for the fuel economy')


#while loop for user to enter valid file name, if not found, prompt error executed by except handle
while(1):
    try:
        input_file = input('Enter the name of the input vehicle file ==> ')
        file = open(input_file)
        break
    except FileNotFoundError:
        print('Could not open file {}'.format(input_file))

#while loop for user to enter a valid output file, prompted with IO error if invalid file name
while(1):
    try:
        output_file = input('Enter the name of the file to output to ==> ')
        file2 = open(output_file,'w')
        break
    except IOError:
        print('There is an IO Error {}'.format(output_file))

print()

#open input file, (vehicle 1 or 2), readlines() to set a variable for txt in file, then look for values that will satisfy user mpg input, write in file2(user output file)
file = open(input_file)
contents = file.readlines()
file.close()
file2 = open(output_file,'w')
for i in contents[1:]:
    try:
        x = i.split('\t')
        if float(x[-3]) >= user_mpg:
            file2.write('{:<5}{:<20}{:<40}{:>10}\n'.format(x[0],x[1],x[2],x[-3]))
    except:
        print('Could not convert value {} for vehicle {} {} {}'.format(x[-3],x[0],x[1],x[2]))
file2.close()


#printed the results of the calculation as well as let user know their file is saved with their results.
print('Your results(below) are now saved in a file called {}:'.format(output_file))
print()
file2 = open(output_file)
contents2 = file2.read()
file2.close()
print(contents2)






    




        
    


