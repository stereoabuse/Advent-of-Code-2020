""" ranking.py -- Advent of Code 2020

    Author: Chris Bowman
    Last Modified: 12/10/2020
    License: MIT

    Prints rank information for all days of AoC 2020 to console
"""

import re
import requests
from bs4 import BeautifulSoup
import solutions.config as config


def daily_total():
    """
    Scrape the total correct submissions for each day from AoC website
    :return: dict with key of str(day) and value (int(total submissions)
    """
    url = 'https://adventofcode.com/2020/stats'
    r = requests.get(url).text
    soup = BeautifulSoup(r, features='html.parser')
    a = re.findall(r'(\d{1,2}) +(\d+) +\d+ +\*+', soup.text)
    day_totals = {}
    for item in a:
        try:
            the_day, total = int(item[0]), int(item[1])
            day_totals[the_day] = int(total)
        except ValueError as ve:
            print(ve)
            print(soup)
            exit()

    return day_totals


def personal_scores():
    """
    Scrape personal submission rankings for each day from AoC website
    :return: dict of day(str): tuple(part1 rank, part2 rank)
    """
    url = 'https://adventofcode.com/2020/leaderboard/self'
    r = requests.get(url, cookies=config.COOKIES).text
    soup = BeautifulSoup(r, features='html.parser')
    personal_stats = soup.find('pre').text
    my_scores = {int(d.split()[0]): (int(d.split()[2]), int(d.split()[5])) for d in personal_stats.splitlines()[2:]}
    return my_scores


def main():
    everyone = daily_total()
    try:
        mine = personal_scores()
        for day in sorted(mine):
            part_1, part_2 = mine[day]
            both_all = everyone[day]
            if day == '1':
                print("*Day 1 didn't count, don't get excited*")
            print(f'On day {day} you placed {part_1}th and {part_2}th of {both_all}')
            print(f'\tPart1: top {round(int(part_1) / int(both_all) * 100, 2)}%')
            print(f'\tPart2: top {round(int(part_2) / int(both_all) * 100, 2)}%')
            print()

    except NameError:
        print('Make sure a "config.py" file is in this directory.  It needs')
        print('to have a variable COOKIES = {"session": YOUR_SESSION_ID}\n')
        print('You can find this in Chrome Devtools:')
        print('\tReload a problem page (like https://adventofcode.com/2020/day/9)')
        print('\tNetwork -> PROBLEM_NUMBER -> Cookies -> Value')
        print('\tIt will be a salted b64 or hex')
        exit()


if __name__ == '__main__':
    main()
