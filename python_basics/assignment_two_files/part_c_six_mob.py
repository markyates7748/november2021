#TODO: Six is a Mob
def crowd_test(room):
    if len(room) > 5:
        print('The room is a mob with {} people in it'.format(len(room)))
    elif len(room) >= 3:
        print('The room is crowded with {} people in it'.format(len(room)))
    elif len(room) >= 1:
        print('The room is not very crowded with {} people in it'.format(len(room)))
    else:
        print('The room is empty')
peopleInRoom = ['John','James','Jack','Jill','Janet','Jesse']
crowd_test(peopleInRoom)
peopleInRoom.pop()
crowd_test(peopleInRoom)
peopleInRoom.pop()
peopleInRoom.pop()
peopleInRoom.pop()
crowd_test(peopleInRoom)
peopleInRoom.pop()
peopleInRoom.pop()
crowd_test(peopleInRoom)