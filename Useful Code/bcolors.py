#!/usr/bin/env python3
#Add to a resources folder and add the following imrpots
# from resources import bcolors

color_codes = { "HEADER" : "\033[95m",
			    "OKBLUE" : "\033[94m",
			    "OKGREEN" : "\033[92m",
			    "WARNING" : "\033[93m",
			    "ENDC" : "\033[0m",
			    "BOLD" : "\033[1m",
			    "UNDERLINE" : "\033[4m",
    			}

def header(text):
	return color_codes["HEADER"]+ text + color_codes["ENDC"]
def okblue(text):
	return color_codes["OKBLUE"]+ text + color_codes["ENDC"]
def okgreen(text):
	return color_codes["OKGREEN"]+ text + color_codes["ENDC"]
def warning(text):
	return color_codes["WARNING"]+ text + color_codes["ENDC"]
def fail(text):
	return color_codes["FAIL"]+ text + color_codes["ENDC"]
def bold(text):
	return color_codes["BOLD"]+ text + color_codes["ENDC"]
def underline(text):
	return color_codes["UNDERLINE"]+ text + color_codes["ENDC"]
