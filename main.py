def main():
    name = input("Name of the file (with file extension):")
    size = input("Size of the entire image (width, height)")
    frameSize = input("Size of a single frame (width, height)")
    frameSizeArray = frameSize.split(',', 1)
    frameRow = frameSizeArray.pop()
    frameWidth = frameSizeArray.pop()
    frameCount = int(input("Amount of frames total"))
    # Can be done by math for later verisons row size / frame size (width wise)
    framesPerRow = int(input("Amount of frames per row (width, height)"))
    print(name + "\nsize: " + size + "\nformat: RGBA8888\nfilter: Nearest,Nearest\nrepeat: none")
    f = -1
    for i in range(0, frameCount):
        if ((i % framesPerRow) == 0):
            f += 1
        x = 360 * (i % framesPerRow)
        y = 180 * (f)
        print("default\nrotate: false\nxy: " + str(x) + "," + str(y) + "\nsize: " + frameSize + "\norig: " + frameSize +"\noffset: 0,0\nindex: " + str(i))
    return

if __name__ == "__main__":
    main()
