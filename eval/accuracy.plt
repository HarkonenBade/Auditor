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
set terminal pngcairo  size 800, 800 
set output 'mp3img-paccuracy.png'
set multiplot layout 3,1 title "Combined Accuracy Tests"

set ylabel "Percentage Proportion"
set xlabel "Training Iteration"
set xrange [ 0.00000 : 19.0000 ] noreverse nowriteback
set title "Perfect Test Case"
plot "mp3img/perfect/data.dat" i 0 u 1:2 t "Correct" w lines,\
"" i 0 u 1:3 t "Fail" w lines,\
"" i 0 u 1:4 t "Miss" w lines
set title "Scramble Test Case"
plot "mp3img/scramble/data.dat" i 0 u 1:2 t "Correct" w lines,\
"" i 0 u 1:3 t "Fail" w lines,\
"" i 0 u 1:4 t "Miss" w lines
set title "Download Test Case"
plot "mp3img/dlscram/data.dat" i 0 u 1:2 t "Correct" w lines,\
"" i 0 u 1:3 t "Fail" w lines,\
"" i 0 u 1:4 t "Miss" w lines


