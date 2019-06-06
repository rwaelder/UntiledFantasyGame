# main with gui

from playerClasses import Warrior, Mage, Sage, Berserker
from enemies import Orc, Goblin, OrcShaman
from attack import Attack
from partyBattle import battle
from loadSave import new_or_load, save_party
from party import *
from item import *
import campaigns 
from shop import Shop

import tkinter as tk


playerParty = new_or_load()


window = tk.Tk()
window.title('Untitled Fantasy Game')




window.mainloop()