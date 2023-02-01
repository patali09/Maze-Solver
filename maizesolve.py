# sample_maze = """*.....####
# ####..####
# .....#####
# ......####
# ......####
# ..........
# ######....
# ######....
# #######...
# ###.....##
# ###.......
# #########.
# #########.
# #########.
# #########$
# """
raw_maze = []
maze = []
maze_block = "ALl the best"
while(maze_block!=""):
    if (maze_block=="ALl the best"):
        maze_block = input("Please enter the maze: ")
    else:
        maze_block = input()
    if(maze_block!=""):
        raw_maze.append(maze_block)
    else:
        pass
    

start_symbol = input("Enter the start symbol: ")
wall_symbol = input("Enter the wall symbol: ")
end_symbol = input("Enter the end symbol: ")
track_symbol = input("Enter the track symbol: ")


for i in raw_maze:
    maze.append(i.replace(start_symbol, "s").replace(track_symbol, "d").replace(wall_symbol, "h").replace(end_symbol, "m"))


size_of_maze = len(maze)-1
position_of_s = [-1,-1]
position_of_d = [-1, -1]
track = []
for i in maze:
    try:
        position_of_s = [maze.index(i), i.index("s")]
    except:
        if(position_of_s==-1 and maze.index(i)==size_of_maze):
            print("THere is no starting point")

for i in maze:
    try:
        position_of_d = [maze.index(i), i.index("m")]
    except:
        if(position_of_d==-1 and maze.index(i)==size_of_maze):
            print("THere is no ending point")
print("Starting coordinates: "+str(position_of_s))
print("Ending Coordinates: "+str(position_of_d))
reached = 0
left_mv =0
right_mv = 0
up_mv =0
down_mv = 0

def down_position():
    if(maze[position_of_s[0]+1][position_of_s[1]]=="d" or maze[position_of_s[0]+1][position_of_s[1]]=="m"):
        global down_mv
        down_mv = 1
    else:
        False

def up_position():
    if(maze[position_of_s[0]-1][position_of_s[1]]=="d" or maze[position_of_s[0]-1][position_of_s[1]]=="m"):
        global up_mv
        up_mv = 1


    else:
        False

def right_position():
    if(maze[position_of_s[0]][position_of_s[1]+1]=="d" or maze[position_of_s[0]][position_of_s[1]+1]=="m"):
        global right_mv
        right_mv = 1


  

def left_position():
    if(maze[position_of_s[0]][position_of_s[1]-1]=="d" or maze[position_of_s[0]][position_of_s[1]-1]=="m"):
        global left_mv
        left_mv = 1



def check_s_and_d():
    if((position_of_d[0]-position_of_s[0]==0) and (position_of_d[1]-position_of_s[1])==0):
        global reached
        reached = 1

def output():
    output_Str= 0
    for i in track:
        try:
            if (track[track.index(i)+1][0]-track[track.index(i)][0]>0):
                print("Down", end="\n")

                pass
        except:
            pass
        try:
            if (track[track.index(i)+1][0]-track[track.index(i)][0]<0):
                print("Up", end="\n")

        except:
            pass
        try:
            if (track[track.index(i)+1][1]-track[track.index(i)][1]>0):
                print("Right", end="\n")

        except:
            pass
        try:
            if(track[track.index(i)+1][1]-track[track.index(i)][1]<0):
                print("Left", end="\n")

        except:
            pass


while(reached!=1):
    check_s_and_d()
    try:
        down_position()
    except:
        pass
    try:
        up_position()
    except:
        pass
    try:
       left_position()
    except:
        pass
    try:
        right_position()
    except:
        pass
    if((down_mv==1) or (up_mv==1) or (left_mv==1) or (right_mv==1)):
        if(down_mv==1):
            track.append([position_of_s[0], position_of_s[1]])
            maze[position_of_s[0]] = list(maze[position_of_s[0]])
            maze[position_of_s[0]][position_of_s[1]] = "t"
            maze[position_of_s[0]] = "".join(maze[position_of_s[0]])
            position_of_s[0] = position_of_s[0] +1
            down_mv=0
        elif(right_mv==1):
            track.append([position_of_s[0], position_of_s[1]])
            maze[position_of_s[0]] = list(maze[position_of_s[0]])
            maze[position_of_s[0]][position_of_s[1]] = "t"
            maze[position_of_s[0]] = "".join(maze[position_of_s[0]])
            position_of_s[1] = position_of_s[1]+1
            right_mv = 0
        elif(left_mv == 1):
            track.append([position_of_s[0], position_of_s[1]])
            maze[position_of_s[0]] = list(maze[position_of_s[0]])
            maze[position_of_s[0]][position_of_s[1]] = "t"
            maze[position_of_s[0]] = "".join(maze[position_of_s[0]])
            position_of_s[1] = position_of_s[1]-1
            left_mv = 0
        elif(up_mv ==1):
            track.append([position_of_s[0], position_of_s[1]])

            maze[position_of_s[0]] = list(maze[position_of_s[0]])
            maze[position_of_s[0]][position_of_s[1]] = "t"
            maze[position_of_s[0]] = "".join(maze[position_of_s[0]])
            position_of_s[0] = position_of_s[0]-1
            up_mv = 0
        else:
            maze[position_of_s[0]] = list(maze[position_of_s[0]])
            maze[position_of_s[0]][position_of_s[1]] = "N"
            maze[position_of_s[0]] = "".join(maze[position_of_s[0]])
            position_of_s = track[len(track)-1]
            track.pop()

    else:
        pass
print("\nThe steps for solution is:- ")
output()
print("\nThe final visual solution of solved maze is: \n")
for i in maze:
    print(i, end="\n")