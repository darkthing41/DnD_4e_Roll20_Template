from . import Roll20

def RollQuery_Augment(*values):
    """Utility function for constructing roll queries for Augmentation level.
    *values : non-zero augmentation levels accepted."""
    prefix = "?{Augment|Unaugmented,0";
    body = "";
    suffix = "}";
    for v in values:
        v = str(v);
        assert v in ("1","2","4","6");
        body = "".join((body, "|", "Augment ", v, ",", v));
    return "".join(("[[", prefix, body, suffix, "]]"));
#end RollQuery_Augment


class Template(Roll20.Template):
    """Roll20 template: dnd4epower
    """
    __name = "dnd4epower";
    __properties = (
        "atwill","encounter","daily","item","other","ability","skill",
        "emote",
        "name","class","level","type","keywords","attacktechnique","action","range",
        "requirement","trigger",
        "beforespecial","beforeeffect",
        "target","primarytarget",
        "attackweaponmod","attack",
        "multiattacktoggle",
        "multiattack2","multiattack3","multiattack4","multiattack5","multiattack6","multiattack7","multiattack8","multiattack9","multiattack10","multiattack11","multiattack12","multiattack13","multiattack14","multiattack15","multiattack16","multiattack17","multiattack18","multiattack19","multiattack20",
        "damage","critical",
        "hitweaponmod","hiteffect","hitaftereffect","effectweaponmod",
        "secondaryrange","secondarytarget","secondaryattack","secondarydamage","secondarycritical","secondaryhiteffect",
        "tertiaryrange","tertiarytarget","tertiaryattack","tertiarydamage","tertiarycritical","tertiaryhiteffect",
        "augmenttoggle",
        "augment1range","augment1target","augment1attack","augment1multitoggle","augment1multiattack2","augment1multiattack3","augment1multiattack4","augment1multiattack5","augment1multiattack6","augment1multiattack7","augment1multiattack8","augment1multiattack9","augment1damage","augment1critical","augment1hiteffect",
        "augment2range","augment2target","augment2attack","augment2multitoggle","augment2multiattack2","augment2multiattack3","augment2multiattack4","augment2multiattack5","augment2multiattack6","augment2multiattack7","augment2multiattack8","augment2multiattack9","augment2damage","augment2critical","augment2hiteffect",
        "augment4range","augment4target","augment4attack","augment4multitoggle","augment4multiattack2","augment4multiattack3","augment4multiattack4","augment4multiattack5","augment4multiattack6","augment4multiattack7","augment4multiattack8","augment4multiattack9","augment4damage","augment4critical","augment4hiteffect",
        "augment6range","augment6target","augment6attack","augment6multitoggle","augment6multiattack2","augment6multiattack3","augment6multiattack4","augment6multiattack5","augment6multiattack6","augment6multiattack7","augment6multiattack8","augment6multiattack9","augment6damage","augment6critical","augment6hiteffect",
        "classmodifier",
        "miss",
        "effect",
        "firstfailedsave","secondfailedsave","eachfailedsave","aftereffect",
        "sustainminor","sustainstandard",
        "movetechnique","mttype","mtrange","mttarget","mteffect",
        "special"
    );

    def __init__(self):
        """Initialize self."""
        Roll20.Template.__init__(self, self.__name, self.__properties);
    #end __init__

#end Template_dnd4ePower


class Power(Template):
    """Roll20 template: dnd4epower
    Represents and automatically fills in common Power properties.
    -header
    -name
    -level
    -range
    -action
    """
    __types = ("atwill", "encounter", "daily", "item");
    _usages = {"atwill":"At-Will", "encounter":"Encounter", "daily":"Daily"};

    def Attribute_Power(self, name):
        """Utility function for constructing Roll20 Attributes that depend on the power number."""
        return Roll20.Attribute(self._power +"-" +name);
    #end Attribute_Power

    def Attack_Skill(self, bonus=0):
        """Utility function for constructing weaponless attack rolls."""
        bonus = str(bonus);
        if (bonus == "0"):
            return "".join(("[[1d20+", Attribute("halflevel"), "[level/2]+", self.Attribute_Power("mod"), "+", self.Attribute_Power("attack-misc"), "]] vs ", self.Attribute_Power("def")));
        else:
            return "".join(("[[1d20+", Attribute("halflevel"), "[level/2]+", self.Attribute_Power("mod"), "+", self.Attribute_Power("attack-misc"), "+", bonus, "]] vs ", self.Attribute_Power("def")));
    #end Attack_Skill

    def Attack_Weapon(self, bonus=0):
        """Utility function for constructing weapon attack rolls."""
        bonus = str(bonus);
        if (bonus == "0"):
            return "".join(("[[1d20+", self.Attribute_Power("attack"), "]] vs ", self.Attribute_Power("def")));
        else:
            return "".join(("[[1d20+", self.Attribute_Power("attack"), "+", bonus, "]] vs ", self.Attribute_Power("def")));
    #end Attack_Weapon

    def W(self, multiplier=1):
        """Utility function for constructing N[W] weapon damage expressions."""
        multiplier = str(multiplier);
        weapon_dice_count = self.Attribute_Power("weapon-num-dice");
        weapon_dice = self.Attribute_Power("weapon-dice");
        return "".join(("(", multiplier, "*", weapon_dice_count, ")d", weapon_dice));
    #end W

    def W_Crit(self, multiplier=1):
        """Utility function for constructing N[W] weapon critical damage expressions."""
        multiplier = str(multiplier);
        weapon_dice_count = self.Attribute_Power("weapon-num-dice");
        weapon_dice = self.Attribute_Power("weapon-dice");
        return "".join(("(", multiplier, "*", weapon_dice_count, ")*", weapon_dice));
    #end W_Crit

    def Damage_Weapon_Mod(self, w_multiplier, damage_type=""):
        """Utility function for constructing N[W] + Ability modifier damage rolls"""
        damage_type = str(damage_type);
        if damage_type == "":
            return "".join(("[[", self.W(w_multiplier), "+", self.Attribute_Power("damage"), "]] damage."));
        else:
            return "".join(("[[", self.W(w_multiplier), "+", self.Attribute_Power("damage"), "]] ", damage_type, " damage."));
    #end Damage_Weapon_Mod

    def Damage_Weapon_Mod_Crit(self, w_multiplier, damage_type=""):
        """Utility function for constructing N[W] + Ability modifier critical damage rolls"""
        damage_type = str(damage_type);
        if damage_type == "":
            return "".join(("[[", self.W_Crit(w_multiplier), "+", self.Attribute_Power("damage"), "]] damage."));
        else:
            return "".join(("[[", self.W_Crit(w_multiplier), "+", self.Attribute_Power("damage"), "]] ", damage_type, " damage."));
    #end Damage_Weapon_Mod_Crit

    def __init__(self, power_num, type_):
        """Initialize self.
        power_num : the power number used for Power attributes
        type_     : the power type, in ("atwill", "encounter", "daily", "item")
        """
        Template.__init__(self);
        assert type_ in Power.__types;

        #calculate property prefix
        self._power = "power-" +str(power_num);

        #set header type
        self._properties[type_] = "1";

        #set reference properties
        for k in ("name", "level", "range"):
            self._properties[k] = self.Attribute_Power(k);
        for k in ("action",):
            self._properties[k] = self.Attribute_Power(k) +" \u2666 ";
    #end __init__

