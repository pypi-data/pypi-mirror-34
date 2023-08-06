=========
Publicize
=========
Set of utilities to help manage how modules are imported or exported

Works with both of the current major CPython versions, 2.7 and 3.7.

Detailed error messages make finding name conflicts easy.

Significantly reduce boilerplate, especially using ``star_export``, ``star_import``, ``public_constants``, and ``import_from_object``.

Simplifies dynamically reloading modules when source code has changed but restarting the interpreter is impossible or undesirable

============
Installation
============

``$ pip install publicize``

=========
Functions
=========

- ``import_as_copy(mod_or_name:[str, object]) -> module:``
    Import a shallow copy of `mod_or_name`

- ``import_from_object(obj, overwrite=False) -> dict``
    Pretends `obj` is a module and imports its public attributes

- ``public(*objects:[str, object], overwrite=False) -> objects[0]``
    Mark objects (or names) as public and automatically append them to ``__all__``.
    Can be used as a decorator with or without closing parentheses.

    There are 2 different ways to use it\:
        
        - ``@public(overwrite=False) <- (with or without parentheses)``
            Simple decorator for functions/classes. Adds the wrapped object's  
            ``__name__`` attribute to ``__all__``

        - ``public(name_or_object, *names_or_objects)``
            If an object is passed as an argument, all names that refer to that
            object will be added to ``__all__``. If a string is passed, the name 
            will be added assuming the reference actually exists.
            
-  ``public constants(**constants) -> constants:``
    Define public global variables, adding their names to ``__all__``.

-  ``public_from_import(module:[str, ModuleType], *names, overwrite=False) -> {**imported}:``
    ``from module import names`` and add the imported names to ``__all__``.

-  ``publish_module(module:[str, ModuleType], overwrite=False) -> module:``
    Publish everything that would be gotten with ``from module import *``

-  ``reimport_module(module:[str, ModuleType]) -> module:``
    Clear a module's dict and reimport it.

-  ``reverse_star_import(module) -> None:``
    Removes what would be imported with ``from module import *``
   
-  ``safe_star_import(module) -> {**imported}:``
    ``from module import *`` that will not overwrite existing names

-  ``star_export(*private_modules, ignore_list=None, export_private=True, export_metadata=False, caller=None):``
    Force `exporter` (caller by default) to export almost everything
    
-  ``star_import(module:[str, ModuleType], overwrite=False, module=False, prefix=None, id_mod=None, ignore_private=False, import_metadata=False) -> [dict, {**imported}]:``
    Ignore default ``* import`` mechanics to import almost everything.

    If ``prefix`` is True, it will be prepended to imported names.
    
    If ``overwrite`` is False, an error is raised instead of overwriting.

    If ``ignore_private`` is True then _private names prepended with an
    underscore are ignored.

    If ``import_metadata`` is True, then module metadata attributes such as
    ``__author__`` and ``__version__`` are imported.

    If ``module`` is True, return the module itself, otherwise a dict
    mapping of imported:object names.
    
    Special attributes of modules such as ``__path__``, ``__file__``, and
    ``__all__`` are never imported.


=============
Example usage
=============
::

    # in colors.py
    from publicize import *
    public_from_import('enum', 'Enum')
    @public
    class Colors(Enum):
        RED = red = 'red'
        BLUE = blue = 'blue'
        GREEN = green = 'green'
    COLOR_LIST = [*Colors]
    COLOR_DICT=public_constants(**Colors.__members__)
    CHARTREUSE = GREEN
    CYAN = BLUE
    CARMINE = RED
    public(CHARTREUSE, CYAN, CARMINE)
    random = star_import('random', prefix='random_', module=True)

    def random_color():
        return random_choice(COLOR_LIST)
    
    def _get_valid_colors():
        return {k for k, v in globals().items() if isinstance(v, Colors)}

``>>> from publicize import *``

``>>> import colors``

``>>> colors_namespace = star_import('colors')``

``>>> colors.__all__``

``['BLUE', 'CARMINE', 'CHARTREUSE', 'CYAN', 'Colors', 'Enum', 'GREEN', 'RED', 'blue', 'green', 'red']``

``>>> CHARTREUSE``

``<Colors.GREEN: 'green'>``

``>>> COLOR_DICT['blue']``

``<Colors.BLUE: 'blue>``

``>>> old = CARMINE``

``>>> reverse_star_import('colors')``

``>>> reimport_module('colors').CARMINE is not old``

``True``

``>>> random_color()``

``<Colors.BLUE: 'blue'>``

``>>> _get_colors()``

``>>> {'BLUE', 'CHARTREUSE', 'GREEN', 'CARMINE', 'red', 'CYAN', 'green', 'blue', 'RED'}``
