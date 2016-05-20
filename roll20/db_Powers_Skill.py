from .Roll20 import *
from .Template_dnd4epower import *

##UTILITY POWERS
#--------------------

#Level 2

#Level 6

class Physicians_Care(Power_Normal):
    """Physician's Care | Heal Utility 6"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "encounter");
        self.Update(
            {"emote":   "Your extensive training helps you get an ally back into the fight.",
             "keywords":"Healing",
             "target":  "You or one ally",
             "effect":  "The target can spend a healing surge.",
             });
    #end __init__
#end Physicians_Care

#Level 10

class Enter_The_Crucible(Power_Normal):
    """Enter the Crucible | Endurance Utility 10"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "daily");
        self.Update(
            {"requirement": "You must have at least one healing surge remaining.",
             "effect":  "You lose a healing surge. Until the end of the encounter, you cannot be weakened, and you gain resist 10 to all damage."
             });
    #end __init__
#end Enter_The_Crucible
