from .Roll20 import *
from .Template_dnd4epower import *

##CLASS FEATURES
#--------------------

class Battleminds_Demand(Power_Normal):
    """Battlemind's Demand | Battlemind Feature"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "You draw your foe's concentration, taunting the foe to strike at you.",
             "keywords":"Augmentable, Psionic",
             "target":  "One creature in burst",
             "effect":  "You mark the target until you use this power again or until the end of the encounter.",
             "augmenttoggle":   RollQuery_Augment("1"),
             "augment1target":  "One or two creatures in burst"
             });
    #end __init__
#end Battleminds_Demand

class Blurred_Step(Power_Normal):
    """Blurred Step | Battlemind Feature"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "You bend reality with the power of your mind, flashing across the space between you and your enemy.",
             "keywords":"Psionic",
             "trigger": "An adjacent enemy marked by you shifts",
             "effect":  "You shift 1 square.",
             "special": "You can use this power only once per turn."
             });
    #end __init__
#end Blurred_Step

class Mind_Spike(Power_Normal):
    """Mind Spike | Battlemind Feature"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "You force the enemy to feel the pain that it inflicts on your friend.",
             "keywords":"Force, Psionic, Psychic",
             "trigger": "An adjacent enemy marked by you deals damage to your ally with an attack that doesn't include you as a target.",
             "target":  "The triggering enemy",
             "effect":  "The target takes force and psychic damage equal to the damage that its attack dealt to your ally.",
             });
    #end __init__
#end Mind_Spike

class Persistent_Harrier(Power_Normal):
    """Persistent Harrier | Battlemind Feature
    w : number of [W] to use (1[W], or 2[W] at 21st level)
    """
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "encounter");
        self.w = "[[1+floor(@{level}/21)]]";
        self.Update(
            {"emote":   "You slip the bonds of space to strike back at even a distant opponent.",
             "keywords":"Psionic, Teleportation, Weapon",
             "trigger": "An enemy hits you or misses you with an attack for the first time during an encounter",
             "target":  "The triggering enemy",
             "special": "You can attack the target with this melee attack even if the target is outside your melee reach.",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod(self.w),
             "critical":self.Damage_Weapon_Mod_Crit(self.w),
             "hiteffect":   "You teleport to a square adjacent to the enemy."
             });
    #end __init__
#end Persistent_Harrier


##AT-WILL ATTACK POWERS
#--------------------

#Level 1

class Bulls_Strength(Power_Normal):
    """Bull's Strength | Battlemind Attack 1"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "You slam your foe back as if it were a puny goblin. By enhancing your strength further, you can reach enemies further away or even swat multiple foes.",
             "keywords":    "Augmentable, Psionic, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("1"),
             "critical":self.Damage_Weapon_Mod_Crit("1"),
             "hiteffect":  "You push the target 1 square.",
             "augmenttoggle":   RollQuery_Augment("1","2"),
             "augment1range":   "**Special:** Your range increases by 1 for this attack.",
             "augment2range":   "Close blast 3",
             "augment2target":  "Each enemy you can see in blast"
             });
    #end __init__
#end Bulls_Strength

class Concussive_Spike(Power_Normal):
    """Concussive_Spike | Battlemind Attack 1"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "Your weapon shimmers with force as you bring it crashing down, clobbering your foes and driving some of them back.",
             "keywords":"Augmentable, Force, Psionic, Weapon",
             "target":  "One creature you can see in blast",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("1", "force"),
             "critical":self.Damage_Weapon_Mod_Crit("1", "force"),
             "hiteffect":   "".join(("You push each enemy in the blast other than the target a number of squares equal to 1 + your Charisma modifier (+[[", Attribute("charisma-mod"), "[CHA]]]).")),
             "augmenttoggle":   RollQuery_Augment("1","2"),
             "augment1range":   "Close burst 3",
             "augment1target":  "One creature you can see in burst",
             "augment1hiteffect":   "".join(("You push one enemy in the burst other than the target a number of squares equal to 1 + your Charisma modifier (+[[", Attribute("charisma-mod"), "[CHA]]]).")),
             "augment2hiteffect":   "".join(("You knock the target prone. You push each enemy in the blast other than the target a number of squares equal to 1 + your Charisma modifier (+[[", Attribute("charisma-mod"), "[CHA]]]).")),
             });
    #end __init__
#end Concussive_Spike

class Iron_Fist(Power_Normal):
    """Iron Fist | Battlemind Attack 1"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "You change the density of your hand and arm to that of iron, allowing you to ward off your foe's attacks.",
             "keywords":"Augmentable, Psionic, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("1"),
             "critical":self.Damage_Weapon_Mod_Crit("1"),
             "effect":  "".join(("Until the end of your next turn, you gain resistance to all damage equal to your Wisdom modifier (+[[", Attribute("wisdom-mod"), "[WIS]]]).")),
             "augmenttoggle":   RollQuery_Augment("1","2"),
             "augment1hiteffect":   "".join(("**Effect:** Until the end of your next turn, you gain fire resistance equal to 5 + your Wisdom modifier (+[[", Attribute("wisdom-mod"), "[WIS]]]).")),
             "augment2damage":  "".join(("[[", self.W("2"), "+", self.Attribute_Power("damage"), "]] damage.")),
             "augment2critical":  "".join(("[[", self.W_Crit("2"), "+", self.Attribute_Power("damage"), "]] damage."))
             });
    #end __init__
