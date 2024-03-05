# Fix Date Time:
Simple script to let you change the datetime of an entire column in one or more excel spreadsheets. 

## Installation

### Windows .exe
You can simply download the fix_datetime.exe from this repository's release page. 

### Pip

>[!Note]
>Assuming you have a working version of python and pip installed.

It is recommended that you use a virtual python environment to install this:

```bash
pip install git+https://github.com/kcx1/FixDateTime
```

From here you can just call it from the command line like:

```bash
fix_datetime [args]
```

### From python
Start by cloning the repo:
```bash
git clone https://github.com/kcx1/FixDateTime
cd FixDateTime
pip install -r requirements.txt
```

Now you can run this from the command line:

```bash
python /path/to/FixDateTime/fix_date_time/fix_date_time.py [args]
```



## Using it


#### **UPDATED**
When you run this script - it will first look for a ```FixDateTime.toml``` in the XDG_CONFIG_HOME (if set) or in the user's home directory. If it finds a config file - it will use that config. Otherwise it will copy the builtin config over to that directory to either home or XDG_CONFIG_HOME (if set)

You can still pass an alternate config using the commandline argument. Simply add the '-c path/to/config.toml' argument. 

The following example shows the builtin config:

Example Config:
```toml
[config]
    columns = [
        "First Discovered",                 # Add any additional columns that you would like to fix here.
    ]
    
    in_format =  "%b %d, %Y %H:%M:%S %Z"    # This is the format of the existing date time
    out_format = "%d-%b-%y"                 # This is the format that we would like to change it to
```


>[!TIP]
> Get more format codes here:
    [Python datetime formatting](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
