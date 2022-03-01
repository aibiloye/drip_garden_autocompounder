import pyautogui
import time
import sys
import os

pth = os.path.abspath(__file__)
root = os.path.abspath(os.path.join(pth, os.pardir))
images_path = os.path.join(root,'images\\')
print(images_path)

#Searches for the image
def see_if_ready():
    while True:
        try:
            image = pyautogui.locateOnScreen(images_path + 'plant_ready.png')
            while image == None:
                image = pyautogui.locateOnScreen(images_path + "plant_ready.png")
                print("Your plants are not ready to harvest yet....")
                print('Looking for plants to harvest....\n\n')
                print('No Plants Found - Checking again in 300 seconds')

                time.sleep(300)
            pyautogui.click(images_path + 'plant_ready.png')
            print('Detected that plants are ready for harvest')
            print('clicking on harvest')
            break
        except:
            print('Hit an error in the see_if_ready loop ....')


def click_compound():
            while True:
                try:
                    print('looking ............')
                    image = pyautogui.locateOnScreen(images_path + "plant_seeds.png", confidence=0.7)
                    while image == None:
                        image = pyautogui.locateOnScreen(images_path + "plant_seeds.png", confidence=0.7)
                        pyautogui.scroll(-300)
                        time.sleep(1)
                        print('didnt find the image')
                    time.sleep(2)
                    image = pyautogui.locateOnScreen(images_path + "plant_seeds.png", confidence=0.7)
                    pyautogui.click(image)
                    print('Clicked on Plant Seeds... ')
                    time.sleep(3)
                    pyautogui.scroll(10000)
                    break
                except:
                    print('Hit an error in the click_compound loop ....')


def metamask():
    while True:
        try:
            print('Waiting for MM to open')
            print('Checking for correct contract address')
            image = pyautogui.locateOnScreen(images_path + "meta_mask.png", confidence=0.7)
            while image == None:
                image = pyautogui.locateOnScreen(images_path + "meta_mask.png", confidence=0.7)
                time.sleep(1)
            address = pyautogui.locateOnScreen(images_path + "security.png", confidence=0.7)
            if address == None:
                sys.exit('The Code did not detect the correct contract.... Exiting the program for your safety')
            pyautogui.click(image)
            pyautogui.scroll(-500)
            time.sleep(1)
            image = pyautogui.locateOnScreen(images_path + "confirm.png", confidence=0.7)
            pyautogui.click(image)
            break
        except:
            print('Hit an error in the metamask loop ....')


def main():
    while True:
        see_if_ready()
        click_compound()
        metamask()
        print('Successfully Compounded. Sleeping for 45 seconds so the UI can update...')
        time.sleep(45)

main()
