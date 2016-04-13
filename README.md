# The Eye

Take shots from webcam using OpenCV

# Using

Create `~/camshots`:

```
mkdir ~/camshots
```

Add a rule to *crontab*:

```
crontab -e
0 * * * * python /path/to/the-eye/src/main.py
```

List *crontab* to check if it's running:

```
crontab -l
```

Check hourly shots at `~/camshots`.
