import cv2
from PIL import Image
import os

def video_to_frames():
    capture = cv2.VideoCapture("C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/badAppleVideo/【東方】Bad Apple!! ＰＶ【影絵】.mp4")
    count = 0

    while(capture.isOpened()):
        success, frame = capture.read()
        if success == False:
            break


        cv2.imwrite(f"C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/badAppleFrames/frame_{count:04d}.png", frame)
        count += 1

        print(f"frame {count}")

def resize(img):
    image = Image.open(img)
    new_image = image.resize((255, 255))
    new_image.save(img)

def check_frame_size(img):
    image = Image.open(f"C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/badAppleFrames/{img}")
    if 255 in image.size:
        print(img)
    print(f"checking {img}")

def rename_better(files):
    count = 0

    for file in files:
        os.rename(f"C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/JGrasp terminal printer/badAppleFrames/{file}", f"C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/JGrasp terminal printer/badAppleFrames/frame_{count:04d}.png")
        count += 1       
        print(f"renaming {count} out of {len(files)}")
    print("done renaming!")



video_to_frames()

#disregard 
# frames = os.listdir("C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/JGrasp terminal printer/badAppleFrames")

# rename_better(frames[:10])
# for x in frames:
    # check_frame_size(x)
    # print(f"resizing {x} ...")
    # resize(f"C:/Users/owner/2024 codes/game/Bad Apple/JprogProj/badAppleFrames - Copy/{x}")

# print(f"done resizing {len(frames)} frames. ")
