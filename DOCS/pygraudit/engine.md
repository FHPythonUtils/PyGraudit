# engine

> Auto-generated documentation for [pygraudit.engine](../../pygraudit/engine.py) module.

PyGraudit engine

- [Pygraudit](../README.md#pygraudit-index) / [Modules](../README.md#pygraudit-modules) / [pygraudit](index.md#pygraudit) / engine
    - [engine](#engine)
    - [extractEvidence](#extractevidence)
    - [filterFiles](#filterfiles)
    - [grep](#grep)
    - [listFiles](#listfiles)

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
```

## engine

[[find in source code]](../../pygraudit/engine.py#L105)

```python
def engine(
    startDirectory: str,
    db: str = 'python',
    allFiles: bool = False,
    ignorePaths: Union[(list[str], None)] = None,
) -> list[Finding]:
```

The engine entry point. Using a target startDirectory and a database, produce
a list of findings that we can throw into a formatter

#### Arguments

- `startDirectory` *str* - startDirectory path to start the search
- `db` *str, optional* - database to use. Defaults to "python".
- `allFiles` *bool, optional* - no filtering, scan everything
ignorePaths (Union[list[str], None]): list of files to filter

#### Returns

- `list[Finding]` - list of findings

## extractEvidence

[[find in source code]](../../pygraudit/engine.py#L41)

```python
def extractEvidence(desiredLine: int, file: str) -> list[Line]:
```

Grab evidence from the source file

#### Arguments

- `desiredLine` *int* - line to highlight
- `file` *str* - file to extract evidence from

#### Returns

- `list[Line]` - list of lines

## filterFiles

[[find in source code]](../../pygraudit/engine.py#L79)

```python
def filterFiles(
    startDirectory: str,
    files: list[str],
    ignorePaths: Union[(list[str], None)] = None,
) -> list[str]:
```

Remove files that are non text files and from hidden directories

#### Arguments

- `startDirectory` *str* - startDirectory path to start the search
- `files` *list[str]* - list of files to filter
ignorePaths (Union[list[str], None]): list of files to filter

#### Returns

- `list[str]` - new list of filtered files

## grep

[[find in source code]](../../pygraudit/engine.py#L142)

```python
def grep(pattern: str, filePath: str) -> Union[(re.Match, None)]:
```

Grep for a single regex in a single file...

#### Arguments

- `pattern` *str* - regex pattern to search
- `filePath` *str* - file to search in

#### Returns

- `Union[re.Match,` *None]* - Match or None

## listFiles

[[find in source code]](../../pygraudit/engine.py#L63)

```python
def listFiles(startDirectory: str) -> list[str]:
```

Get a list of files under a starting directory

#### Arguments

- `startDirectory` *str* - startDirectory path to start the search

#### Returns

- `list[str]` - list of files to filter
