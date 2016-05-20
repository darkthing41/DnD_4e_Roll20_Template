# DnD_4e_Roll20_Template
D&amp;D 4th Edition: Roll20 dnd4epower template generator

##Description
A set of Python (v. 3.5.1 at last update) scripts for generating Roll20 template strings.
Specifically, this supports the [`dnd4epower`][link-template] template, as used by the [4th Edition Character Sheet][link-sheet].

[link-sheet]:https://wiki.roll20.net/DnD4e_Character_Sheet
[link-template]:https://wiki.roll20.net/DnD4e_Character_Sheet#Roll_Template

##Modules

###`roll20` Package
This package encapsulates the template logic and power databases.

| Name          | Purpose       |
| ------------- | ------------- |
| `Roll20.py`   | Encapsulate the Roll20 interface (attributes, templates)
| `Template_dnd4epower.py` | The `dnd4epower` template; subtypes; specific utilities
| `db_Powers_*.py` | Database containing (mostly) completed templates.

(At present the databases cover only a tiny fraction of those in the source books; if anybody wishes to extend or add to these, please do!)

###Character Modules
Any further `.py` scripts outside of the `roll20` package are character scripts.
These contain instances of the templates pulled from the databases, specifically constructed, or maybe tweaked for that character.

The final template strings may be copied by running these scripts, and printing the defined variables.
(A basic interface is provided to allow the script to be run directly by `python.exe`; simply enter the variable name, e.g. `My_Melee_Basic_Attack`)

##Module Documentation

###`roll20.Roll20`
Encapsulates the aspects defined by Roll20 itself.
+ accessing attributes
+ generic templates
  - constructing, updating dictionaries
  - constructing final template string

###`roll20.Template_dnd4epower`
Encapsulates the specific `dnd4epower` template, and its subtypes (e.g. Powers, Skill Checks).
These templates are designed to match the style of rolls built in to the sheet.

Additionally, defines some utility functions for constructing rolls or expressions common to many powers (e.g. N[W] weapon damage rolls).

###`roll20` Databases
The `Template_dnd4epower` template subtypes are partially implemented in the database files, ready to be used in Character scripts.

| Name                  | Contents      |
| --------------------- | ------------- |
| `db_Powers_Background` | [incomplete] Powers sourced from character background or themes.
| `db_Powers_Battlemind` | [incomplete] Powers for the Battlemind class, Paragon paths, and Epic Destinies.
| `db_Powers_Core`      | [incomplete] Powers common to all characters.
| `db_Powers_Skill    ` | [incomplete] Skill Powers.
