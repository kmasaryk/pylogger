#!/usr/bin/env python
#-------------------------------------------------------------------------------
#
# Name: pylogger.py
# Description: Send syslog formatted messages to a syslog receiver. Follows
#              arg names as found in the *nix 'logger' command.
#
# Message format: <PRI>TIMESTAMP HOSTNAME TAG: MESSAGE
#                 This format reflects RFC3164.
#
#-------------------------------------------------------------------------------

import argparse
import logging
import logging.handlers
import socket
import getpass

parser = argparse.ArgumentParser(__file__,
                                 description="Send a syslog formatted message to a syslog receiver")

parser.add_argument("--server",
                    "-n",
                    default="localhost",
                    help="Write to this remote server")

parser.add_argument("--port",
                    "-P",
                    type=int,
                    default=514,
                    help="Use this port for UDP or TCP connection")

parser.add_argument("--udp",
                    "-u",
                    action='store_true',
                    help="Generate UDP packets instead of TCP.")

parser.add_argument("--priority",
                    "-p",
                    default="DEBUG",
                    help="The syslog message log level: CRITICAL, ERROR, WARNING, INFO or DEBUG")

parser.add_argument("--tag",
                    "-t",
                    help="Mark the message with this tag")

parser.add_argument("msg",
                    help="The syslog message")


# This needs to be rewritten for the syslog handler
def string_to_level(log_level):
    """ Convert a commandline string to a proper log level
    @param string log_level     command line log level argument
    @return logging.LEVEL       the logging.LEVEL object to return
    """
    if log_level == "CRITICAL":
        return logging.CRITICAL
    if log_level == "ERROR":
        return logging.ERROR
    if log_level == "WARNING":
        return logging.WARNING
    if log_level == "INFO":
        return logging.INFO
    if log_level == "DEBUG":
        return logging.DEBUG
    return logging.NOTSET


args = parser.parse_args()

if not args.tag:
    tag = getpass.getuser()
else:
    tag = args.tag

msg_fmt = logging.Formatter(fmt='%(clienthostname)s %(tag)s: %(message)s')
d = {'clienthostname': socket.getfqdn(), 'tag': tag}
    
syslogger = logging.getLogger('SyslogLogger')
    
pri = string_to_level(args.priority)
syslogger.setLevel(pri)

if args.udp:
    transport=socket.SOCK_DGRAM
else:
    transport=socket.SOCK_STREAM

handler = logging.handlers.SysLogHandler(address=(args.server, args.port),
                                         facility=19, socktype=transport)
handler.setFormatter(msg_fmt)
syslogger.addHandler(handler)

syslogger.log(pri, args.msg, extra=d)
