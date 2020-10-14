Module pygraudit.engine
=======================
PyGraudit engine

Functions return finding dictionary

```json
{
        id: str
        title: str
        file: str
        evidence: list[Line]
        line: int
        col: int
}

Functions
---------

    
`engine(startDirectory: str, db: str = 'python', allFiles: bool = False, ignorePaths: Union[list[str], None] = None) ‑> list`
:   The engine entry point. Using a target startDirectory and a database, produce
    a list of findings that we can throw into a formatter
    
    Args:
            startDirectory (str): startDirectory path to start the search
            db (str, optional): database to use. Defaults to "python".
            allFiles (bool, optional): no filtering, scan everything
            ignorePaths (Union[list[str], None]): list of files to filter
    
    Returns:
            list[Finding]: list of findings

    
`extractEvidence(desiredLine: int, file: str) ‑> list`
:   Grab evidence from the source file
    
    Args:
            desiredLine (int): line to highlight
            file (str): file to extract evidence from
    
    Returns:
            list[Line]: list of lines

    
`filterFiles(startDirectory: str, files: list[str], ignorePaths: Union[list[str], None] = None) ‑> list`
:   Remove files that are non text files and from hidden directories
    
    Args:
            startDirectory (str): startDirectory path to start the search
            files (list[str]): list of files to filter
            ignorePaths (Union[list[str], None]): list of files to filter
    
    Returns:
            list[str]: new list of filtered files

    
`grep(pattern: str, filePath: str) ‑> Optional[re.Match]`
:   Grep for a single regex in a single file...
    
    Args:
            pattern (str): regex pattern to search
            filePath (str): file to search in
    
    Returns:
            Union[re.Match, None]: Match or None

    
`listFiles(startDirectory: str) ‑> list`
:   Get a list of files under a starting directory
    
    Args:
            startDirectory (str): startDirectory path to start the search
    
    Returns:
            list[str]: list of files to filter