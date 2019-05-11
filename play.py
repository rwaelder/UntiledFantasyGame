# main thing

from playerClasses import Warrior, Mage, Sage, Berserker
from enemies import Orc, Goblin, OrcShaman
from attack import Attack
from partyBattle import battle
from loadSave import new_or_load, save_party
from party import *
from item import *
import campaigns 

print('\n\n')
print('--------------------------------------------------------------')
print('-------------- Welcome to Untitled Fantasy Game --------------')
print('--------------------------------------------------------------')
print('--------------------------------------------------------------')
print('------------------- Press any key to play --------------------')
print('--------------------------------------------------------------')
input('\n\n')



playerParty = new_or_load()
playerParty.add_item(Spear(5))

# enemies = [OrcShaman(1), Orc(1), Goblin(1)]
# enemyParty = Party(enemies)


campaigns.choose_campaign(playerParty)

save_party(playerParty)