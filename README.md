# pylogger
CLI command to generate and send well-formed syslog messages to a syslog receiver.
Follows most arg names as found in the *nix 'logger' command.

Messages are sent using TCP by default. The '--udp' option can be used to switch
to UDP instead.

## Message format
`<PRI>TIMESTAMP HOSTNAME TAG: MESSAGE`

This format reflects [RFC3164](http://www.ietf.org/rfc/rfc3164.txt).

## Example Usage

`pylogger.py --server 1.2.3.4 --tag "mytag" "Soylent Green is people!"`

You can see a list of CLI args and descriptions with --help:

`pylogger.py --help`

## To Do
* Rewrite of priority code to better match syslog priorities.

## Why?
Versions of the *nix ‘logger’ command prior to 2.26 did not send well-formed messages
and the latest version available for CentOS 7/RHEL 7 is 2.23. I wrote pylogger at
a time when I couldn't wait for the upstream version of 'logger' to make it into
CentOS/RHEL.

Ubuntu 16.04 has v. 2.27 so no problem there.