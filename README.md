# Website Down Detector
This is a small python application to track the history and status of any website. The website will be requested at specific intervals and log the status, either off (0) or on (1).

## Running
The program takes two command line arguments; a string url and an int update time. The url will be the website you wish to track the status and history of while the update time will be a delay (in seconds) between each request. The command will look as follows:

``` console
python3 logger.py [url] [update_time]
```

The output is saved to a file called output.log.

<hr/>

<small>
website-down-detector by Cameron Bonesteel is under an MIT License. Check LICENSE.md for more information.
</small>