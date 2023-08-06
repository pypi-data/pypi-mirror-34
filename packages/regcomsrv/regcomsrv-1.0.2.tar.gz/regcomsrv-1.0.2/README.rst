Regcomsrv documentation
-------------------------
See at https://regcomsrv.readthedocs.io

Overwiew
--------
Package helps you to register or unregister COM-servers that defined in python packages.

Register from Python
--------------------
::

	from regcomsrv import reg
	import sys
	
	# set command line attributes
	sys.argv.clear()
	sys.argv.append(__file__)
	sys.argv.append("win32com.servers.dictionary")
	sys.argv.append("DictionaryPolicy")
	
	reg()

Unregister from Python
----------------------
::

	from regcomsrv import reg
	import sys
	
	# set command line attributes
	sys.argv.clear()
	sys.argv.append(__file__)
	sys.argv.append("win32com.servers.dictionary")
	sys.argv.append("DictionaryPolicy")
	sys.argv.append("--unregister")
	
	reg()

Register from command line
--------------------------
::

	python -m regcomsrv win32com.servers.dictionary DictionaryPolicy
	
Unregister from command line
----------------------------
::
	
	python -m regcomsrv -u win32com.servers.dictionary DictionaryPolicy

Show help
---------
::

	python -m regcomsrv -h