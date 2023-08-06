# Copyright 2018 leoetlino <leo@leolam.fr>
# Licensed under GPLv2+
import os
import subprocess
from typing import Union

def get_path(rel_path: str):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), rel_path)

_tool_name = 'wszst' if os.name != 'nt' else get_path('wszst/wszst.exe')

def compress(data: Union[bytes, memoryview], level: int = 10) -> bytes:
    return subprocess.run([_tool_name, "comp", "-", "-d-", f"-C{level}"], input=data, # type: ignore
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout

def decompress(data: Union[bytes, memoryview]) -> bytes:
    return subprocess.run([_tool_name, "de", "-", "-d-"], input=data, # type: ignore
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout

def decompress_file(file_path: str) -> bytes:
    return subprocess.run([_tool_name, "de", file_path, "-d-"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout
