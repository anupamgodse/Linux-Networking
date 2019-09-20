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

All logging scripts are created in "$HOME/"

Note: This script does not check for input arguments error. Please enter correct argument values.

2. Log cleaning scripts:

Usage:
./clear_logs.sh

Working:

This script runs forever, in each run it sleeps for 3600 seconds, on wakeup it removes the log files, load.csv and load_alerts.csv


3. Cron jobs

*Cronjob for implementing 5.1 and 5.2 is not needed, because
Not needed for monitoring script itself as it runs for TP secs only. The log_loads.sh itself runs for TP seconds.

Not needed for current implementation of log cleaning scripts. Currently the log cleaning script runs forever and cleans logs every hour.

If we want to clean logs at exact hours we can do this by writing a cron job by adding following line in user's crontab:

"0 * * * * $HOME/clear_logs.sh"

Assuming clear_logs.sh exists in $HOME directory

Now, clear_logs.sh would simply have single line "rm -rf load.csv load_alerts.csv".

* Cron job for testing 5.1 and 5.2

No cronjob was created for cleaning log files as script itself runs forever

Created 2 cron jobs as follows

"0 * * * * $HOME/log_loads.sh 5 1800 1 1.5"
and,
"10 * * * * stress -c 4 -t 100"

The first one will invoke log_loads.sh every hour telling it to log load_averages every 5 seconds for 1800 seconds with 1 and 1.5 as X and Y
thresholds. This will log loads to $USER/load.csv and generate alerts in $USER/load_alerts.csv.

The second cronjob will run stress every hour at 10 mins, for 100 seconds which will create load on CPU. This will generate log alerts.

Also we will start clear_logs.sh script which will keep on cleaning the log files.

The cronjobs and clear_logs.sh was run for 24 hours and no exceptions were observed.
