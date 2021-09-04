from enum import Enum
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import re
import pandas as pd
import os, sys

rx_dict = {
    'ip': re.compile(r'ip=(.*)\n'),
    'port': re.compile(r'port=(.*)\n'),
}

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0

def _parse_line(line):
    """
    Do a regex search against all defined regexes and
    return the key and match result of the first matching regex

    """

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    # if there are no matches
    return None, None


def parse_config_file(filepath):
    """
    Parse text at given filepath

    Parameters
    ----------
    filepath : str
        Filepath for file_object to be parsed

    Returns
    -------
    data : pd.DataFrame
        Parsed data

    """
    
    ip = ""
    port = 0

    data = []  # create an empty list to collect the data
    # open the file and read through it line by line
    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        while line:
            # at each line check for a match with a regex
            key, match = _parse_line(line)

            # extract ip address
            if key == 'ip':
                ip = line.split("=", 1)[1]
                ip = ip.split("\n", 1)[0]

            # extract port
            if key == 'port':
                port = line.split("=", 1)[1]
                port = port.split("\n", 1)[0]
                port = int(port)
            
            line = file_object.readline()

    return ip, port
