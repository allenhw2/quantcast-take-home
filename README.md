# Most Active Cookie CLI

## Setup

Linux/MacOS
```
python3 -m venv env
source env/bin/activate
env/bin/pip3 install -e .
env/bin/most_active_cookie -h 
env/bin/most_active_cookie "test_input.csv" -d 2018-12-09
env/bin/most_active_cookie "test_input.csv" -d 2018-12-08
```

Windows (Powershell)
```
python -m venv env
env/Scripts/Activate.ps1
env/Scripts/pip3 install -e .
env/Scripts/most_active_cookie -h 
env/Scripts/most_active_cookie "test_input.csv" -d 2018-12-09
env/Scripts/most_active_cookie "test_input.csv" -d 2018-12-08
```

Windows (cmd)
```
python -m venv env
env/Scripts/activate.bat
env/Scripts/pip3 install -e .
env/Scripts/most_active_cookie -h 
env/Scripts/most_active_cookie "test_input.csv" -d 2018-12-09
env/Scripts/most_active_cookie "test_input.csv" -d 2018-12-08
```

## Testing

Linux/MacOS
```
python3 -m unittest discover .
```

Windows
```
python -m unittest discover .
```


