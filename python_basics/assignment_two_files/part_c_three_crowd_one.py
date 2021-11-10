## Part C
#TODO: Three is a Crowd
def crowd_test(room):
    if len(room) > 3:
        print('The room is crowded with {} people in it'.format(len(room)))
peopleInRoom = ['John','James','Jack','Jill']
crowd_test(peopleInRoom)
peopleInRoom.pop()
peopleInRoom.pop()
crowd_test(peopleInRoom)