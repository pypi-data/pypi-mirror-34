#!/usr/bin/env python3
import pathlib

import click

from lztools.Bash import get_bashrc, add_bashrc_alias, copy_bashrc_other
from lztools.click import proper_group, proper_command

@proper_group()
def main():
    """A collection of python tools and bash commands for manipulating text by laz aka nea"""

@proper_command()
@click.argument("line")
@click.option('-t', '--type', type=click.Choice(["alias", "export", "variable", "other"]), default="other")
def rcadd(line, type):
    """Adds a line to .bashrc"""
    if type == "alias":
        add_bashrc_alias(line)


@proper_command()
@click.option("-t/-f", "--to-me/--from-me", is_flag=True, default=False)
def rccopy(to_me):
    """Adds a line to .bashrc"""
    copy_bashrc_other(to_me)


