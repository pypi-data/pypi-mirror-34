__version__ = "0.0.2"

__doc__ = """"
rpcdb framework to interact with mysql.
Has a client and server.
Client connects through a remote procedure call to an xmrpc server
that controls the database through a proxy/controller.
The controller 'talks' to the database and returns query reults.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rpcdb.client.client_proxy import Proxy
from rpcdb.client import Base
from rpcdb.server import rpcserver
from rpcdb.server.sqlconnection import Connection

__all__ = 'Base', 'rpcserver', 'Proxy', 'Connection'

