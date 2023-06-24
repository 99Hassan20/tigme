from pynput.mouse import Controller

def dont_move():
    mouse = Controller()
    init_x ,init_y = mouse.position
    while True:
        current_x, current_y = mouse.position
        print(current_x, current_y)
        if current_x != init_x or current_y != init_y:
            print("go to sleep")
            return 1

if __name__ == "__main__":
   dont_move()
