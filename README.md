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
