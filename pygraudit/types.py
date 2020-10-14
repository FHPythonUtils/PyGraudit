"""
Types used by pygraudit

"""

from __future__ import annotations
import typing

class Finding(typing.TypedDict):
	"""Finding type

	{
		id: str
		title: str
		file: str
		evidence: list[Line]
		line: int
		col: int
	}
	"""
	id: str
	title: str
	file: str
	evidence: list[Line]
	line: int
	col: int




class Line(typing.TypedDict):
	"""Line type

	{
		line: int
		content: str
		selected: bool
	}
	"""
	line: int
	content: str
	selected: bool
