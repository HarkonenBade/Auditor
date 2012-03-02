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
set output 'tstNUM-accuracy.png'
set title "Test Set NUM - Accuracy" 
set xlabel "K-Value" 
set xrange [ 1.00000 : 20.0000 ] noreverse nowriteback
plot "tstNUM.dat" i 0 u 1:2 t "Correct" w lines,\
"" i 0 u 1:3 t "Fail" w lines,\
"" i 0 u 1:4 t "Miss" w lines#,\
#"" i 2 u 1:7 t "AFS-NF" w imp,\
#"" i 2 u 2:7 t "AFS-WF" w imp,\
#"" i 2 u 3:7 t "MIFS-NF" w imp,\
#"" i 2 u 4:7 t "MIFS-WF" w imp,\
#"" i 2 u 5:7 t "MAFS-NF" w imp,\
#"" i 2 u 6:7 t "MAFS-WF" w imp
#    EOF
