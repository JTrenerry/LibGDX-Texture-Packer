def main():
    # Get the name of the image
    name = input("The filename of the image: ")
    # How big is a frame THEY MUST ALL BE THE SAME SIZE
    frameSize = input("Size of a single frame (width, height): ")
    # Split the input into seperate values
    frameSizeArray = frameSize.split(',', 1)
    frameHeight = frameSizeArray.pop()
    frameWidth = frameSizeArray.pop()
    # Get the total number of frames
    frameCount = int(input("Amount of frames total: "))
    # How many frames are in a row
    framesPerRow =  int(input("Amount of frames per row (MUST BE CONSISTENT (LAST ROW NOT INCLUDED)): "))
    # Get the frames per column by some math
    framesPerColumn = int(frameCount / framesPerRow)
    # Gets the Spritesheet size by some more math
    imageWidth = framesPerRow * frameWidth
    imageHeight = framesPerColumn * frameHeight
    # Starts the output process
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
