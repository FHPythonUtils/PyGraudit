# types

> Auto-generated documentation for [pygraudit.types](../../pygraudit/types.py) module.

Types used by pygraudit

- [Pygraudit](../README.md#pygraudit-index) / [Modules](../README.md#pygraudit-modules) / [pygraudit](index.md#pygraudit) / types
    - [Finding](#finding)
    - [Line](#line)

## Finding

[[find in source code]](../../pygraudit/types.py#L9)

```python
class Finding(typing.TypedDict):
```

Finding type

{
 id: str
 title: str
 file: str
 evidence: list[Line]
 line: int
 col: int
}

## Line

[[find in source code]](../../pygraudit/types.py#L31)

```python
class Line(typing.TypedDict):
```

Line type

{
 line: int
 content: str
 selected: bool
}
