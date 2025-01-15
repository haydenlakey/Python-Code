#Test 12 hour input
#Hayden Lakey
#LKYHAY001 
#11 April 2022
"""
>>> import timeutil 
>>> timeutil.validate('11:37am.')
False
>>> timeutil.validate('01:23we am')
False
>>> timeutil.validate('12:61 am')
False
>>> timeutil.validate('21:15 p.m.')
False
>>> timeutil.validate('1:1 p.m.')
False
>>> timeutil.validate('231 p.m')
False

"""
import doctest
doctest.testmod(verbose=True)