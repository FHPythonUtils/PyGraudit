Module pygraudit.types
======================
Types used by pygraudit

Classes
-------

`Finding(*args, **kwargs)`
:   Finding type
    
    {
            id: str
            title: str
            file: str
            evidence: list[Line]
            line: int
            col: int
    }

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `col: int`
    :

    `evidence: list`
    :

    `file: str`
    :

    `id: str`
    :

    `line: int`
    :

    `title: str`
    :

`Line(*args, **kwargs)`
:   Line type
    
    {
            line: int
            content: str
            selected: bool
    }

    ### Ancestors (in MRO)

    * builtins.dict

    ### Class variables

    `content: str`
    :

    `line: int`
    :

    `selected: bool`
    :