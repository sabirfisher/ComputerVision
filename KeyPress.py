import pygame 

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400)) #the window size

def getKey(keyName):
    ans = False
    for evbe in pygame.event.get(): pass

    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))

    if keyInput[myKey]:
        ans = True
    pygame.display.update()

    return ans
#if the key is pressed it will return true if not then it will be false

def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")


if __name__ == '__main__':
    init()
    while True:
        main()