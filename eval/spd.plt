#!/usr/bin/gnuplot -persist
#
#    
#    	G N U P L O T
#    	Version 4.4 patchlevel 4
#    	last modified November 2011
#    	System: Linux 3.2.5-1-ARCH
#    
#    	Copyright (C) 1986-1993, 1998, 2004, 2007-2011
#    	Thomas Williams, Colin Kelley and many others
#    
#    	gnuplot home:     http://www.gnuplot.info
#    	faq, bugs, etc:   type "help seeking-assistance"
#    	immediate help:   type "help"
#    	plot window:      hit 'h'
set terminal pngcairo  size 640, 480 
set output 'speed.png'
set title "Speed per Query Test" 
set xlabel "Tree Size"
set ylabel "Query Time"
set logscale
unset key
plot "data.dat" u 1:2 w lines
#    EOF
