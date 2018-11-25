"""
Cities.csv format
Name,TopLeft_X,TopLeft_Y,BottomRight_X,BottomRight_Y
New York,1,1,5,6
"""
"""
Points.csv format
ID,X,Y
Point_1,2,1
"""

import csv
import sys

# Default initial value for the output file
output_file = 'output_points.csv'

# Default initial value for the cities file
cities_file = 'cities.csv'

# Default initial value for the points file
points_file = 'points.csv'

'''
checking the number of Argument passed to the script through the command line
the Argument can be as the following:
 - 2 Arguments and the second argument is '--help' the script will show the help text
 - the number of aruments is not valid, error message will be viewed to the user
 - no argument passed, the defualt value will be used as mentioned above this code

'''
total = len(sys.argv)
#print (total)
if total == 2 :
    if str( sys.argv[1]) == '--help':
        print ("\nPlease run the script with 3 arguments as following:")
        print ("\tFirst argument must be Cities csv filename" )
        print ("\tSecond argument must be Points csv filename" )
        print ("\tFirst argument must be output csv filename" )
        print ("\tExample: python main.py cities.csv points.csv output.csv")
        print ("\tNote: you can run the script without any arguments and to handle cities.csv and points.csv in the same folder of the script\n")
        sys.exit()

if 1 < total < 4 or total > 4 :
    print ("\nError : The total numbers of args must passed to this script is 3 Argument, run \'python main.py --help\' for more info\n")
    sys.exit()

elif total == 4:
    cities_file = sys.argv[1]
    points_file = sys.argv[2]
    output_file = sys.argv[3]
    
'''
this function to read any csv file and convert it to Dictionary
'''
def csv_dict_list(filename): 
    with open(filename, mode='r') as csvfile:    
        reader = csv.DictReader(csvfile)
        dict_list = []
        for row in reader:
            dict_list.append(row)
        return dict_list

# extracting the cities form the csv from
dict_cities = csv_dict_list(cities_file)

# extracting the points form the csv from
dict_points = csv_dict_list(points_file)

print("\n")

#initial value for ouput results dictionary
output_points = []

#this function will check if certain point is inside any City or touches it boundry
def checkpoint(point):
    insidecity = False
    for cityrow in dict_cities:
        if int(cityrow["TopLeft_X"]) <= int(point["X"]) and int(cityrow["TopLeft_Y"]) <= int(point["Y"]) and int(cityrow["BottomRight_X"]) >= int(point["X"]) and int(cityrow["BottomRight_Y"]) >= int(point["Y"]) :
            print (f'\t{row["ID"]}  is in  {cityrow["Name"]}' )
            point["City"] = cityrow["Name"]
            output_points.append(point.copy())
            insidecity = True
    return insidecity

# number of current row in points dict
pointrow = 0

#looping through points and checking each point against Cities boundries
for row in dict_points:
    print(f'{row["ID"]} cordinates is ({row["X"]} , {row["Y"]})')
    insidecity = checkpoint(row)
    if insidecity == False:
        output_points.append(dict_points[pointrow])
        output_points[len(output_points) - 1]["City"] = 'None'
        print (f'\t{row["ID"]}  is not in any City' )
    pointrow = pointrow+1   

print("\n")

#writing down the output results (each point and cities-it sits within )
try:
    with open(output_file, 'w' , newline='') as csvfile:
        csv_columns = ['ID','X','Y','City']
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in output_points:
            writer.writerow(data)
        print ("output results written to file" + output_file + "\n")
except IOError:
    print("I/O error during writing the output to csv file")  
