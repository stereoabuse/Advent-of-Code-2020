""" utils.py -- Advent of Code 2020 Utility functions

    Author: Chris Bowman
    Last Modified: 12/5/2020
    License: MIT
"""

import re
import requests
from bs4 import BeautifulSoup
import config  # AoC website login


# Web interaction
def web_input(day, year=2020):
    """Snags input data from AoC website, returns string."""
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    return requests.get(url, cookies=config.COOKIES).text


def local_input(day):
    """Takes input data from local file, returns string or FileNotFoundError."""
    file = f'../input/{str(day).zfill(2)}'
    try:
        return open(file, 'r').read()
    except FileNotFoundError as error:
        return error


def gen_local_input(day, year=2020):
    """Creates local file of the day's input data."""
    with open(f'../inputs/{str(day).zfill(2)}', 'w') as file:
        file.write(web_input(day, year))


def submit(answer, day, part, year=2020):
    """Submits my answer to the AoC website and returns if accepted or not."""
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    form = {'level': str(part), 'answer': str(answer)}
    r = requests.post(url, cookies=config.COOKIES, data=form)
    soup = BeautifulSoup(r.text, features='html.parser')
    reply = soup.find('p').text
    return reply


# Parsing
def integers(s):
    """Takes a string and return digits split by any other character into generator."""
    return [int(i) for i in re.split(r'\D+', s) if i]


def alphanums(s):
    """Splits a string by any non letter or digit and returns a list"""
    return [i for i in re.split(r'\W+', s, re.MULTILINE) if i]
