import pyautogui
import time
import sys


#Searches for the image
def see_if_ready():
    while True:
        try:
            image = pyautogui.locateOnScreen("images/plant_ready.png")
            while image == None:
                image = pyautogui.locateOnScreen("images/plant_ready.png")
                print("Your plants are not ready to harvest yet....")
                print('Looking for plants to harvest....\n\n')
                print('No Plants Found - Checking again in 2 minutes')

                time.sleep(300)
            pyautogui.click('images/plant_ready.png')
            print('Detected that plants are ready for harvest')
            print('clicking on harvest')
            break
        except:
            pass

def click_compound():
            while True:
                try:
                    print('looking ............')
                    image = pyautogui.locateOnScreen("images/plant_seeds.png",confidence=0.7)
                    while image == None:
                        image = pyautogui.locateOnScreen("images/plant_seeds.png", confidence=0.7)
                        pyautogui.scroll(-300)
                        time.sleep(1)
                        print('didnt find the image')
                    time.sleep(2)
                    image = pyautogui.locateOnScreen("images/plant_seeds.png", confidence=0.7)
                    pyautogui.click(image)
                    print('Clicked on Plant Seeds... ')
                    time.sleep(3)
                    pyautogui.scroll(10000)
                    break
                except:
                    pass


def metamask():
    while True:
        try:
            print('Waiting for MM to open')
            print('Checking for correct contract address')
            image = pyautogui.locateOnScreen("images/meta_mask.png", confidence=0.7)
            while image == None:
                image = pyautogui.locateOnScreen("images/meta_mask.png", confidence=0.7)
                time.sleep(1)
            address = pyautogui.locateOnScreen("images/security.png")
            if address == None:
                sys.exit('The Code did not detect the correct contract.... Exiting the program for your safety')
            pyautogui.click(image)
            pyautogui.scroll(-500)
            time.sleep(1)
            image = pyautogui.locateOnScreen("images/confirm.png", confidence=0.7)
            pyautogui.click(image)
            break
        except:
            pass


def main():
    while True:
        see_if_ready()
        click_compound()
        metamask()
        print('Successfully Compounded. Sleeping for 45 seconds so the UI can update...')
        time.sleep(45)

main()
