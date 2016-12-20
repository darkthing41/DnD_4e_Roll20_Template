from roll20.Roll20 import Attribute
from roll20 import Template_dnd4epower
from roll20 import db_Powers_Core
from roll20 import db_Powers_Background
from roll20 import db_Powers_Battlemind
from roll20 import db_Powers_Skill

##POWERS
#--------------------

##01-10 Basic
#--------------------
#01
My_Melee_Basic_Attack = db_Powers_Core.Melee_Basic_Attack_Trained(1, "constitution");
My_Melee_Basic_Attack.Update({"emote": "Hammer time."});
#02
My_Ranged_Basic_Attack_Light = db_Powers_Core.Ranged_Basic_Attack(2);
My_Ranged_Basic_Attack_Light.Update({"emote": Attribute("character_name") +" resorts to the simple attack they learned when they first picked up a ranged weapon."});
#03
My_Ranged_Basic_Attack_Heavy = db_Powers_Core.Ranged_Basic_Attack(3);
My_Ranged_Basic_Attack_Heavy.Update({"emote": Attribute("character_name") +" resorts to the simple attack they learned when they first picked up a ranged weapon."});
#09
My_Second_Wind = db_Powers_Core.Second_Wind(9);
#10
My_Action_Point = db_Powers_Core.Action_Point(10);

##11-20 Background
#--------------------
#11
My_Disrupting_Advance = db_Powers_Background.Disrupting_Advance(11);

##21-30 Race
#--------------------
#21
My_Iron_Fist = db_Powers_Battlemind.Iron_Fist(21);
My_Iron_Fist.Update({"emote": Attribute("character_name") +" hardens his resolve."});
My_Iron_Fist.Delete("augmenttoggle", "augment1hiteffect","augment2damage","augment2critical");

##31-40
#--------------------
#31
My_Beckoning_Strike_Attack = db_Powers_Battlemind.Beckoning_Strike_Attack(31);
My_Beckoning_Strike_Attack.Update({"emote": "Going somewhere?"});

##41-50 Class - feature
#--------------------
#41
My_Battleminds_Demand = db_Powers_Battlemind.Battleminds_Demand(41);
#42
My_Blurred_Step = db_Powers_Battlemind.Blurred_Step(42);
My_Blurred_Step.Update({"Harrying Step:": "When you use your blurred step, you can teleport to any square adjacent to the triggering enemy instead of shifting."});
#43
My_Mind_Spike = db_Powers_Battlemind.Mind_Spike(43);
#44
My_Persistent_Harrier = db_Powers_Battlemind.Persistent_Harrier(44);

##51-60 Class - attack
#--------------------
#51
My_Bulls_Strength = db_Powers_Battlemind.Bulls_Strength(51);
My_Bulls_Strength.Update({"emote": Attribute("character_name") +" grins and swings with a casual grace."});
#52
My_Concussive_Spike = db_Powers_Battlemind.Concussive_Spike(52);
#53
My_Psionic_Speed = db_Powers_Battlemind.Psionic_Speed(53);
#57
My_Aspect_Of_Elevated_Harmony = db_Powers_Battlemind.Aspect_Of_Elevated_Harmony(57);
My_Aspect_Of_Elevated_Harmony.Update({"emote": "Your eyes glow as you achieve harmony of mind, body, and spirit."});
#58
My_Beckoning_Strike = db_Powers_Battlemind.Beckoning_Strike(58);
#59
My_Iron_Tomb = db_Powers_Battlemind.Iron_Tomb(59);

##61-70 Class - utility
#--------------------
#61
My_Feather_Step = db_Powers_Battlemind.Feather_Step(61);
My_Feather_Step.Update({"emote": "".join(("With a focused thought, ", Attribute("character_name"), " lifts slightly off the ground on a current of psionic energy."))});
#62
My_Physicians_Care = db_Powers_Skill.Physicians_Care(62);
#63
My_Enter_The_Crucible = db_Powers_Skill.Enter_The_Crucible(63);
My_Enter_The_Crucible.Update({"emote": Attribute("character_name") +" grins. Finally, a worthy challenge."});

##71-80 Paragon
#--------------------
#71
My_Iron_Hewed_Smash = db_Powers_Battlemind.Iron_Hewed_Smash(71);
#72
#My_Enduring_Body = db_Powers_Battlemind.Enduring_Body(72);
#73
#My_Overwhelming_Force = db_Powers_Battlemind.Overwhelming_Force(73);

##81-90 Epic
#--------------------

##91-100 Item
#--------------------
#91
My_Preservation_Shield = Template_dnd4epower.Power_Item(91, "daily");
My_Preservation_Shield.Update(
    {"effect": "".join(("You and each ally within 5 squares of you gain temporary hitpoints equal to the number of healing surges you have remaining ([[", Attribute("surges"), "]])."))
     });
#92
My_Pinning_Warhammer = Template_dnd4epower.Power_Item(92, "daily");
My_Pinning_Warhammer.Update(
    {"trigger": "You hit an enemy with this weapon.",
     "effect":  "That enemy is immobilized until you are no longer adjacent to it."
     });
#93
My_Summoned_Armor = Template_dnd4epower.Power_Item(93, "atwill");
My_Summoned_Armor.Update(
    {"effect":  "You banish this armor to a secure extradimensional location. At any point in the future, unless you are wearing armor, you can use another minor action to recall the armor. The armor appears on you as though you had donned it normally."
     });


##ABILITIES
#--------------------
My_Spyglass_Of_Perception = Template_dnd4epower.Skill("perception", "3[item]");
My_Spyglass_Of_Perception.Update(
    {"emote":   Attribute("character_name") +" looks through their Spyglass of Perception.",
     "special": "Using Spyglass of Perception."
     });



#--------------------


#Provide pseudo-shell
if __name__ == "__main__":
    import sys;
    print(My_Blurred_Step);
    while True:
        try:
            exp = eval(input(">>>\t"));
        except Exception as e:
            print(e);
        else:
            print(exp);
    #end while
#end __main__