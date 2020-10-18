"""PyGraudit engine

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
"""
from __future__ import annotations
from typing import Union

import os
import os.path
import mimetypes
import re
from pathlib import Path

import regex

from pygraudit.types import Finding, Line

THISDIR = str(Path(__file__).resolve().parent)

IGNORE_PATHS = [
	re.compile(patt % {"sep": re.escape(os.path.sep)}) for patt in (
	r"(^|%(sep)s)\.[^\.]", # ignores any files or directories starting with '.'
	r"^tests?%(sep)s?",
	r"%(sep)stests?(%(sep)s|$)",
	# Ignore foo_test(s)/.
	r"_tests?(%(sep)s|$)",
)] # yapf: disable


def extractEvidence(desiredLine: int, file: str) -> list[Line]:
	"""Grab evidence from the source file

	Args:
		desiredLine (int): line to highlight
		file (str): file to extract evidence from

	Returns:
		list[Line]: list of lines
	"""
	with open(file, "r", encoding="utf-8", errors="ignore") as fileContents:
		start, stop = max(desiredLine - 3, 0), min(desiredLine + 2,
		sum(1 for i in open(file, 'rb')))
		for line in range(start):
			next(fileContents)
		content = []
		for line in range(start + 1, stop + 1):
			content.append({"selected": line==desiredLine,"line": line,
			"content": next(fileContents).rstrip().replace("\t", "    ")}) # yapf: disable
	return content


def listFiles(startDirectory: str) -> list[str]:
	"""Get a list of files under a starting directory

	Args:
		startDirectory (str): startDirectory path to start the search

	Returns:
		list[str]: list of files to filter
	"""
	filepaths = []
	for root, _, files in os.walk(startDirectory):
		for fileName in files:
			filepaths.append(os.path.join(root, fileName))
	return filepaths


def filterFiles(startDirectory: str, files: list[str],
ignorePaths: Union[list[str], None] = None) -> list[str]:
	"""Remove files that are non text files and from hidden directories

	Args:
		startDirectory (str): startDirectory path to start the search
		files (list[str]): list of files to filter
		ignorePaths (Union[list[str], None]): list of files to filter

	Returns:
		list[str]: new list of filtered files
	"""
	ignorePaths = ignorePaths or []
	ignoreRePaths = [re.compile(patt) for patt in ignorePaths]
	ignoreRePaths += IGNORE_PATHS
	outFiles = files.copy()
	for filepath in files:
		relpath = os.path.relpath(filepath, startDirectory)
		mimetype = mimetypes.guess_type(filepath)
		if any([ignore.search(relpath) for ignore in ignoreRePaths]):
			outFiles.remove(filepath)
		elif mimetype[0] is None or not str(mimetype[0]).startswith("text/"):
			outFiles.remove(filepath)
	return outFiles


def engine(startDirectory: str, db: str = "python", allFiles: bool = False,
ignorePaths: Union[list[str], None] = None) -> list[Finding]:
	"""The engine entry point. Using a target startDirectory and a database, produce
	a list of findings that we can throw into a formatter

	Args:
		startDirectory (str): startDirectory path to start the search
		db (str, optional): database to use. Defaults to "python".
		allFiles (bool, optional): no filtering, scan everything
		ignorePaths (Union[list[str], None]): list of files to filter

	Returns:
		list[Finding]: list of findings
	"""
	findings: list[Finding] = []
	grepFiles = listFiles(startDirectory)
	if not allFiles: # Filter the files
		grepFiles = filterFiles(startDirectory, grepFiles, ignorePaths)
	tests = open(THISDIR + "/signatures/" + db + ".db", "r",
	encoding="utf-8").read().splitlines(False)
	for file in grepFiles:
		for index, test in enumerate(tests):
			match = grep(test, file)
			if match is not None:
				content = open(file, "r", encoding="utf-8").read()[:match.start()]
				line = content.count("\n") + 1
				col = len(content.splitlines()[-1].replace("\t", "    ")) + 1
				findings.append({
				"id": f"PYG.{db}.{index:03}",
				"title": "Found match: " + str(match.group()).strip(),
				"file": file.replace(startDirectory, ".").replace("\\", "/"),
				"evidence": extractEvidence(line, file),
				"line": line,
				"col": col}) # yapf: disable
	return findings


def grep(pattern: str, filePath: str) -> Union[re.Match, None]:
	"""Grep for a single regex in a single file...

	Args:
		pattern (str): regex pattern to search
		filePath (str): file to search in

	Returns:
		Union[re.Match, None]: Match or None
	"""
	with open(filePath, "r", encoding="utf-8") as file:
		return regex.search(pattern, file.read())
