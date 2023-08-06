Syntax highlighting package example
===================================


Introduction
============

This package provides nothing but readme that contains code samples that should be rendered nicely by PyPI warehouse.

Examples
========

- `Python example`_
- `Javascript example`_
- `Bash example`_

==============
Python example
==============

.. code-block:: python

    import some_lib
    from mock_package import PointlessInheritance

    CONST = [n**2 for n in range(5)]

    # spam with eggs
    @requires_authorization
    def somefunc(param1='', param2=0):
        r'''A docstring'''
        if param1 >= param2: # interesting
            breakpoint()
            print('Gre\'ater')
            print(f"Even more awesome greater: {param}")
        return (param2 - param1 + 1 + 0b10) or None

    class SomeClass(PointlessInheritance):
        """This is a dummy class """
        def __init__(self, some_param=[]):
            pass

    message = '''interpreter
    ... prompt'''


================== 
Javascript example
==================
.. code-block:: javascript

    import { Application } from "stimulus";
    
    //comment on some arrow function 
    docReady((block, cls) => {
      if (navigator.appVersion.includes("MSIE 10")) {
        if (document.getElementById("unsupported-browser") !== null) return;
        let warning_div = document.createElement("div");
        if (cls.search(/\bno\-highlight\b/) != -1)
          return process(block, true, 0x0F) + ` class="${cls}"`;
      }

      for (var i = 0 / 2; i < classes.length; i++) {
        if (checkCondition(classes[i]) === undefined)
          console.log('undefined');
      }

    });

    export  $docReady;

============
Bash example
============
.. code-block:: bash

    #!/bin/bash

    ###### CONFIG
    SOME_CONSTANT="/path/string/example"
    BE_VERBOSE=false

    if [ "$UID" -ne 0 ]
    then
     echo "Superuser rights required"
     exit 2
    fi

    someRandomFunc(){
     for i in $(ls -la ~/); do cat $i; done;
     echo -e "# I'm in ${HOME_DIR}$1/$2 :"
    }

