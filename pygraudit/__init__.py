"""Python version of graudit by Wireghoul https://github.com/wireghoul/graudit
"""
import os
import argparse
from sys import exit as sysexit, stdout
from pathlib import Path

stdout.reconfigure(encoding="utf-8")

import pygraudit.formatter as formatter
from pygraudit.engine import engine


THISDIR = str(Path(__file__).resolve().parent)
DB_FILES = [file.replace(".db", "") for file in os.listdir(THISDIR + "/signatures/")
if file.endswith(".db")]

FORMAT_HELP = "Output format. One of ansi, json, markdown, csv, sarif. default=ansi"
DB_HELP = f"db to use. One of {DB_FILES}. Default=python"

BANNER = """====================================================================
__________         ________                       .___.__  __
\\______   \\___.__./  _____/___________   __ __  __| _/|__|/  |_
 |     ___<   |  /   \\  __\\_  __ \\__  \\ |  |  \\/ __ | |  \\   __\\
 |    |    \\___  \\    \\_\\  \\  | \\// __ \\|  |  / /_/ | |  ||  |
 |____|    / ____|\\______  /__|  (____  /____/\\____ | |__||__|
           \\/            \\/           \\/           \\/
             grep rough audit - static analysis tool, in python
====================================================================
"""

def cli():
	""" cli entry point """
	parser = argparse.ArgumentParser(description=__doc__ ,
	formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("path_to_scan", help="Path to scan (.) for current directory", default=".")
	parser.add_argument("--format", "-f", help=FORMAT_HELP)
	parser.add_argument("--db", "-d", help=DB_HELP)
	parser.add_argument("-B", help="Suppress banner", action="store_true")
	parser.add_argument("-A", help="Scan ALL files", action="store_true")
	parser.add_argument("-z", help="Suppress colours", action="store_true")
	parser.add_argument("-Z", help="High contrast colours", action="store_true")
	parser.add_argument("-l", help="Lists databases available", action="store_true")
	parser.add_argument("--exclude", "-x", nargs="+", default=None, help="Paths to ignore")
	parser.add_argument("--file", "-o",
	help="Filename to write to (omit for stdout)")

	args = parser.parse_args()

	# File
	filename = stdout if args.file is None else open(args.file, "w", encoding="utf-8")
	# Colour Mode
	colourMode = 1
	if args.z:
		colourMode = 0
	if args.Z:
		colourMode = 2
	# Disable banner
	if not args.B:
		print(BANNER)
	# List database
	if args.l:
		_ = [print(db) for db in DB_FILES]
		sysexit(0)

	# Format
	formatMap = {
	"json": formatter.json, "markdown": formatter.markdown, "csv": formatter.csv,
	"ansi": formatter.ansi, "sarif": formatter.sarif}
	if args.format is None:
		formatt = formatter.ansi
	elif args.format in formatMap:
		formatt = formatMap[args.format]
	else:
		print(FORMAT_HELP)
		sysexit(1)

	findings = []
	if args.db is None or args.db in DB_FILES:
		if args.db is None:
			args.db = "python"
		findings = engine(args.path_to_scan, args.db, allFiles=args.A, ignorePaths=args.exclude)
		print(formatt(findings, colourMode=colourMode), file=filename)
	else:
		print(DB_HELP)
		sysexit(1)
