set term png
set output "ns1.telkom.scatter.png"
set title "Scatter Plot IPv6 vs IPv4"
set ylabel "IPv6 RTT (msec)"
set xlabel "IPv4 RTT (ms)"
set yrange [0:300]
set xrange [0:300]
plot "ns1.telkom.net.pair.dat" u 1:2 t "", "dummy.txt" u 1:2 w lines t "" 
