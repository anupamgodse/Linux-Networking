plugin=$1
files=$(ls logs/${plugin}*)
echo -e "${plugin} ouputs for iperf traffic between kubernetes pods in 2 nodes"
for i in {1..10}
do
   echo ___________________________________________________________________________
   echo -e "Server output for throughput test ${i}:"
   cat logs/${plugin}_${i}_server.log
   echo
   echo
   echo -e "Client output for throughput test ${i}:"
   cat logs/${plugin}_${i}_client.log
   echo
   echo
done
