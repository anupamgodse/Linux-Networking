1. Monitoring script:

Usage:
./log_loads.sh T TP X Y
where,
T = interval at which loads are logged
TP = total duration to run the script
X = 1 min load average thereshold for detecting HIGH CPU usage
Y = 5 min load average threashold for detecting VERY HIGH CPU usage

Working:

i) total runs = TP/T
ii) In each run,
	a) current load averages are logged to a "load.csv" file with a timestamp
	b) alerts are generated and logged to "load_alerts.csv" using following criteria
		i) If current 1 min load avg is greater than the threshold X then, HIGH CPU usage alert is logged 
		ii) If current 5 min load avg is greater than the threshold Y and the 1 min load avg is increasing
		    (assument strictly increasing) Very HIGH CPU usage alert is logged 
	c) sleep for T secs

Note: This script does not check for input arguments error. Please enter correct argument values.


2. Log cleaning scripts:

Usage:
./clear_logs.sh

Working:

This script runs forever, in each run it sleeps for 3600 seconds, on wakeup it removes the log files, load.csv and load_alerts.csv


3. Cron job
Not needed for monitoring script as it runs for TP secs only. The log_loads.sh itself runs for TP seconds.

Not needed for current implementation of log cleaning scripts. Currently the log cleaning script runs forever and cleans logs every hour.

If we want to clean logs at exact hours we can do this by writing a cron job by adding following line in user's crontab:

"0 * * * * /absolute/path/to/your/clear_logs.sh"

where "/absolute/path/to/your/" is path of folder where clear_logs.sh exists

Now, clear_logs.sh would simply have single line "rm -rf load.csv load_alerts.csv".
