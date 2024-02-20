# Fix Date Time:
Simple script to let you change the datetime of an entire column in one or more excel spreadsheets. 

### Installation

##### Windows .exe
You can simply download the fix_datetime.exe from this repository's release page. 

##### Pip



### Using it




If you would like to create a custom config file, please create a 'config.toml' file in your home directory. Or simply add the '-c path/to/config.toml' argument. See the following example:

Example Config:
```toml
[config]
    columns = [
        "First Discovered",                 # Add any additional columns that you would like to fix here.
    ]
    
    in_format =  "%b %d, %Y %H:%M:%S %Z"    # This is the format of the existing date time
    out_format = "%d %b %y"                 # This is the format that we would like to change it to
```


>[!TIP]
> Get more format codes here:
    [Python datetime formatting](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
