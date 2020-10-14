"""
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
"""
# pyright: reportConstantRedefinition=false
from __future__ import annotations

from io import StringIO
from json import dumps
from csv import writer
import typing
from pygraudit.types import Finding, Line


def formatEvidence(evidence: list[Line], newlineChar: bool =True) -> str:
	"""Format evidence to plaintext

	Args:
		evidence (list[Line]): list of lines of code
		newlineChar (bool, optional): use newline char. Defaults to true

	Returns:
		str: string representation of this
	"""
	evidenceText = [line["content"] for line in evidence]
	if newlineChar:
		return "\n".join(evidenceText)
	return "\\n".join(evidenceText)



def markdown(findings: list[Finding],
heading: typing.Optional[str] = None, colourMode: int=0) -> str:
	"""Format to Markdown

	Args:
		findings (list[Finding]): Findings to format
		heading (str, optional): Optional heading to include. Defaults to None.

	Returns:
		str: String to write to a file of stdout
	"""
	if len(findings) == 0:
		return "No findings"

	heading = heading if heading is not None else \
	"# Findings\nList of findings"
	strBuf = [heading]

	# Details
	for finding in findings:
		strBuf.extend([
		f"## {finding['title']}",
		f"\n\nFile: `{finding['file']}`",
		f"\n\nLine: {finding['line']}\n\n```python\n{formatEvidence(finding['evidence'])}\n```",
		])
	return "\n".join(strBuf) + "\n"


def json(findings: list[Finding],
heading: typing.Optional[str] = None, colourMode: int=0) -> str:
	"""Format to Json

	Args:
		findings (list[Finding]): Findings to format
		heading (str, optional): Optional heading to include. Defaults to None.

	Returns:
		str: String to write to a file of stdout
	"""
	out = {"heading": heading if heading is not None else \
	"Findings - Findings below",
	"findings": findings}
	return dumps(out, indent="\t")


def csv(findings: list[Finding],
heading: typing.Optional[str] = None, colourMode: int=0) -> str:
	"""Format to CSV

	Args:
		findings (list[Finding]): Findings to format
		heading (str, optional): Optional heading to include. Defaults to None.

	Returns:
		str: String to write to a file of stdout
	"""
	output = StringIO()
	csvString = writer(output)
	csvString.writerow([heading if heading is not None else \
	"Findings - Findings below (you may want to delete this line)"])
	csvString.writerow([
	"id", "title", "file", "evidence", "line", "col"])
	for finding in findings:
		csvString.writerow([
		finding["id"], finding["title"], finding["file"],
		formatEvidence(finding["evidence"], False),
		finding["line"], finding["col"]])
	return output.getvalue()


def ansi(findings: list[Finding],
heading: typing.Optional[str] = None, colourMode: int=0) -> str:
	"""Format to ansi

	Args:
		findings (list[Finding]): Findings to format
		heading (str, optional): Optional heading to include. Defaults to None.

	Returns:
		str: String to write to a file of stdout
	"""
	# pylint: disable=invalid-name
	TXT = ""
	BLD = ""
	CLS = ""
	UL = ""
	CB = ""
	CG = ""
	CODE = f"{TXT}│"
	if colourMode == 1:
		TXT = ""
		BLD = "\033[01m"
		CLS = "\033[00m"
		UL = "\033[04m"
		CB = "\033[36m"
		CG = "\033[32m"
		CODE = f"{TXT}│\033[100m\033[93m"
	elif colourMode == 2:
		TXT = "\033[97m"
		BLD = "\033[01m"
		CLS = "\033[00m"
		UL = "\033[04m"
		CB = "\033[96m"
		CG = "\033[92m"
		CODE = f"{TXT}│\033[107m\033[90m"

	if len(findings) == 0:
		return f"{BLD}{UL}{CB}No findings{CLS}"

	# pylint: enable=invalid-name
	heading = heading if heading is not None else \
	f"{BLD}{UL}{CB}Findings{CLS}\n\n{TXT}List of findings\n"
	strBuf = [heading]


	# Details
	for finding in findings:
		evidence = [f"{TXT}┌{' ' + finding['file'] + ' ':─^85}┐"]
		for line in finding['evidence']:
			evidence.append((CODE if line["selected"] else f"{TXT}│") +f"{str(line['line'])[:3]: >3}  {line['content'][:80]: <80}{CLS}{TXT}│")
		evidence.append(f"└{'─'*85}┘")
		evidenceStr = '\n'.join(evidence)
		strBuf.extend([
		f"{BLD}{UL}{CG}{finding['title']}{CLS}",
		f"{evidenceStr}\n",
		])
	return "\n".join(strBuf) + f"{CLS}"