#end Power


class Power_Normal(Power):
    """Roll20 template: dnd4epower
    Represents and automatically fills in normal Attack and Utility power properties.
    -type (usage)
    """

    def __init__(self, power_num, usage):
        """Initialize self.
        power_num : the power number used for Power attributes
        usage     : the power's usage, in ("atwill", "encounter", "daily")
        """
        Power.__init__(self, power_num, usage);
        assert usage in Power._usages;

        #set matching 'usage'
        self._properties["type"] = Power._usages[usage] +" \u2666 ";
    #end __init__

#end Power_Attack


class Power_Item(Power):
    """Roll20 template: dnd4epower
    Represents and automatically fills in Item power properties.
    -type (usage)
    """

    def __init__(self, power_num, usage):
        """Initialize self.
        power_num : the power number used for Power attributes
        usage     : the item power's usage, in ("atwill", "encounter", "daily")
        """
        Power.__init__(self, power_num, "item");
        assert usage in Power._usages;

        #set matching 'usage'
        self._properties["type"] = Power._usages[usage] +" \u2666";
    #end __init__

#end


class Ability(Template):
    """Roll20 template: dnd4epower
    Represents and automatically fills in Ability properties.
    -emote
    -name
    -class
    -type
    -ability
    """
    __types = ("strength", "constitution", "dexterity", "intelligence", "wisdom", "charisma");

    def __init__(self, type_, bonus=0):
        """Initialize self.
        type_ : the ability type
        bonus : the bonus to add to the ability check
        """
        Template.__init__(self);
        assert type_ in Ability.__types;
        bonus = str(bonus);

        self._properties["emote"] = Roll20.Attribute("".join(("ability-", type_, "-roll-text")));
        self._properties["name"] = type_.title() +" Ability Check";
        self._properties["class"] = Roll20.Attribute("character_name");
        self._properties["type"] = "Using " +type_.title();
        if (bonus == "0"):
            self._properties["ability"] = "".join(("[[1d20+", Roll20.Attribute(type_ +"-mod-level"), "]]"));
        else:
            self._properties["ability"] = "".join(("[[1d20+", Roll20.Attribute(type_ +"-mod-level"), "+", bonus, "]]"));
    #end __init__

#end Ability


class Skill(Template):
    """Roll20 template: dnd4epower
    Represents and automatically fills in Skill properties.
    -emote
    -name
    -class
    -type
    -skill
    """
    #__types = {"Acrobatics":"dexterity", "Arcana":"intelligence", "Athletics":"strength", "Bluff":"charisma", "Diplomacy":"charisma", "Dungeoneering":"wisdom", "Endurance":"constitution", "Heal":"wisdom", "History":"intelligence", "Insight":"wisdom", "Intimidate":"charisma", "Nature":"wisdom", "Perception":"wisdom", "Religion":"intelligence", "Stealth":"dexterity", "Streetwise":"charisma", "Thievery":"dexterity"};
    __types = ("acrobatics", "arcana", "athletics", "bluff", "diplomacy", "dungeoneering", "endurance", "heal", "history", "insight", "intimidate", "nature", "perception", "religion", "stealth", "streetwise", "thievery");

    def __init__(self, type_, bonus=0):
        """Initialize self.
        type_ : the skill type
        bonus : the bonus to add to the skill check
        """
        Template.__init__(self);
        assert type_ in Skill.__types;
        bonus = str(bonus);

        self._properties["emote"] = Roll20.Attribute("".join(("skill-", type_, "-roll-text")));
        self._properties["name"] = type_.title();
        self._properties["class"] = Roll20.Attribute("character_name");
        self._properties["type"] = "Skill Check";
        if (bonus == "0"):
            self._properties["skill"] = "".join(("[[1d20+", Roll20.Attribute(type_), "]]"));
        else:
            self._properties["skill"] = "".join(("[[1d20+", Roll20.Attribute(type_), "+", bonus, "]]"));
    #end __init__

#end Skill