#end Iron_Fist

#Level 3

#Level 7

class Psionic_Speed(Power_Normal):
    """Psionic Speed | Battlemind Attack 7"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "You move in a blur, making a series of quick attacks that force your opponents to regard you as a threat.",
             "keywords":"Augmentable, Psionic, Weapon",
             "target":  "One, two, or three creatures",
             "attack":  "".join(("".join(("[[1d20+", self.Attribute_Power("attack"), "]]"))*3, " vs ", self.Attribute_Power("def"))),
             "damage":  "".join(("".join(("[[", self.W("1"), "+", self.Attribute_Power("weapon-damage"), "+", self.Attribute_Power("damage-misc"), "]]"))*3, " damage.")),
             "critical":"".join(("[[", self.W_Crit("1"), "+", self.Attribute_Power("weapon-damage"), "+", self.Attribute_Power("damage-misc"), "]] damage.")),
             "hiteffect":   "You mark the target until the end of your next turn.",
             "augmenttoggle":   RollQuery_Augment("1","2"),
             "augment1hiteffect":   "**Effect:** After both the first and second attacks, you shift 1 square to a square adjacent to the next target.",
             "augment2damage":  "".join(("+ Constitution modifier (+[[", Attribute("constitution-mod"), "[CON]]]) damage.")),
             "augment2hiteffect":   "**Effect:** You mark the target until the end of your next turn.",
             });
    #end __init__
#end Psionic_Speed

#Level 13

class Intellect_Snap(Power_Normal):
    """Intellect Snap | Battlemind Attack 13"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "Your weapon channels your psychic fury to distract and hinder your foe.",
             "keywords":"Augmentable, Psionic, Psychic, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("0", "psychic"),
             "critical":self.Damage_Weapon_Mod_Crit("0", "psychic"),
             "hiteffect":   "The target is dazed until the start of your next turn.",
             "augmenttoggle":   RollQuery_Augment("1","4"),
             "augment1hiteffect":   "As above, and you are no longer dazed or marked.",
             "augment4damage":  self.Damage_Weapon_Mod("2", "psychic"),
             "augment4critical":self.Damage_Weapon_Mod_Crit("2", "psychic"),
             "augment4hiteffect":   "The target is dazed until the end of your next turn. In addition, you or one ally within 5 squares of you can make a saving throw against an effect that dazes or stuns.",
             });
    #end __init__
#end Intellect_Snap


##DAILY ATTACK POWERS
#--------------------

#Level 1

class Aspect_Of_Elevated_Harmony(Power_Normal):
    """Aspect of Elevated Harmony | Battlemind Attack 1"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "daily");
        self.Update(
            {"emote":   "Your eyes glow as you achieve harmony of mind, body, and spirit. In this state, you are able to heal yourself, and you can understand where to strike your enemy best and how to lessen its blows.",
             "keywords":"Healing, Polymorph, Psionic, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("2"),
             "critical":self.Damage_Weapon_Mod_Crit("2"),
             "miss":    "Half damage.",
             "effect":  "You can spend a healing surge. You then assume the aspect of elevated harmony until the end of the encounter. While in this aspect, you can use the following augmentation with your battlemind at-will attack powers that are augmentable. This augmentation is in addition to the effects that an at-will power might have; this augmentation doesn't supersede them.",
             "**Augment 1**":   "",
             "**Effect:**": "".join(("You gain temporary hit points equal to 5 + your Wisdom modifier (+[[", Attribute("wisdom-mod"), "[WIS]]]). In addition, choose a single creature hit by the at-will attack. That creature takes extra damage equal to your Wisdom modifier (+[[", Attribute("wisdom-mod"), "[WIS]]])."))
             });
    #end __init__
#end Aspect_Of_Elevated_Harmony

#Level 5

class Beckoning_Strike(Power_Normal):
    """Beckoning Strike | Battlemind Attack 5"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "daily");
        self.Update(
            {"emote":   "As you strike your enemy, you unleash a surge of psionic energy that warps the minds of the foes you challenge, compelling them to approach you.",
             "keywords":"Psionic, Stance, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("2"),
             "critical":self.Damage_Weapon_Mod_Crit("2"),
             "miss":    "Half damage.",
             "effect":  "You assume the beckoning stance. Until the stance ends, you can use the Beckoning Strike Attack power."
             });
    #end __init__
#end Beckoning_Strike
class Beckoning_Strike_Attack(Power_Normal):
    """Beckoning_Strike_Attack | """
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"keywords":"Psionic, Weapon",
             "requirement": "The power Beckoning Strike must be active in order to use this power.",
             "trigger": "An adjacent enemy marked by you moves without shifting on its turn",
             "target":  "The triggering enemy",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("1"),
             "critical":self.Damage_Weapon_Mod_Crit("1"),
             "hiteffect":   "At the end of the target's turn, you can use a free action to pull the target a number of squares equal to its speed."
             });
    #end __init__
#end Beckoning_Strike_Attack

#Level 9

class Iron_Tomb(Power_Normal):
    """Iron Tomb | Battlemind Attack 9"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "daily");
        self.Update(
            {"emote":   "Psionic energy cascades from your weapon as you strike your foe, transforming the enemy into a statue of iron.",
             "keywords":"Polymorph, Psionic, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "hiteffect":   "The target is stunned and immune to all damage but psychic damage (save ends both).",
             "miss":    "The target is stunned and immune to all damage but psychic damage until the end of your next turn."
             });
    #end __init__
#end Iron_Tomb


##UTILITY POWERS
#--------------------

#Level 2

class Feather_Step(Power_Normal):
    """Feather Step | Battlemind Utility 2"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "atwill");
        self.Update(
            {"emote":   "With a focused thought, you lift your body slightly off the ground on a current of psionic energy, allowing you to move over water or broken ground with ease.",
             "keywords":"Psionic",
             "effect":  "Until the end of this turn, you ignore difficult terrain and can both move across liquid and stand on it as if it were solid ground. In addition, you move 3 squares."
             });
    #end __init__
#end Feather_Step

#Level 6

class Winged_Weapon(Power_Normal):
    """Winged Weapon | Battlemind Utility 6"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "encounter");
        self.Update(
            {"emote":   "You channel psionic energy into your weapon, adjusting the rules of nature so that the weapon will slide through the air as if on wings when you hurl it.",
             "keywords":"Psionic",
             "effect":  "Choose a weapon you are holding. The next melee attack you make with that weapon before the end of your next turn becomes a ranged attack with a range of 10. The weapon returns to your hand after you make that attack."
             });
    #end __init__
#end Winged_Weapon

#Level 10


##PARAGON PATH
#--------------------

#Talaric Ironjack

class Iron_Hewed_Smash(Power_Normal):
    """Iron Hewed Smash | Talaric Ironjack Attack 11"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "encounter");
        self.Update(
            {"emote":   "You imbue your weapon with your own fury, striking hard to send your foes flying.",
             "keywords":    "Augmentable, Psionic, Weapon",
             "target":  "One creature",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("2"),
             "critical":self.Damage_Weapon_Mod_Crit("2"),
             "hiteffect":  "You push the target 5 squares.",
             "augmenttoggle":   RollQuery_Augment("2"),
             "augment2range":   "Close blast 3",
             "augment2target":  "Each enemy you can see in blast"
             });
    #end __init__
#end Iron_Hewed_Smash

class Enduring_Body(Power_Normal):
    """Enduring Body | Talaric Ironjack Utility 12"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "daily");
        self.Update(
            {"emote":   "As combat takes its toll on you, the power of the mind protects your body from additional harm.",
             "keywords":    "Healing, Psionic",
             "requirement": "You must be bloodied.",
             "effect":  "Until the end of the encounter, while you are bloodied you have regeneration 5 and resist 5 to all damage."
             });
    #end __init__
#end Enduring_Body

class Overwhelming_Force(Power_Normal):
    """Overwhelming Force | Talaric Ironjack Attack 20"""
    def __init__(self, power_num):
        """Initialize self.
        power_num : the power number used for Power attributes
        """
        Power_Normal.__init__(self, power_num, "daily");
        self.Update(
            {"emote":   "You channel the inherent violence of the world into a blow that freezes a foe in its tracks.",
             "keywords":    "Force, Psionic, Weapon",
             "attack":  self.Attack_Weapon(),
             "damage":  self.Damage_Weapon_Mod("4", "force"),
             "critical":self.Damage_Weapon_Mod_Crit("4", "force"),
             "hiteffect":  "The target is immobilized (save ends).",
             "eachfailedsave":  "The target takes 10 force damage.",
             "miss":    "Half damage."
             });
    #end __init__
#end Overwhelming_Force


##EPIC DESTINY
#--------------------
