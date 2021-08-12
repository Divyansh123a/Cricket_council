# Cricket_council
Expected completion time: 30 minutes

Topics Covered: Control structures, Collection Frameworks, Class and Objects

State Board of Cricket Council (SBCC) is one of the leading cricket selection academies in the state. They are in need of an automated system that should manipulate the player details provided and also find the players who have secured star ratings between specific ranges from the database.  You being their software consultant have been approached to develop a Python application that can be used by the admin for the above-mentioned requirement.

Requirement:  Create a player profile by validating given data and store it into a list using functions.

This functionality deals with getting the basic details of players such as player Id, player Name, number of matches played, run scored, and playing zone of the players and store all this information into a dictionary by validating the given information. Create players and display the player's details as specified in the sample input and output using functions.

Player Details:

Attribute Name

Data Type

player_details

list

 

 

 



Perform the below operations to complete the requirement.

1.  Create the menu as specified in the sample input and output statements.

2.  Create a list  ‘player_details’ of type list in the main program.

3.  Create the following functions in the program:

a. create_player(id,name,matches_played,runs_scored,playing_zone): 

This method should take player id, name,matches_played,runs_scored and playing_zone as its argument and should check whether the given data is valid or not, if the given data is valid save the data inside a dictionary else returns the message “Invalid Data”.

The given data is valid if it satisfies the below conditions:

The id should be of 6 length character, the first 3 characters should be ICC and the next 3 characters should be number.
The playing zone should be either “North“, “South“, “East“, or “west“.
If the given data satisfies the above conditions, save the data inside a dictionary as  follows:

{“Id”:<id of the player>,” Name”:<name of the player>,” Matches_Played”:<no. of matches played>, “Run_Scored”:<total no. of run taken>, “Playing_Zone”:<player’s zone>}

This dictionary should be appended to the list ‘player_details’ and should return the message “Player details are created successfully”.

 b. display_player(players_details): This method should take ‘player_details’ list as an argument and should check whether player_details list is empty or not, if the list is empty display “No player details available” else display  all player details as mentioned in the sample output.

 4.  If the user enters option1, get the player details such as player id, name, matches played, runs scored, and playing zone from the user and pass those details to function  ‘create_player()’.

5. If the user enters option 2,  pass the list ‘player_details’ as an argument to function ‘display_player()’

6. Option 3 is to stop the program execution.  For this don't use 'system.exit(0)' .  Instead, use the 'break' statement.

Strictly follow the naming conventions for variables and functions as specified in the problem description.

 

Sample Input and Output  Statements 1:

1. Create Player

2. Display Player Details

3. Exit

Enter your choice

1

Enter the player Id

ICC001

Enter the player name

Dhoni

Enter the number of matches played

10

Enter the total runs scored

678

Enter the playing zone

North

Player details added successfully

1. Create Player

2. Display Player Details

3. Exit

Enter your choice

1

Enter the player Id

ICC002

Enter the player name

ROHITH

Enter the number of matches played

8

Enter the total runs scored

458

Enter the playing zone

North

Player details added successfully

1. Create Player

2. Display Player Details

3. Exit

2
PLAYER DETAILS:

Player 1: 

Player Id: ICC001

Player Name: DHONI

No. of Matches Played: 10

Total Runs Scored: 678

Playing Zone: North

 

Player 2:

Player Id: ICC002

Player Name: ROHIT

No. of Matches Played: 8

Total Runs Scored: 458

Playing Zone: North

 

1. Create Player

2. Display Player Details

3. Exit

Enter your choice

3

Thank you for using the SBCC application

 

Sample Input and Output 2:

1. Create Player

2. Display Player Details

3. Exit

Enter your choice

2

No player details have been stored

1. Create Player

2. Display Player Details

3. Exit

Enter your choice

3

Thank you for using the SBCC application
