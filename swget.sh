#!/bin/bash

#grabs a search term or terms from the command line and uses wget to search#
#ToDo - make it interactive and use wget -r flag to download info

echo $#
search="https://duckduckgo.com/html/?q="
for i in $@
do
	search+=$i
	search+='+'
done

wget -r --output-document=- $search

