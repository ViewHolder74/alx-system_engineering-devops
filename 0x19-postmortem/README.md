# 0x19. Postmortem

##Tasks

####0. My first postmortem

https://twitter.com/devopsreact/status/834887829486399488 

**Summary**

From 3:00 PM to 10:00 PM GMT, An ecommerce website hosted on web01 ALX server resulted in 502 error messages. Any client accessing this page returned an error . The issue resulted into loss of 1 millon dollars. The root cause of this outage was a typing mistake in configuration files that caused a Website to malfunction.

##Timeline (all GMT)

   + 2:45 PM: Configuration push begins
   + 2:55 PM: Outage begins
   + 3:00 PM: Pagers alerted teams
   + 4:30 PM: Check status of server(running)
   + 7:40 PM: Check Django configuration files
   + 8:50 PM: Server restarts begin
   + 9:58 PM: 100% of traffic back online

##Root Cause & Resolution

####Root Cause
At 2:45 PM GMT, a configuration change was inadvertently released to our production environment without first being released to the testing environment. The change was made in settings.py file with a typo of statec instead of static in the following directory STATIC_ROOT = os.path.join(BASE_DIR, 'static/'). This problem caused a routing problem to return 502 error anytime the website is hit. The configuration error quickly caused all the serving threads to be consumed. Traffic was permanently queued waiting for a serving thread to become available. The server became repeatedly hanging and restarting as they attempted to recover and at 2:46 PM GMT, the service outage began.

####Resolution

At 3:00 PM GMT, the monitoring systems alerted our engineers who investigated and escalated the issue. By 4:30: PM, the incident response team identified that the monitoring system was exacerbating the problem caused by this typo.

At 8:50 PM, we attempted to restart server and it was running alright. This made us check server logs with ltrace to discover the typo settings.py configuration files. Since the file was big we could not risk fixing only one line and leaving potential other typos. So we used puppet script to replace any occurence of the typo in the entire file with the right word.

The jobs started to slowly recover, and we determined the overall recovery would be faster by a restart of the API infrastructure. By 9:25 PM, 90% of traffix was restored and 100% of traffic was routed to the API infrastructure at 9:58 PM.

####Corrective & Preventive Measures

In the last hours, we've conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and avoid repeating same mistakes:

    + Disable the current configuration release mechanism untill safer measures are implemented.
    + Change rollback process to be quicker and more robust.
    + Fix all typos in configuration files before deploying.
    + Programatically enforce staged rollouts of all configuration changes.
    + Improve process for auditing all high-risk configuration options.
