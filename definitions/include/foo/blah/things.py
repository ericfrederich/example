from definitions.headeritems import *

ITEMS = [
Function('iFail', 'AOM_ask_value_strings', '''\
Asks one or more values of a property. The property can be single-valued or multi-valued (i.e., array or list).

This function uses #PROP_ask_value_strings_msg if multi-valued and #PROP_ask_value_string_msg if single-valued.
To customize the behavior of this function, register a method against one of these messages.''',
    [('tag_t'      , 'object_tag', 'I'       , '< (I) Unique identifier (tag) of the object instance.'),
     ('const char*', 'prop_name' , 'I'       , '< (I) A property name of the object instance.'),
     ('int*'       , 'num'       , 'OC'      , '< (O) Number of values asked.'),
     ('char***'    , 'values'    , 'OL(num)F', '< (OF) num Actual values of the property. This must be a list or array \n'
                                               '       of constant chars. If the property is an array, the number of \n'
                                               '       values passed in must equal the size of the array.\n'
                                               '       Iterate through the output array and call MEM_free on each element to de-allocate\n'
                                               '       the nested memory block and then free the memory pointed by itself using MEM_free.'),
    ]),
]
