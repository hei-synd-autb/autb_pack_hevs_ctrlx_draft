'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
Modified by Cedric.Lenoir@hevs.ch to write a file with time of the image.
'''
from pypylon import pylon
from datetime import datetime
import cv2

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
camera.ExposureAuto.SetValue("Continuous") # TODO : tester si le paramétre est bien changé !
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

def getOnePicture():
    img=None
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()

    grabResult.Release()

    return img


if __name__ == "__main__":

    # One Shot
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
            # Access the image data
            image = converter.Convert(grabResult)
            img = image.GetArray()
            cv2.namedWindow('FromRobot One Shot', cv2.WINDOW_NORMAL)

            # Get image size
            print(f"Image Width is {img.shape[1]}")
            print(f"Image Height is {img.shape[0]}")

            # Get time
            now = datetime.now()
            print(f"Today's Time is: , {now.hour}_{now.minute}_{now.second}")
            
            # Using resizeWindow() 
            # cv2.resizeWindow("FromRobot One Shot", 412, 300) 
            cv2.resizeWindow("FromRobot One Shot", 824, 600) 

            # Show the image on the scree
            cv2.imshow('FromRobot One Shot', img)

            # Using cv2.imwrite() method
            # Saving the image
            filename = f"C:/Users/cedric.lenoir/Documents/AutRob/imgRobot/OneShot_{now.hour}_{now.minute}_{now.second}.jpg"
            cv2.imwrite(filename, img)
            print(f"Written image in {filename}")

            # Wait until the user closes the window
            while True:
                # Wait for 1 millisecond for a key event
                key = cv2.waitKey(1) & 0xFF
    
                # Check if the window is still open
                if cv2.getWindowProperty('FromRobot One Shot', cv2.WND_PROP_VISIBLE) < 1:
                    break         
        
    # Releasing the resource
    camera.StopGrabbing()

    cv2.destroyAllWindows()
