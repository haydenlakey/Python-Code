#Create path coverage
#Hayden Lakey
#LKYHAY001
#11 April 2022 
""" 
>>> import numberutil
>>> numberutil.aswords(10)
'ten'
>>> numberutil.aswords(-1)  
'ninety nine'
>>> numberutil.aswords(1000)
'ten hundred'
>>> numberutil.aswords(0) 
'zero'
>>> numberutil.aswords(247)
'two hundred and forty seven'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(1001)
'ten hundred and one'
>>> numberutil.aswords(3)
'three'

"""
import doctest
doctest.testmod(verbose=True)
