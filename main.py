# 'Runs the code' that gives the output and writes it to the output file
def output(size: str, name: str, frameHeight: int, frameWidth: int, frameSize: int, framesPerRow: int, frameCount: int, animationDets):
    # Makes output file
    outputFileName = 'output\\' + name.split(".", 1)[0].strip('.') + ".atlas"
    outputFile = open(outputFileName, "w")
    # Starts the output process
    outputFile.write(name + "\nsize: " + size + "\nformat: RGBA8888\nfilter: Nearest,Nearest\nrepeat: none")
    animationNumber = 0
    index = 0
    k = -1
    for i in range(0, frameCount):
        if ((i % framesPerRow) == 0):
            k += 1
        if (animationDets[animationNumber][1] == index):
            animationNumber += 1
            index = 0
        x = frameWidth * (i % framesPerRow)
        y = frameHeight * (k)
        outputFile.write("\n" + animationDets[animationNumber][0] + "\n  rotate: false\n  xy: " + str(x) + ","
                         + str(y) + "\n  size: " + frameSize + "\n  orig: " + frameSize +"\n  offset: 0,0\n  index: " + str(index))
        index += 1
    return

def main():
    # In this file because I want a GUI eventually but it can wait til basic shit is done <3
    
    ##### GENERAL INFORMATION ABOUT THE SPRITE SHEET #####
    # Get the name of the image
    name = input("The filename of the image (including the extension): ")
    # How big is a frame THEY MUST ALL BE THE SAME SIZE
    frameSize = input("Size of a single frame (width, height): ")
    # How many frames are in a row
    framesPerRow =  int(input("Amount of frames per row (MUST BE CONSISTENT (LAST ROW NOT INCLUDED)): "))
    ##### GETTING INDIVIDUAL ANIMATION DETAILS #####
    animationNamesAndSizes = list()
    frameCount = 0
    while True:
        animationName = input("Animation name: ")
        if animationName == "":
            break
        animationFrames = int(input("Length of animation (in frames): "))
        frameCount += animationFrames
        animationNamesAndSizes.append((animationName, animationFrames))
    # Split the input into seperate values
    frameSizeArray = frameSize.split(',', 1)
    frameHeight = int(frameSizeArray.pop())
    frameWidth = int(frameSizeArray.pop())

    # Get the frames per column by some math
    framesPerColumn = int(frameCount / framesPerRow)
    # Gets the Spritesheet size by some more math
    imageWidth = framesPerRow * frameWidth
    imageHeight = framesPerColumn * frameHeight
    size = str(imageWidth) + ", " + str(imageHeight)
    output(size, name, frameHeight, frameWidth, frameSize, framesPerRow, frameCount, animationNamesAndSizes)
    return

if __name__ == "__main__":
    main()
