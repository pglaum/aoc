#!/usr/bin/env python3
from datetime import datetime
import os
import re

import click
import httpx
from git import Repo

@click.group()
def cli():
    pass

def try_get_day(day = -1):
    if day == -1:
        day = int(os.path.basename(os.getcwd()))

    if day < 1 or day > 25:
        click.echo('Day must be between 1 and 25', err=True)
        exit(1)

    return day

def try_get_year(year = -1):
    if year < 0:
        try:
            branch = Repo('.').active_branch
            year = int(branch.name)
        except:
            try:
                branch = Repo('..').active_branch
                year = int(branch.name)
            except:
                click.echo('Could not get year from branch name', err=True)

    if year < 2015 or datetime.now().year < year:
        click.echo('Year must be between 2015 and current year', err=True)
        exit(1)

    return year

@cli.command()
@click.argument('day', type=int)
def prep(day: int):
    day = try_get_day(day)

    dirname = f'{day:02d}'
    os.makedirs(dirname, exist_ok=True)
    with open(f'{dirname}/input', 'w') as f:
        f.write('')
    with open(f'{dirname}/example', 'w') as f:
        f.write('')
    with open(f'{dirname}/day{dirname}.py', 'w') as f:
        f.write('''#!/usr/bin/env python3

import os

fdir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(fdir, 'input'), 'r') as f:
    content = f.read()''')

    os.chmod(f'{dirname}/day{dirname}.py', 0o755)
    click.echo(f'Day {day} prepared')

@cli.command()
@click.option('--day', '-d', type=int, default=-1)
@click.option('--year', '-y', type=int, default=-1)
def dl(day: int, year: int):
    day = try_get_day(day)
    year = try_get_year(year)

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookie = ''
    fdir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(fdir, 'cookie'), 'r') as f:
        cookie = f.read().strip()
    res = httpx.get(url, headers={'cookie': cookie}).content
    with open(os.path.join(fdir, f'{day:02d}/input'), 'w') as f:
        f.write(res.decode('utf-8'))


@cli.command()
@click.argument('part', type=int)
@click.argument('result', type=str)
@click.option('--day', '-d', type=int, default=-1)
@click.option('--year', '-y', type=int, default=-1)
def submit(day: int, year: int, part: int, result: str):
    day = try_get_day(day)
    year = try_get_year(year)

    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    cookie = ''
    fdir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(fdir, 'cookie'), 'r') as f:
        cookie = f.read().strip()
    res = httpx.post(url, data={'level': part, 'answer': result}, headers={'cookie': cookie})
    if "That's the right answer!" in res.text:
        click.secho('Correct answer!', fg='green')
    elif "Did you already complete it?" in res.text:
        click.secho("That doesn't seem like the right level. Did you already complete it?", fg='yellow')
    elif "That's not the right answer; your answer is too high." in res.text:
        click.secho("That's not the right answer; your answer is too high.", fg='red')
    elif "You gave an answer too recently" in res.text:
        click.secho("You gave an answer too recently.", fg='yellow')
        seconds = re.findall(r'You have (\d+)s left', res.text)
        if seconds and len(seconds) > 0:
            click.secho(f"Wait another {seconds[0]} seconds.", fg='yellow')
    else:
        print(res.text)

@cli.command()
def test():

    try_get_year()

if __name__ == '__main__':
    cli()
