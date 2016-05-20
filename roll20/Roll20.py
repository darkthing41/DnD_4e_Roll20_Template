def Attribute(name):
    """Returns a Roll20 attribute reference from the given name."""
    return "".join(("@{", name ,"}"));
#end Attribute

def _Property(name, value):
    """Returns a template property with the given property name and value."""
    return "".join(("{{", name, "=" ,value, "}}"));
#end Attribute


class Template:
    """Roll20 template
    Transforms a set of properties into a complete template string.
    names : container of property names in the order used by the template
    """

    def __init__(self, name_template, names_properties):
        """Initialize self.
        Attributes:
        name_template    : the template name
        names_properties : a container of property names in the order used by the template
        """
        self.__header = "".join(("&{template:", name_template, "}"));

        self._properties = {};
        self.names = names_properties;
    #end __init__


    def Update(self, *dicts):
        for d in dicts:
            self._properties.update(d);
    #end Update


    def Delete(self, *names_properties):
        for n in names_properties:
            del self._properties[n];
    #end Delete


    def __str__(self):
        """Return str(self).
        The textual representation of the template to be used in Roll20.
        """
        body = "";

        #Append named properties in order
        temp = self._properties.copy();
        for k in self.names:
            if k in temp:
                body += _Property(k, str(temp[k]));
                del temp[k];
            #end if
        #end for

        #Append any remaining properties
        for k in temp.keys():
            body += _Property(str(k), str(temp[k]));
        #end for

        return self.__header +body;
    #end __str__

#end Template
