# Website Down Detector
This is a small python application to track the history and status of any website. The website will be requested at specific intervals and log the status, up or down, and graph it to the history chart.

## Installing
This application uses matplotlib to graph the status. There are a couple ways you can install the necessary requirements.

### Method 1 - Anaconda
Using Anaconda is likely the easiest way to get this installed as most users using matplotlib have likely used this before. You can find the download instructions for Anaconda [here](https://www.anaconda.com/products/individual). After Anaconda is installed you can use either of the following commands to install matplotlib and numpy:

``` console
conda install matplotlib
conda install numpy
```

or
``` console
pip install -r requirements.txt
```

### Method 2 - TkAgg
Alternatively, you can install all the packages needed to run the program using TkAgg. Run these commands below and then uncomment line 5 in detector.py:

If matplotlib and numpy are not installed, use this command:
``` console
pip install -r requirements.txt
```

Then run these commands:
``` console
apt install tk-dev libpng-dev libffi-dev dvipng texlive-latex-base
pip install cairocffi
pip install --upgrade matplotlib
```

## Running
The program takes two command line arguments; a string url and an int update time. The url will be the website you wish to track the status and history of while the update time will be a delay (in seconds) between each request. The command will look as follows:

``` console
python3 detector.py [url] [update_time]
```

<hr/>

<small>
website-down-detector by Cameron Bonesteel is not licensed in any way. This code is provided as is and may be used and/or modified.
</small>