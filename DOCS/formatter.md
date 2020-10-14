Module pygraudit.formatter
==========================
Take our findings dictionary and give things a pretty format

finding dictionary

```json
{
        id: str
        title: str
        file: str
        evidence: list[Line]
        line: int
        col: int
}
```

Formats

- markdown
- json
- csv
- ansi

Functions
---------

    
`ansi(findings: list[Finding], heading: typing.Optional[str] = None, colourMode: int = 0) ‑> str`
:   Format to ansi
    
    Args:
            findings (list[Finding]): Findings to format
            heading (str, optional): Optional heading to include. Defaults to None.
    
    Returns:
            str: String to write to a file of stdout

    
`csv(findings: list[Finding], heading: typing.Optional[str] = None, colourMode: int = 0) ‑> str`
:   Format to CSV
    
    Args:
            findings (list[Finding]): Findings to format
            heading (str, optional): Optional heading to include. Defaults to None.
    
    Returns:
            str: String to write to a file of stdout

    
`formatEvidence(evidence: list[Line], newlineChar: bool = True) ‑> str`
:   Format evidence to plaintext
    
    Args:
            evidence (list[Line]): list of lines of code
            newlineChar (bool, optional): use newline char. Defaults to true
    
    Returns:
            str: string representation of this

    
`json(findings: list[Finding], heading: typing.Optional[str] = None, colourMode: int = 0) ‑> str`
:   Format to Json
    
    Args:
            findings (list[Finding]): Findings to format
            heading (str, optional): Optional heading to include. Defaults to None.
    
    Returns:
            str: String to write to a file of stdout

    
`markdown(findings: list[Finding], heading: typing.Optional[str] = None, colourMode: int = 0) ‑> str`
:   Format to Markdown
    
    Args:
            findings (list[Finding]): Findings to format
            heading (str, optional): Optional heading to include. Defaults to None.
    
    Returns:
            str: String to write to a file of stdout