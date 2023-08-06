#!/usr/bin/env python3
import random as rand
from multiprocessing import Process, Queue
from multiprocessing.pool import Pool

import click

import lztools.Data.Images
from Resources.Requirements import apt_requires
from lztools.Bash import command_result, command, search_history
from lztools.Data import Images
from lztools.text import search_words, get_random_word, regex as rx

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

colorizations = ['none', 'rainbow', 'altbow', 'metal']

def try_read_input(input):
    try:
        return "\n".join(input.readlines())[:-1]
    except:
        return input

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A collection of python tools and bash commands by laz aka nea"""

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("term")
@click.option("-r", "--regex", is_flag=True, default=False)
def history(term, regex):
    """Search bash history"""
    for line in search_history(term, regex=regex):
        print(line)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("term", default="")
@click.option('-t', '--type', type=click.Choice(['words', 'images']), help="The type of search")
@click.option("-s", "--strict", is_flag=True, default=False, help="Indicates that letters has to appear in the same order as the do in TERM")
@click.option("-m", "--max-images", default=1, type=click.IntRange(1, 500), help="Max number of images")
def search(term, type, strict, max_images):
    if type == "words":
        res = search_words(term, strict=strict)
        print(res)
    elif type == "images":
        res = lztools.Data.Images.search(term, count=max_images)
        for x in res:
            print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option('-t', '--type', type=click.Choice(['words', 'images', 'colorization']), default='images', help="Random category")
@click.option("-c", "--count", default=1, help="The number of results")
@click.option("-nn", "--not-nocolor", is_flag=True, default=False, help="Random colorization never selects no color")
@click.argument("input", default=click.get_text_stream('stdin'))
def random(type, count, not_nocolor, input):
    if type == "images":
        res = Images.get_random_image(count=count)
        for x in res:
            print(x)
    elif type == "words":
        for _ in range(count):
            print(get_random_word())
    elif type == "colorization":
        choices = colorizations
        input = try_read_input(input)
        if not_nocolor:
            choices = colorizations[1:]
        color(input, rand.choice(choices), not_nocolor=not_nocolor)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("input", nargs=-1)
@click.option("-d", "--delimiter", nargs=1, help="The delimiter to split the input by")
def split(input, delimiter):
    i = str.join("\n", input).strip()
    if delimiter:
        i = i.split(delimiter)
    else:
        i = i.splitlines()
    for x in i:
        print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("start")
@click.argument("end")
@click.argument("Text", default=click.get_text_stream('stdin'))
@click.option("-p", "--partial-matches", is_flag=True, default=False, help="Used if indicators are not complete lines")
def cut(start, end, text, partial_matches):
    p = False
    for l in text.splitlines():
        if partial_matches:
            if end in l:
                p = False
        else:
            if l == end:
                p = False
        if p:
            print(l)
        if partial_matches:
            if start in l:
                p = True
        else:
            if l == start:
                p = True

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("expr")
@click.argument("Text", default=click.get_text_stream('stdin'))
@click.option("-s", "--single-result", is_flag=True, default=False)
def regex(expr, text, single_result):
    input = try_read_input(text)
    print(input, expr)
    if not single_result:
        for x in rx(expr, input, only_first=single_result, suppress=True):
            print(x)
    else:
        print(rx(expr, input, only_first=single_result, suppress=True))

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("input")
@click.option('-t', '--type', type=click.Choice(colorizations))
@click.option("-nn", "--not-nocolor", is_flag=True, default=False)
def colorize(input, type, not_nocolor):
    color(input, type, not_nocolor)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-s", "--speed", type=float, default=20)
@click.option("-f", "--frequency", type=float, default=0.1)
@click.option("-a", "--animate", is_flag=True, default=False)
@click.argument("input")
def rainbow(speed, frequency, animate, input):
    args = []
    if animate:
        args.append("-a")
        args.append("--speed")
        args.append(str(speed))

    args.append("--freq")
    args.append(str(frequency))

    command("echo \"{}\" | lolcat {}".format(input, str.join(" ", args)))

def color(input, type, not_nocolor):
    if type == 'none':
        print(input)
    elif type == 'rainbow':
        print(command_result("toilet", "-f", "term", "--gay", input))
    elif type == 'altbow':
        command("echo \"{}\" | lolcat".format(input))
    elif type == 'metal':
        print(command_result("toilet", "-f", "term", "--metal", input))

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-w", "--width", type=int, default=100)
@click.option("-i", "--invert", is_flag=True, default=False)
@click.option("-c", "--add-color", is_flag=True, default=False)
@click.argument("target")
def art(width, invert, add_color, target):
    args = []

    if invert:
        args.append("-i")
    if color:
        args.append("-c")

    args.append("--width")
    args.append(str(width))

    args.append(target)
    command("asciiart", *args)

@main.command(context_settings=CONTEXT_SETTINGS)
def install():
    command("sudo apt install -y {}".format(str.join(" ", apt_requires)))

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option('-o', '--operation', type=click.Choice(["bashrc", "autosource"]))
def bash(operation):

    pass

def to_art(url, width, color):
    args = ["art", url, f"-w {str(width-2)}"]
    if color:
        args.append("-c")
    return command_result("lztools", *args)

def queue_image(q, image, width):
    q.put(to_art(image, width))

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-n", "--noire", is_flag=True, default=False)
def fun(noire):
    term_width = int(command_result("tput", "cols"))
    q = Queue()
    images = Images.get_random_image(count=300)

    with Pool(5) as p:
        for result in  p.map(to_art, [(i, term_width, noire) for i in images]):
            print(result)

# @main.command(context_settings=CONTEXT_SETTINGS)
# @click.option("-n", "--noire", is_flag=True, default=False)
# def fun(noire):
#     res = int(command_result("tput", "cols"))
#     ps = []
#
#     with Pool(5) as p:
#         for result in  p.map(to_art, [(i, res, noire) for i in Images.get_random_image(count=300)]):
#             print(result)

if __name__ == '__main__':
    main()




