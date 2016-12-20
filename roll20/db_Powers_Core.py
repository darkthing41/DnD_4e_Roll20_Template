from .Roll20 import *
from .Template_dnd4epower import *

class _Basic_Attack(Power_Normal):
    """Common Basic Attack
    w : number of [W] to use (1[W], or 2[W] at 21st level)
    """
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.w = "[[1+floor(@{level}/21)]]";
        self.Update(
            {"keywords":    "Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod(self.w),
             "critical":self.Damage_Weapon_Mod_Crit(self.w),
             });
    #end __init__
#end _Basic_Attack

class Melee_Basic_Attack(_Basic_Attack):
    """Melee Basic Attack"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        _Basic_Attack.__init__(self, power_num);
        self.Update(
            {"emote":   "You resort to the simple attack you learned when your first picked up a melee weapon."
             });
    #end __init__
#end Melee_Basic_Attack

class Melee_Basic_Attack_Trained(Melee_Basic_Attack):
    """Melee Basic Attack with Melee Training
    """
    __modifiers = ("constitution", "dexterity", "intelligence", "wisdom", "charisma");

    def __init__(self, power_num, modifier):
        """Initialize self.
        power_num : the power number used for Power attributes
        modifier : the ability modifier to use for the attack, in ("constitution", "dexterity", "intelligence", "wisdom", "charisma")
        """
        Melee_Basic_Attack.__init__(self, power_num);
        assert modifier in Melee_Basic_Attack_Trained.__modifiers;
        mod_attribute = "".join((Attribute(modifier+"-mod"), "[", modifier[:3].upper(), "]"));
        self.Update(
            {"attack":  "".join(("[[1d20+", Attribute("halflevel"), "[level/2]+", mod_attribute, "+", self.Attribute_Power("weapon-attack"), "+", self.Attribute_Power("attack-misc"), "]] vs ", self.Attribute_Power("def"))),
             "damage":  "".join(("[[", self.W(self.w), "+floor(", mod_attribute, "/2)+", self.Attribute_Power("weapon-damage"), "+", self.Attribute_Power("damage-misc"), "]] damage.")),
             "critical":"".join(("[[", self.W_Crit(self.w), "+floor(", mod_attribute, "/2)+", self.Attribute_Power("weapon-damage"), "+", self.Attribute_Power("damage-misc"), "]] damage.")),
             "Melee Training:": "".join(("Using ", modifier.title(), " modifier."))
             });
    #end __init__
#end Melee_Basic_Attack_Trained

class Ranged_Basic_Attack(_Basic_Attack):
    """Ranged Basic Attack"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        _Basic_Attack.__init__(self, power_num);
        self.Update(
            {"emote":   "You resort to the simple attack you learned when your first picked up a ranged weapon."
             });
    #end __init__
#end Ranged_Basic_Attack

class Second_Wind(Power_Normal):
    """Second Wind"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "encounter");
        self.Update(
            {"effect":  "".join(("Spend a healing surge to regain [[", Attribute("surge-value"), "]] hit-points and gain a +2 bonus to all defenses until the start of your next turn.")),
             });
    #end __init__
#end Second_Wind

class Action_Point(Power_Normal):
    """Action Point"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "encounter");
        self.Update(
            {"effect":  "Gain a standard action this turn.",
             });
    #end __init__
#end Action_Point
