import re
import pkgutil
import definitions

def get_everything():
    for importer, inc_modname, ispkg in pkgutil.walk_packages(definitions.__path__, prefix=definitions.__name__ + '.'):
        # the module name without the `includes.` prefix
        modname = re.match(r'definitions.(?P<NAME>.*)', inc_modname).group('NAME')

        # no data should be in any __init__.py
        if ispkg:
            continue

        # headeritems is the only file which doesn't correspond to a .h file
        if modname == 'headeritems':
            continue

        # import the module and grab ITEMS
        mod = importer.find_module(inc_modname).load_module(inc_modname)

        yield modname, mod.ITEMS
