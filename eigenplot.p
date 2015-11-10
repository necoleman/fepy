# Gnuplot script file for eigenvalue plotting in file 'eig.dat'
# This file is 'eigenplot.p'
set surface
splot '<awk -f addblanks.awk eig.dat' using 1:2:4 with lines, '<awk -f addblanks.awk eig.dat' using 1:2:5 with lines, '<awk -f addblanks.awk eig.dat' using 1:2:6 with lines, '<awk -f addblanks.awk eig.dat' using 1:2:7 with lines, '<awk -f addblanks.awk eig.dat' using 1:2:8 with lines