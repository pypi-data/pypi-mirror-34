Help on package rpcdb:

NAME
    rpcdb

DESCRIPTION
    rpcdb framework to interact with mysql.
    Has a client and server.
    Client connects through a remote procedure call to an xmrpc server
    that controls the database through a proxy/controller.
    The controller 'talks' to the database and returns query reults.

PACKAGE CONTENTS
    __main__
    client (package)
    server (package)
    utils (package)

SUBMODULES
    chatclient
    console
    rpcserver
    util

CLASSES
    builtins.object
        base.Base
        rpcdb.server.sqlconnection.Connection

    class Base(builtins.object)
     |  Methods defined here:
     |
     |  __call__(self, **kwargs)
     |      Call self as a function.
     |
     |  __eq__(self, other)
     |      Return self==value.
     |
     |  __getitem__(self, index)
     |
     |  __init__(self, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self)
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  add_column(self, column, after)
     |
     |  alter_column(self, old_column, new_column)
     |
     |  as_csv_data(self, filename, iterable)
     |
     |  create_table(self)
     |
     |  delete(self)
     |
     |  description(self)
     |
     |  drop_column(self, column)
     |
     |  execute(self, sql)
     |
     |  exists(self)
     |      Check if a record of exists in table
     |
     |  get(self, as_dict=False, only_one=False, strict=True, groupby=None, orderby=None, sortby='ASC', limit=None, offset=None, **where)
     |
     |  getall(self, as_dict=False, only_one=False)
     |
     |  migrate(self)
     |
     |  onClear(self)
     |
     |  onDelete(self)
     |
     |  onFind(self)
     |
     |  onSave(self)
     |
     |  read_csv(self, filename)
     |
     |  save(self)
     |
     |  save_csv_data(self, data)
     |
     |  show(self)
     |
     |  show_record(self, data={})
     |
     |  update(self)
     |
     |  widget(self, parent, font='Consolas 13', relief='raised', bd=2, sticky='ew', label_fg='black', label_bg='SystemButtonFace')
     |
     |  write_to_csv(self)
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  schema() from base.BaseMeta
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  AGEFIELD = <class 'models.AGEFIELD'>
     |
     |
     |  BLOB = <class 'models.BLOB'>
     |
     |
     |  BOOLEAN = <class 'models.BOOLEAN'>
     |
     |
     |  CHAR = <class 'models.CHAR'>
     |
     |
     |  DATE = <class 'models.DATE'>
     |
     |
     |  DATETIME = <class 'models.DATETIME'>
     |
     |
     |  DECIMAL = <class 'models.DECIMAL'>
     |
     |
     |  DOUBLE = <class 'models.DOUBLE'>
     |
     |
     |  Descriptor = <class 'models.Descriptor'>
     |
     |
     |  ENUM = <class 'models.ENUM'>
     |
     |
     |  FLOAT = <class 'models.FLOAT'>
     |
     |
     |  FULLAGEFIELD = <class 'models.FULLAGEFIELD'>
     |
     |
     |  INTEGER = <class 'models.INTEGER'>
     |
     |
     |  LONGTEXT = <class 'models.LONGTEXT'>
     |
     |
     |  String = <class 'models.String'>
     |
     |
     |  TEXT = <class 'models.TEXT'>
     |
     |
     |  TIME = <class 'models.TIME'>
     |
     |
     |  VARCHAR = <class 'models.VARCHAR'>
     |
     |
     |  __hash__ = None
     |
     |  columns = {}
     |
     |  fields = []

    class Connection(builtins.object)
     |  Methods defined here:
     |
     |  __enter__(self)
     |
     |  __exit__(self, exc_type, exc_val, tb)
     |
     |  __init__(self, db=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  create_database(self, db)
     |
     |  use(self, db)
     |
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |
     |  connect(**kwargs) from builtins.type
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  manual_config = True
     |
     |  params = {}

FUNCTIONS
    Proxy(host, port)

DATA
    __all__ = ('Base', 'rpcserver', 'Proxy', 'Connection', 'chatclient', '...

VERSION
    0.0.5
