# METODO GET 
picnicItems	=	{'apples':	5,	'cups':	2} se

'I	am	bringing	'	+	str(picnicItems.get('cups',	0))	+	'	cups.'

	'I	am	bringing	'	+	str(picnicItems.get('eggs',	0))	+	'	eggs.'
'''
É	tedioso	verificar	se	uma	chave	está	presente	em	
um	dicionário	antes	de acessar	o	valor	dessa	chave.	Felizmente,	
os	dicionários	têm	um	método	get() que	aceita	dois	argumentos:	
a	chave	do	valor	a	ser	obtido	e	um	valor alternativo	a	ser
retornado	se	essa	chave	não	existir.
'''
