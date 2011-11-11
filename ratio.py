#!/usr/bin/python

import sys

filename = sys.argv[1]
fd = open(filename, 'rb')
ipv4 = []
ipv6 = []
for line in fd.readlines():
    #print line
    ipv4.append(float(line.split()[0]))
    ipv6.append(float(line.split()[1]))
fd.close()
ratio_=[]
for i in range (len(ipv4)):
    ratio_.append((ipv4[i]/ipv6[i]))

#percentage
j=0
k=0
for i in range(len(ipv4)):
    if (ratio_[i] > 1):
        j=j+1 #IPv6 delay better than IPv4 delay
    else:
        k=k+1 #IPv4 delay better than IPv6 delay

total=float(len(ipv4))
print j, k, float(float(j)/total)*100 , float(float(k)/total)*100

#CDF IPv4 first
ipv4.sort()
prob_1 = 0
cdf_11 =[]
cdf_12 =[]
for time in ipv4:
    prob_1 += 1.0/len(ipv4)
    #print "%.4f\t%.4f" % (prob_1, time)
    cdf_11.append(prob_1)
    cdf_12.append(time)

#CDF IPv6
ipv6.sort()
prob_2 = 0
cdf_21=[]
cdf_22=[]
for time in ipv6:
    prob_2 +=1.0/len(ipv6)
    #print "%.4f\t%.4f" % (prob_2, time)
    cdf_21.append(prob_2)
    cdf_22.append(time)

filename=filename+'.cdf'
FILE = open(filename,"w")
for i in range(len(cdf_11)):
    #print cdf_11[i], cdf_12[i], cdf_21[i], cdf_22[i]
    FILE.writelines("%.4f %.4f %.4f %.4f\n" % (cdf_11[i] , cdf_12[i] , cdf_21[i] , cdf_22[i]))
FILE.close()
