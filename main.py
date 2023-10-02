from tkinter import *
import tkinter as tk

import os
from WinMng import WinMng

class TournamentManager:

    '''
    ###
    path='TournamentFIles\\sasa'
    os.makedirs(path)

    ###
    '''
    ## rando time calculating code
    def run():


        window=Tk()
        window.geometry('1080x720')
        window.iconbitmap("logo.ico")
        widgets=[]
        winManage=WinMng
        winManage.init(window,widgets)
        winManage.tab1()
        window.mainloop()

