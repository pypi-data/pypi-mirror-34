import os
from pathlib import Path
from subprocess import run

import lztools
from lztools import text

bashrc_symbols = {
    "customSection": "# ▂▃▅▇█▓▒░LAZ░▒▓█▇▅▃▂",
    "aliasStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> ALIAS START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
    "aliasEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> ALIAS END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
    "exportStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> EXPORT START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
    "exportEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> EXPORT END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
    "variablesStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> VARIABLES START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
    "variablesEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> VARIABLES END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
    "otherStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
    "otherEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
}

def command_result(name, *args):
    try:
        result = run([name, *args], capture_output=True, universal_newlines=True)
        # x = check_output([name, *args], universal_newlines=True)
        #
        # Popen()
        return result.stdout
    except:
        raise

def command(command, *args):
    fargs = " ".join(args)
    os.system(f"{command} {fargs}")

def apt_install(package):
    command(f"sudo apt install -y {package}")

def get_bashrc_path() -> str:
    return f"{str(Path.home())}/.bashrc"

def get_bashrc_other_path() -> str:
    return f"{lztools.__path__[0]}/resources/bashrc"

def get_bashrc() -> str:
    return command_result("cat", get_bashrc_path())

def get_bashrc_other() -> str:
    other_path = get_bashrc_other_path()
    return command_result("cat", other_path)

def _rcadd(text, symbol):
    start, end = get_bashrc().split(symbol, 1)
    start = start + text
    end = symbol + end
    return f"{start}\n{end}"

def _rccopy(rc, replacement, symbol):
    start, _ = rc.split(symbol, 1)
    _, replacement = replacement.split(symbol, 1)
    return start[:-1] + symbol + replacement

def add_bashrc_alias(text):
    print(_rcadd(text, bashrc_symbols["aliasEnd"]), end="")

def add_bashrc_variabel(text):
    print(_rcadd(text, bashrc_symbols["variablesEnd"]), end="")

def add_bashrc_export(text):
    print(_rcadd(text, bashrc_symbols["exportEnd"]), end="")

def add_bashrc_other(text):
    print(_rcadd(text, bashrc_symbols["otherEnd"]), end="")

def copy_bashrc_other(to_me:bool=True, out_path:str=None):
    if to_me:
        old = get_bashrc()
        new = get_bashrc_other()
        path = get_bashrc_path()
    else:
        old = get_bashrc_other()
        new = get_bashrc()
        path = get_bashrc_other_path()

    if out_path is not None:
        path = out_path

    new_rc = _rccopy(rc=old, replacement=new, symbol=bashrc_symbols["customSection"])

    with open(path, "w") as f:
        f.write(new_rc)

def get_history():
    return command_result("cat", "{}/.bash_history".format(str(Path.home())))

def search_history(term, regex=False):
    if not regex:
        for line in get_history().splitlines():
            if term in line:
                yield line
    else:
        return text.regex(term, get_history())
