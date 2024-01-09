command = ''
carIsStarted = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if carIsStarted:
            print("Car is already Started")
        else:
            carIsStarted = True
            print('Car Started')
    elif command == 'stop':
        if not carIsStarted:
            print('Car is already Stopped')
        else:
            carIsStarted = False
            print("Car Stopped")
    elif command == 'help':
        print("""
start = start the car
stop = stop the car
quit = exit the game
""")
    elif command == 'quit':
        break
    else:
        print("I don't understand")