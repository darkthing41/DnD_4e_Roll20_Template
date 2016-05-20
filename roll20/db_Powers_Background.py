from .Roll20 import *
from .Template_dnd4epower import *

##GLADIATOR
#--------------------

class Disrupting_Advance(Power_Normal):
    """Disrupting Advance | Gladiator Attack
    w : number of [W] to use (2[W]; 3[W] at 11th level; 4[W] at 21st level)
    """
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "encounter");
        self.w = "[[1+ceil(@{level}/10)]]";
        self.Update(
            {"emote":   "With an attack followed by a violent shove, your enemy flies backward. As it flails for balance, it loses its footing and stumbles into the creatures around it.",
             "keywords":"Martial, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod(self.w),
             "critical":self.Damage_Weapon_Mod_Crit(self.w),
             "hiteffect":   "You push the target 2 squares. The target and each enemy adjacent to the target at the end of the push are slowed until the end of your next turn."
             });
    #end __init__
#end Disrupting_Advance
