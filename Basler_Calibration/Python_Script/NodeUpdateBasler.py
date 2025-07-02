'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)

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

    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grabResult.GrabSucceeded():
            # Access the image data
            image = converter.Convert(grabResult)
            img = image.GetArray()
            cv2.namedWindow('FromRobot Update', cv2.WINDOW_NORMAL)
            cv2.resizeWindow("FromRobot Update", 824, 600) 
            cv2.imshow('FromRobot Update', img)

            # Wait for 1 millisecond for a key event
            key = cv2.waitKey(1) & 0xFF
    
            # Check if the window is still open
            if cv2.getWindowProperty('FromRobot Update', cv2.WND_PROP_VISIBLE) < 1:
                break

            

        grabResult.Release()
        
    # Releasing the resource
    camera.StopGrabbing()

    cv2.destroyAllWindows()
