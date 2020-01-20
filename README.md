# Install Python 3 
brew install python3

# Post installation on python 3 to get pip 3
brew postinstall python3

# Install all the requirement packages by 
pip3 install -r requirements.txt

# Run the tests by 
```
pytest
```

# Environment variable
```BROWSER=chrome pytest```

# Parallel run
```BROWSER=chrome pytest -s -v -n=2```

# snapshot run
```snap=1 pytest```

# 

