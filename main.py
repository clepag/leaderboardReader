import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
from pynput.mouse import Controller
import csv
import time
import re
from difflib import SequenceMatcher
import datetime

already_placed = True

weapon_map = {'S': 'Sword',
              'A': 'Axe',
              'H': 'Hammer',
              'C': 'Chainblades',
              'P': 'Warpike',
              'R': 'Repeaters',
              'K': 'Strikers'}

device_map = {
    'PC': 'PC',
    'PS': 'PlayStation',
    'XB': 'XBOX',
    'SW': 'Switch'
}


def filterSymbol(small_image, large_image, text="", offset_x=0):
    # Filter device and completed goals
    method = cv2.TM_CCOEFF_NORMED
    result = cv2.matchTemplate(large_image, small_image, method)

    threshold = 0.9

    loc = nm.where(result >= threshold)
    trows, tcols = small_image.shape[:2]

    font = cv2.FONT_HERSHEY_PLAIN

    for pt in zip(*loc[::-1]):
        coord_x, coord_y = pt
        cv2.rectangle(large_image, (coord_x - 3, coord_y - 17), (coord_x + tcols, coord_y + trows + 17), (0, 0, 0), -1)
        if text != "":
            cv2.putText(large_image, text, (coord_x + offset_x, coord_y + 35), font, 3, (255, 255, 255), 2, cv2.LINE_AA)

    # cv2.imshow('filtered', large_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def getImage(weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, weapon7, omnicell1, omnicell2, omnicell3, omnicell4,
             omnicell5, device1, device2, device3, device4, goals, y_value):
    # Make screenshot, filter Symbols and apply preprocessing
    cap = ImageGrab.grab(bbox=(900, 550, 2200, y_value))

    gray = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)

    filterSymbol(goals, gray)
    filterSymbol(device1, gray, "PC", 70)
    filterSymbol(device2, gray, "PS", 70)
    filterSymbol(device3, gray, "XB", 70)
    filterSymbol(device4, gray, "SW", 70)

    filterSymbol(weapon1, gray, "S")
    filterSymbol(weapon2, gray, "A")
    filterSymbol(weapon3, gray, "H")
    filterSymbol(weapon4, gray, "C")
    filterSymbol(weapon5, gray, "P")
    filterSymbol(weapon6, gray, "R")
    filterSymbol(weapon7, gray, "K")

    filterSymbol(omnicell1, gray)  # , "B")
    filterSymbol(omnicell2, gray)  # , "R")
    filterSymbol(omnicell3, gray)  # , "T")
    filterSymbol(omnicell4, gray)  # , "I")
    filterSymbol(omnicell5, gray)  # , "D")

    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_TOZERO)
    # reverse = cv2.bitwise_not(thresh)
    resize = cv2.resize(thresh, (0, 0), fx=1.5, fy=1.5)

    # kernel = nm.ones((1, 1), nm.uint8)
    # dilation = cv2.dilate(resize, kernel, iterations=10)
    # cv2.imshow('cap', nm.array(cap))
    # cv2.imshow('gray', gray)
    # cv2.imshow('thresh', thresh1)
    # cv2.imshow('resize', resize)
    # cv2.imshow('dilation', dilation)
    # cv2.imshow('reverse', reverse)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return resize


def imToString(image, leaderboard_data):
    pattern = re.compile("^([0-9][0-9]:[0-5][0-9])$")

    custom_oem_psm_config = r'--dpi 1000 --oem 3 --psm 6'
    # tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(gray), cv2.COLOR_BGR2GRAY), langu = 'eng+chi_sim+chi_tra+jpn+deu+spa+fra', config=custom_oem_psm_config)
    tesstr = pytesseract.image_to_string(image, lang='eng+chi_sim+chi_tra+jpn+deu+spa+fra',
                                         config=custom_oem_psm_config)
    print(tesstr)
    lines = tesstr.split('\n')
    lines.pop()
    for line in lines:
        elements = line.split(' ')
        time = elements[(len(elements) - 1)]
        if bool(re.match(pattern, time)):
            name = ""
            for i in range(1, len(elements) - 2):
                name = name + elements[i]
            if name == "":
                name = elements[1]

            data_already_read = False
            skip_after_2_more = False
            skip_counter = 0

            for x in reversed(leaderboard_data):
                if skip_counter == 2:
                    break

                if skip_after_2_more == True:
                    skip_counter += 1

                if int(time.replace(':', '')) < int(x[3].replace(':', '')):
                    skip_after_2_more = True

                if x[3] == time and SequenceMatcher(None, x[1], name).ratio() > 0.8:
                    data_already_read = True
                    print("duplicate found for: ", name)
                    print("as duplicate of: ", x[1])
                    break

            if data_already_read == False:
                line_entry = [weapon_map.get(elements[0]), name, device_map.get(elements[(len(elements) - 2)]),
                              elements[(len(elements) - 1)]]
                leaderboard_data.append(line_entry)


if __name__ == '__main__':

    mouse = Controller()
    fields = ['Weapon', 'Name', 'Device', 'Time']
    leaderboard_data = []

    if already_placed == True:
        y_value = 1200
        scroll_val = -19
        iterations = 15
    else:
        y_value = 1230
        scroll_val = -19
        iterations = 15

    sword = cv2.imread('images/sword.png', 0)
    axe = cv2.imread('images/axe.png', 0)
    hammer = cv2.imread('images/hammer.png', 0)
    chainblades = cv2.imread('images/chainblades.png', 0)
    pike = cv2.imread('images/pike.png', 0)
    repeaters = cv2.imread('images/repeater.png', 0)
    strikers = cv2.imread('images/strikers.png', 0)

    bastion = cv2.imread('images/bastion.png', 0)
    revenant = cv2.imread('images/revenant.png', 0)
    tempest = cv2.imread('images/tempest.png', 0)
    iceborne = cv2.imread('images/iceborne.png', 0)
    discipline = cv2.imread('images/discipline.png', 0)

    pc = cv2.imread('images/pc.png', 0)
    ps = cv2.imread('images/ps.png', 0)
    xbox = cv2.imread('images/xbox.png', 0)
    switch = cv2.imread('images/switch.png', 0)

    goal = cv2.imread('images/goal.png', 0)

    # image = getImage(sword, axe, hammer, chainblades, pike, repeaters, strikers,
    #                  bastion, revenant, tempest, iceborne, discipline,
    #                  pc, ps, xbox, switch, goal, y_value)
    #
    # imToString(image, leaderboard_data)

    for i in range(0, iterations):
        mouse.position = (0, 0)
        image = getImage(sword, axe, hammer, chainblades, pike, repeaters, strikers,
                         bastion, revenant, tempest, iceborne, discipline,
                         pc, ps, xbox, switch, goal, y_value)
        imToString(image, leaderboard_data)
        mouse.position = (1200, 600)
        mouse.scroll(0, scroll_val)
        time.sleep(0.3)
    mouse.position = (1200, 600)
    mouse.scroll(0, 500)

    print("leaderboard data: ", leaderboard_data)
    filename = "board_data/leaderboard" + str(datetime.datetime.now()).replace(' ', '_').replace(':', '_').split('.')[
        0] + ".csv"
    with open(filename, 'w', encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(leaderboard_data)
