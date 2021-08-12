player_details=[]
def create_player(id,name,matches_played,runs_scored,playing_zone):
    player_d={}
    zone=["north","south","east","west"]
    if(len(id)==6 and id[:3] == "ICC" and id[3:].isnumeric()):
        if playing_zone.lower() in zone:
            player_d['Id']=id
            player_d['Name']=name
            player_d['Matches_Played']=matches_played
            player_d['Run_Scored']=runs_scored
            player_d['Playing_Zone']=playing_zone
            player_details.append(player_d)
            return "Player details are created successfully"
        else:
            return "Invalid Data"
    else:
        return "Invalid Data"
def display_player(player_details):
    if len(player_details)==0:
        print("No player details have been stored");
    else:
        for i in range(len(player_details)):
            print("Player {}:".format(i+1))
            print("Player Id:",player_details[i]['Id'])
            print("Player Name:",player_details[i]['Name'])
            print("No. of Matches Played:",player_details[i]['Matches_Played'])
            print("Total Runs Scored:",player_details[i]['Run_Scored'])
            print("Playing Zone:",player_details[i]['Playing_Zone'])
flag=True
while flag:
    print("1.Create Player\n2.Display Player Details\n3.Exit")
    n = int(input())
    if n == 1:
        print("Enter the player Id")
        id = input()
        print("Enter the player name")
        name = input()
        print("Enter the number of matches played")
        match = int(input())
        print("Enter the total runs scored")
        runs = int(input())
        print("Enter the playing zone")
        zone = input()
        print(create_player(id,name,match,runs,zone))
    elif n==2:
        print("PLAYER DETAILS:")
        display_player(player_details);
    else:
        flag=False
        print("Thank you for using the SBCC application")
