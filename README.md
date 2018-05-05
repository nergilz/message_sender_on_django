## Message sender on django

---

### The programm log_in users and send the messages

+ the message send to the specified address after registration
+ after sending a marker appears in the admin panel
+ reallized opportunity "Sign_out"


### Make the following changes to the file:

```bash
fogstreamtest/settings.py
```

### Configure the host to send messages:

```python
EMAIL_USE_TLS = True
EMAIL_HOST = ""
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
```

### Requirements
```bash
python 3.5 (or higher)

django 1.8 (or higher)
``` 

---

### this code is written as a test job


