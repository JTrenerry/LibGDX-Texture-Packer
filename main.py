# 'Runs the code' that gives the output and writes it to the output file
def output(size: str, name: str, frameHeight: int, frameWidth: int, frameSize: int, framesPerRow: int, frameCount: int):
    # Makes output file
    outputFileName = 'output\\' + name.split(".", 1)[0].strip('.') + ".atlas"
    outputFile = open(outputFileName, "w")
    # Starts the output process
    outputFile.write(name + "\nsize: " + size + "\nformat: RGBA8888\nfilter: Nearest,Nearest\nrepeat: none")
    f = -1
    for i in range(0, frameCount):
        if ((i % framesPerRow) == 0):
            f += 1
        x = frameWidth * (i % framesPerRow)
        y = frameHeight * (f)
        outputFile.write("\ndefault\n  rotate: false\n  xy: " + str(x) + "," + str(y) + "\n  size: " + frameSize + "\n  orig: " + frameSize +"\n  offset: 0,0\n  index: " + str(i))
    return

def main():
    # Get the name of the image
    name = input("The filename of the image (including the extension): ")
    # How big is a frame THEY MUST ALL BE THE SAME SIZE
    frameSize = input("Size of a single frame (width, height): ")
    # Split the input into seperate values
    frameSizeArray = frameSize.split(',', 1)
    frameHeight = int(frameSizeArray.pop())
    frameWidth = int(frameSizeArray.pop())
    # Get the total number of frames
    frameCount = int(input("Amount of frames total: "))
    # How many frames are in a row
    framesPerRow =  int(input("Amount of frames per row (MUST BE CONSISTENT (LAST ROW NOT INCLUDED)): "))
    # Get the frames per column by some math
    framesPerColumn = int(frameCount / framesPerRow)
    # Gets the Spritesheet size by some more math
    imageWidth = framesPerRow * frameWidth
    imageHeight = framesPerColumn * frameHeight
    size = str(imageWidth) + ", " + str(imageHeight)
    output(size, name, frameHeight, frameWidth, frameSize, framesPerRow, frameCount)
    return

if __name__ == "__main__":
    main()
