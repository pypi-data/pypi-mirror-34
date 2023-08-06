# Simple PyIRC

This project aims at providing a very simple IRC client that can be easily
used in Python scripts to ouput some results or information.

The client is written in Python3, respects PEP-8 syntax and should be
fully documented with reST-formatted docstrings.

It supports both [RFC 1459](https://tools.ietf.org/html/rfc1459) and
[RFC 2812](https://tools.ietf.org/html/rfc2812) server implementations.

This project is not a full-blown IRC client. It is not meant to act as a bot
which would listen and react to IRC messages. For such usage, refer to
[PyPI's irc package](https://pypi.org/project/irc/) for instance. This 
IRC client is meant to be lighter and simply send messages to a channel or to
an another user from time to time.


## Usage

The targeted use case is to be able to connect to a set of specific channels
on a server, keep the connection alive and be able to send messages to this
channel from time to time when other components of the project require it.

```python
from simple_pyirc import IRCClient


irc_client = IRCClient("my.irc.network", "mynick")

irc_client.join("#chan")

# Do something ...

irc_client.privmsg("#chan", "Result: 42")

# Do something else ...

irc_client.quit()
```

Or one can also use the context manager if a quick connection is required:

```python
from simple_pyirc import IRCClient

with IRCClient("my.irc.network", "mynick") as irc_client:
    irc_client.join("#chan")
    irc_client.msg("#chan", "Hello & Good Bye !")
```
