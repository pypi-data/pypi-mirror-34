from lztools.click import proper_group

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@proper_group
def main():
    """Main test"""