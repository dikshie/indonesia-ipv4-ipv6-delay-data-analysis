set term png
set output "borobudur.ntt.cdf.png"
set title "Cummulative Distribution Function (CDF) IPv4-IPv6"
set ylabel "CDF"
set xlabel "RTT (ms)"
plot "borobudur.ntt.pair.dat.cdf" u 2:1 t "v4", "borobudur.ntt.pair.dat.cdf" u 4:3 t "v6"  
