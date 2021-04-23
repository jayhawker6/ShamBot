while True:
    global realinput
    try:
        realinput = input("Play Either R, P, or S: ")
    except ValueError:
        print("")
    if realinput == 'R':
        print('Human: Rock')
        print('Robot: Paper')
        input('Robot Wins!')
        continue
    if realinput == 'P':
        print('Human: Paper')
        print('Robot: Scissors')
        input('Robot Wins!')
        continue
    if realinput == 'S':
        print('Human: Scissors')
        print('Robot: Rock')
        print('Robot Wins!')
        continue
    else:
        continue