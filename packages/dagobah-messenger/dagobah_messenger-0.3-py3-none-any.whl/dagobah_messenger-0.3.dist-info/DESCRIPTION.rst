### dagobah-messenger ###
JSON instant messenger with presence control and AES encryption.

### Install ###

    pip install dagobah-messenger

### How to start ###

1. Run server:

		python3 -m dagobah-messenger -m server

2. Run any number (max 5) of GUI or console clients:

		python3 -m dagobah-messenger  # run console client
		python3 -m dagobah-messenger -m clnt_gui  # run GUI client
		python3 -m dagobah-messenger  # run console client (default)
		python3 -m dagobah-messenger -m clnt_cli  # run console client


P.S. Use PyCharm to avoid module not found issue with pycryptodome.

Thx a lot to Leo Orlov and GeekBrains.
Ilia Kruglov, 31072018.


