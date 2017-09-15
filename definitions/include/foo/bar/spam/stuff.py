from definitions.headeritems import *

ITEMS = [

Function('iFail', 'BOM_create_window', '''\
Creates a new BOM window and returns the tag of the newly created window.''',
    [('tag_t*', 'window', 'O', '< (O) Tag of the newly created window'),
    ]),

Function('iFail', 'BOM_close_window', '''\
Close the BOM window.

@note Any changes to the structure of the bill in the window will be lost
      unless the #BOM_save_window function is called first.''',
    [('tag_t', 'window', 'I', '< (I) Tag of the window'),
    ]),

Function('iFail', 'BOM_refresh_window', '''\
Refresh the BOM window from the database.''',
    [('tag_t', 'window', 'I', '< (I) Tag of the window'),
    ]),

]