#Importing Reqquired Libraries
import math
import re
import argparse

while True:
    def get_distance(total_path):
        curr_position = [0,0]
        movement = total_path.split(",")

        for i in movement:
            #validating the Alphabets, numbers and lenth of the input 
            if (re.findall("[A-Z]", i[0])):
                if (re.findall("[0-9]", i[1])):
                    if(len(i) == 2):
                        command = i[0]
                        number = int(i[1])
                        if command == "F":
                            curr_position[0] += number
                        elif command == "B":
                            curr_position[0] -= number
                        elif command == "R":
                            curr_position[1] += number
                        elif command == "L":
                            curr_position[1] -= number
                        else:
                            print("Invalid Path, Accepted: F,B,R,L")
                            return "Invalid Path, Accepted: F,B,R,L" #for testing
                    else:
                        print("Only one alphabet and one digit allowed between commas")
                        return "Only one alphabet and one digit allowed between commas" #For Testing
                else:
                    print("Please use the number in the after the direction command")
                    return "Please use the number in the after the direction command" #For testing
            else:
                print("Please use capital letters for the commands (directions)")
                return "Please use capital letters for the commands (directions)" #For Testing

        #Calculating Distance from the origin
        distance = int(round(math.sqrt(curr_position[1]**2+curr_position[0]**2)))
        print(f"Distance from the starting point is {distance} units")
        return distance


    if __name__ == '__main__':
        #Creating Help Text and Description  
        parser = argparse.ArgumentParser(prog="Robot Movement", 
                                usage = '''
                                Find the Robot's minimum distance from its starting point                      
                                ''',
                                description='''
                                ****************************************************
                                Description:
                                ****************************************************


                                This tool receives a string of commands and will output the robot's distance from it's starting point.
                                Sample Input: - a string of comma-separated commands eg `F1,R1,B2,L1,B3`

                                ''',
                                epilog= "Copyright @Bhavesh Pandey: Tool Build for Woven graduate coding test",
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                add_help=True)
        
        arg = parser.parse_args()
        print("Find the Robot's minimum distance from its starting point".center(100,'*'))
        print('''
         \nSample Input:  `F1,R1,B2,L1,B3`\n
                ''')
        total_path = input("\nPlease enter the path : ")
        get_distance(total_path)
