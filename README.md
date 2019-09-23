# MarcLinter

A little test repo I wrote when LIS 415 was going over MARC 21 encoding. The idea is that I can feed the program bulk sets of MARC encoding after I constrain the script with exceptions, to find where I'm misunderstanding the specification. Basically it's like a reverse linter; I'm the one being linted (assuming that the data in is all good), but it should be able to tell when any breaking changes are made to existing MARC records as well.

The repo currently only takes in text files; xml may happen later, but I'm not that excited about it...that's not as fun a problem to solve.

The json specification for the MARC fields was borrowed from [pkiraly](http://pkiraly.github.io/2018/01/28/marc21-in-json/).

