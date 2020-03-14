# Python Overview

Python Keywords and Identifiers

	In this tutorial, you will learn about keywords (reserved words in Python) and identifiers (names given to variables, functions, etc.).

	Python Keywords
	
		Keywords are the reserved words in Python.
		We cannot use a keyword as a variable name, function name or any other identifier.
		They are used to define the syntax and structure of the Python language.
		In Python, keywords are case sensitive.		
		All the keywords except True, False and None are in lowercase and they must be written as it is.
		
		Keywords in Python
		False	class	finally	is	return
		None	continue	for	lambda	try
		True	def	from	nonlocal	while
		and	del	global	not	with
		as	elif	if	or	yield
		assert	else	import	pass	 
		break	except	in	raise	 
		
	Python Identifiers
	
		An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate 
		one entity from another.
		
		Rules for writing identifiers
		Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) 
		or an underscore _. Names like myClass, var_1 and print_this_to_screen, all are valid example.
		An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
		Keywords cannot be used as identifiers.
		
		>>> global = 1
		File "<interactive input>", line 1
			global = 1
				^
		SyntaxError: invalid syntax
		We cannot use special symbols like !, @, #, $, % etc. in our identifier.
		
		>>> a@ = 0
		File "<interactive input>", line 1
			a@ = 0
			^
		SyntaxError: invalid syntax
		
		Things to Remember
		Identifier can be of any length.
		Python is a case-sensitive language. This means, Variable and variable are not the same.
		Multiple words can be separated using an underscore, this_is_a_long_variable.