# Find Unused EIPs in AWS

This code allows us to find unused ip addresses in AWS and searches security groups for any reference of them. This allows us to save costs and keep it clean.

### Installation

This script requires python to run.

Step 1 - Setup venv (optional)
```sh
$ virtualenv .venv
$ source .venv/bin/activate  
```

Step 2 - Install Requirements

```sh
$ pip install -r requirements.txt
```

### Scenarios:

1. Search all regions for unused ip addresses, and for referecnces to all security groups in the same region:
```sh
AWS_PROFILE=<profile name> python unused_ip_addresses.py --region all
```

2. Search a specific region for all unused ip addresses, and for references to all security groups in that region:
```sh
AWS_PROFILE=<profile name> python unused_ip_addresses.py --region us-east-1
```

3. Search a specific region for a specified list of unused ip addresses, and for referecnces to all scurity groups in that region:
```sh
AWS_PROFILE=<profile name> python unused_ip_addresses.py --region us-east-1 --ip_addresses 10.1.1.1,10.2.2.2,10.3.3.3
```
