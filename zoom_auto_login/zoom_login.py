import os
import pandas as pd
import pyautogui
import time
from datetime import datetime

files_path="C:\\Users\\username\\PycharmProjects\\zoom_meeting_data\\"


def signIn(meeting_id, password):
    os.startfile('C:\\Users\\username\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    time.sleep(3)

    join_btn=pyautogui.locateCenterOnScreen(files_path+"joinameeting.png")
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(1)

    meeting_id_btn=pyautogui.locateCenterOnScreen(files_path+"meetingid.png")
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.write(meeting_id)
    time.sleep(2)

    for i in range(2):
        media_btn=pyautogui.locateCenterOnScreen(files_path+"media.png")
        #for btn_1 in media_btn:
        pyautogui.moveTo(media_btn)
        pyautogui.click()
        time.sleep(1)

    join=pyautogui.locateCenterOnScreen(files_path+"join.png")
    pyautogui.moveTo(join)
    pyautogui.click()
    time.sleep(2)

    passcode=pyautogui.locateCenterOnScreen(files_path+"meetingpasscode.png")
    pyautogui.moveTo(passcode)
    pyautogui.write(password)
    time.sleep(5)

    join_meeting=pyautogui.locateCenterOnScreen(files_path+"joinmeeting.png")
    pyautogui.moveTo(join_meeting)
    pyautogui.click()
    time.sleep(1)


if __name__ == "__main__":
    df=pd.read_excel(files_path+'join_timings.xlsx')
    while True:
        now=datetime.now().strftime("%H:%M")
        if now in str(df['Timings']):
            mylist=df["Timings"]
            mylist=[i.strftime("%H:%M") for i in mylist]
            c=[i for i in range(len(mylist)) if mylist[i] == now]
            row=df.loc[c]
            meeting_id=str(row.iloc[0,1])
            password=str(row.iloc[0,2])
            time.sleep(5)
            signIn(meeting_id, password)
            time.sleep(2)
            print('signed in')
            break

