from pathlib import Path

import click

from lztools.click import proper_group, proper_command
from lztools.modules import local_install, get_version, add_versions

@proper_group()
def main():
    """Python utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""

@proper_command()
@click.argument('paths', nargs=-1, type=click.Path())
@click.option("-u", "--upload", is_flag=True, default=False)
@click.option("-a", is_flag=True, default=False, help="Adds 0.0.1 to version number")
@click.option("--add", default=None, type=str, help="Adds amount to version number (Default: 0.0.1)")
def install(paths, upload, a, add):
    """Installs one or more python3.7 modules and more by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙

    \b
    -a X.X.X                Adds amount to version number
    --add-to-version X.X.X  Format: X.X.X where X is any integer
                            If no value is passed in the added amount defaults to 0.0.1
                            \b
                            Exampel 1: Default of 0.0.1 added
                            if original version is 0.0.0
                            lpy -a
                            the new version will be 0.0.1
                            \b
                            Exampel 2: 3.2.1 added
                            if original version is 1.2.3
                            lpy -a 3.2.1
                            the new version will be 4.4.4
                            \b
                            Exampel 3: 0.3.0 added and path specified
                            if original version is 3.0.3
                            lpy -a 0.3.0 path/to/module
                            the new version will be 1.2.3
                            \b
                            Exampel 4: Default of 0.0.1 added and path specified
                            if original version is 1.2.2
                            lpy path/to/module -a
                            the new version will be 1.2.3
                            \b
    -p, paths [paths]       The paths to install modules from
                            \b
    -u, --upload            Uploads package using twine
    """
    if a or add is not None:
        if add is None:
            add = "0.0.1"

    if not paths:
        local_install(".", upload, add)
    else:
        for x in paths:
            local_install(str(Path(x).absolute()), upload, add)


