Python library to load credentials or other sensitive data for .json format file.
Credentials must be stored under ``~/.credentials.json` in key:value dictionary format.

Example::

  {
   "device1":
      { "username": "federico.olivieri", "password": "p4ssw0rd" },
    "device2":
      { "username": "olivierif", "password": "mys3cr3t" }
  }

If you want change default location of .credentials.json file you need to modify file path under `__init__` methond

How to run it::

  db = credPass()
  db.load('device1','password') # 'p4ssw0rd'
