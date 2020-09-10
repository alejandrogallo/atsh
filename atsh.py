#!/usr/bin/env python
# taritz: sudo nix-shell --run "st -e python %"
from typing import List
import serial
import yaml
import re
import inspect
import imei
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter


def get_aliases() -> dict:
    with open("aliases.yml") as f:
        return yaml.load(f)


def get_at_commands() -> dict:
    with open("reference.yml") as f:
        return yaml.load(f)


def repl(port: str, prompt_text: str) -> None:

    aliases = get_aliases()  # type: dict

    def get_user_commands() -> List[str]:
        return list(aliases.keys()) + list(commands.keys())

    commands \
        = { ":h": lambda: print("\n".join(get_user_commands()))
          , ":imei-check": lambda x: print(imei.check_imei_sum(x))
          , ":imei-unlock-code": lambda x: print(imei.compute_imei_unlock_code(x))
          }

    all_commands = {}
    all_commands.update(aliases)
    all_commands.update(get_at_commands())
    #all_commands.update(commands)

    completer = FuzzyWordCompleter(
        words=all_commands.keys(),
        meta_dict={w: " ".join(c["desc"] for c in v["commands"])
                   for w, v in all_commands.items()},
        WORD=True
    )


    com = serial.Serial(port=port,
                        timeout=.1,
                        rtscts=True,
                        dsrdtr=True,
                        baudrate=9600)

    try:
        while True:
            #user_input = input(prompt)
            user_input = prompt(prompt_text,
                                completer=completer,
                                complete_while_typing=True
                                )
            if user_input in all_commands:
                cmds = [{"cmd": c["cmd"] + '\r\n', "desc": c["desc"]}
                        for c in all_commands[user_input]["commands"]]
            elif user_input.split(" ")[0] in commands:
                name, *args = user_input.split(" ")
                f = commands[name]
                cmds = f(*args)
                if not cmds: continue
            else:
                cmds = [{"cmd": '{}\r\n'.format(user_input.upper()), "desc": ""}]

            for cmd in cmds:
                print("\x1b[31m« \x1b[0m",
                      cmd["cmd"].replace("\n", "").replace("\r", ""),
                      " \x1b[35m# ", cmd["desc"], "\x1b[0m")
                com.write(cmd["cmd"].encode())
                print("")
                output = com.read(4096).decode("utf-8")
                print("\n".join(re.sub(r"^", "\x1b[32m»\x1b[0m", o)
                                for o in output.split("\n")))
    except EOFError:
        pass

    print("exiting")
    com.close()

if __name__ == "__main__":
    u = "/dev/serial/by-id/usb-Sierra_Wireless_Inc._Sierra_Wireless_EM7345_4G_LTE_013937007484700-if02"
    u = "/dev/ttyUSB0"
    u = "/dev/ttyACM0"
    u = "/dev/tty0"
    prompt_text = "> "
    repl(port=u,
         prompt_text=prompt_text)
