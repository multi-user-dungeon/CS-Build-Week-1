from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

f = open('RoomNames.txt', 'r')
room_names_file = f.read().split("\n")
f.close()

roomName = 1 
room_names_dict = {}
x = 1

while x <= 100:
    for name in room_names_file:
        room_names_dict.update({x :f'{name}'})
        x+=1

# print(room_names_dict)
# print (f'this is room 3 {room_names_dict[3]}')

size_y = 15
size_x = 15
num_rooms = 110

grid = [None] * size_y
width = size_x
height = size_y
for i in range(len(grid)):
    grid[i] = [None] * size_x

x = -1 
y = 0 
room_count = 0

direction = 1  


previous_room = None
while room_count < num_rooms:
    if direction > 0 and x < size_x - 1:
        room_direction = "e"
        reverse_direction = "w"
        x += 1
    elif direction < 0 and x > 0:
        room_direction = "w"
        reverse_direction = "e"
        x -= 1
    else:
        room_direction = "n"
        reverse_direction = "s"
        y += 1
        direction *= -1
    room = Room(id = room_count+1, title = f"Room: {room_names_dict[roomName]}",
                description = f"This is: {room_names_dict[roomName]}.", x = x, y = y)
    
    grid[y][x] = room
   
    room.save()
    roomName +=1
    if previous_room is not None:
        previous_room.connectRooms(room, room_direction)
        room.connectRooms(previous_room, reverse_direction)
    previous_room = room
    room_count += 1

players = Player.objects.all()
for p in players:
    p.currentRoom = 1
    p.save()


