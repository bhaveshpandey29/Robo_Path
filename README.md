# Robo_Path
Code Challenge for Woven graduate coding test

****************************************************
     Description
****************************************************


This tool receives a string of commands and will output the robot's distance from it's starting point.

How to run?

- Goto Dist Directory
- Open "Robo_Movemnet.exe"

=> Sample Input:  `F1,R1,B2,L1,B3`

***Additional Help can be found while loading the .exe file in CMD by using -h, e.g : <Path>\Robo_Path\dist\Robo_Movement.exe -h   

Test Cases Covered Below:

1. Default Value `F1,R1,B2,L1,B3`
2. Changed First Alphabet
3. Use of small words (Only Capital Allowed)
4. Two Digits input (Only One Word and one Digit is allowed)


Test Cases can be found in Robo_movement_test.py

To run Test Cases : pytest <filename>.py

***NOTE: Please remove While=true condition to run the tests from the Robo_movement.py file, while condition is placed to keep the CLI application open

[Additional TXT file added]
Copyright @Bhavesh Pandey: Tool Build for Woven graduate coding test
