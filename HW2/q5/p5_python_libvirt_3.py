import sys
import libvirt
import time
import operator

#CPU or MEM
usage_type = sys.argv[1]
if usage_type != 'CPU' and usage_type != 'MEM':
    print("Mention usage type")
    exit(1)

if usage_type == 'CPU':
    T = float(input("Enter CPU alert Threshold % "))
    f = open("alerts.csv", "a")

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

domainIDs = conn.listDomainsID()
usage_x = dict()
if domainIDs == None:
    print('Failed to get a list of domain IDs', file=sys.stderr)


def get_stats(usage_type):
    if usage_type == 'CPU':
        stats1 = dom.getCPUStats(True)
        time.sleep(1)
        stats2 = dom.getCPUStats(True)
        usage = 100 * ((stats2[0]['cpu_time'] - stats1[0]['cpu_time']) / 1000000000.)
        if(usage > T):
            alert = dom.name() + ", " + str(time.time()) + ", " + str(usage)
            print("HIGH CPU usage: ", alert)
            f.write(alert + "\n")
            
    else:
        stats = dom.memoryStats();
        #used = actual - unused
        usage = stats['actual'] - stats['unused']

    return usage


if len(domainIDs) == 0:
    print('  None')
else:
    for domainID in domainIDs:
        dom = conn.lookupByID(domainID)
        if dom == None:
    	    print('Failed to find the domain '+domName, file=sys.stderr)
    	    exit(1)
        
        usage_x[dom.name()] = get_stats(usage_type)

print(sorted(usage_x.items(), key=operator.itemgetter(1)))

do_loop = int(input("Do you want to calculate moving avg?(1/0)"))
if do_loop != 1:
    print("Enter 1 to calculate moving avg: exiting")
    exit(0)

windows = dict()
interval = int(input("Interval in seconds: "))
window_size = int(input("Window size: "))

for domainID in domainIDs:
    dom = conn.lookupByID(domainID)
    windows[dom.name()] = [usage_x[dom.name()]] 


while(1):
    time.sleep(interval)
    mov_avg = dict()
    for domainID in domainIDs:
        dom = conn.lookupByID(domainID)
        if dom == None:
    	    print('Failed to find the domain '+domName, file=sys.stderr)
    	    exit(1)
        lw = len(windows[dom.name()])
        windows[dom.name()].append(get_stats(usage_type))
        if(lw == window_size):
            windows[dom.name()].pop(0)
        mov_avg[dom.name()]=sum(windows[dom.name()]) / len(windows[dom.name()])
        #print(dom.name() + " " + usage_type + " moving avg = ", sum(windows[dom.name()]) / len(windows[dom.name()]))
    print(usage_type+" moving averages "+sorted(mov_avg.items(), key=operator.itemgetter(1)))        

conn.close()
exit(0)
