Note: Some editors could check the PEP8 fro you automatically, such as VS Code python lint extension, PyCharm etc. 

[PEP 8](https://www.python.org/dev/peps/pep-0008/) (Python Enhancement Proposal) is a guide which contains a set of rules to format your Python code to maximize its readability. Consistency is the key.


- Indentation: Use 4 spaces per indentation level.
- Spaces are the preferred indentation method.
- Limit all lines to a maximum of 79 characters.
- Surround top-level function and class definitions with two blank lines.
- Method definitions inside a class are surrounded by a single blank line.
- Code in the core Python distribution should always use UTF-8 (or ASCII in Python 2).
- Imports should usually be on separate lines:
- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
- Imports should be grouped in the following order:
    - Standard library imports.
    - Related third party imports.
    - Local application/library specific imports.
    
    Note: You should put a blank line between each group of imports.
- Absolute imports are recommended
- Wildcard imports (from <module> import *) should be avoided
- Module level "dunders" (i.e. names with two leading and two trailing underscores) such as __all__, __author__, __version__, etc. should be placed after the module docstring but before any import statements except from __future__ imports
- Don't use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter.
- Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).
- Paragraphs inside a block comment are separated by a line containing a single #
- Documentation Strings
    - Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.
    - the """ that ends a multiline docstring should be on a line by itself
    - For one liner docstrings, please keep the closing """ omn the same line. 
- Naming Conventions
    - Method Names and Instance Variables: 
        - Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.
        - Use one leading underscore only for non-public methods and instance variables.
    - Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
    - Class names should normally use the CapWords convention.
    - Function names should be lowercase, with words separated by underscores as necessary to improve readability.
    - Variable names follow the same convention as function names.
    - mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.
    - Use one leading underscore only for non-public methods and instance variables.
    - Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.
    - Public attributes should have no leading underscores.
- Comparisons to singletons like None should always be done with is or is not, never the equality operators.
- Use is not operator rather than not
- Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier.
- Derive exceptions from Exception rather than BaseException.
- Use exception chaining appropriately. In Python 3, "raise X from Y" should be used to indicate explicit replacement without losing the original traceback.
- When catching exceptions, mention specific exceptions whenever possible instead of using a bare except: clause:
- For all try/except clauses, limit the try clause to the absolute minimum amount of code necessary.
- Be consistent in return statements. Either all return statements in a function should return an expression, or none of them should.
- Use string methods instead of the string module.
- String methods are always much faster and share the same API with unicode strings.
- Use ''.startswith() and ''.endswith() instead of string slicing to check for prefixes or suffixes.
- Object type comparisons should always use isinstance() instead of comparing types directly.
- For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
- Don't write string literals that rely on significant trailing whitespace.
- Don't compare boolean values to True or False using ==.
- Use of the flow control statements return/break/continue within the finally suite of a try...finally, where the flow control statement would jump outside the finally suite, is discouraged.
- [Function Annotations](https://www.python.org/dev/peps/pep-0484/)
- [Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
    - Annotations for module level variables, class and instance variables, and local variables should have a single space after the colon.
    - There should be no space before the colon.
    - If an assignment has a right hand side, then the equality sign should have exactly one space on both sides.