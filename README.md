# ionos_ipupdater

A lightweight docker container to periodically check public IP and update IONOS DNS record if changed.


# Run

```
> sudo docker-compose up -d
```

# Example

```
> sudo docker-compose up
Recreating ipupdater ... done
Attaching to ipupdater
ipupdater    | crond: crond (busybox 1.31.1) started, log level 8
ipupdater    | crond: USER root pid   7 cmd python3 /etc/ipupdater.py 2>&1
ipupdater    | Public IP :XXX.XXX.XXX.XXX
ipupdater    | https://login.ionos.co.uk/?redirect_url=https%3A%2F%2Fmy.ionos.co.uk%2FLogin
ipupdater    | https://my.ionos.co.uk:443/domains-dashboard
ipupdater    | https://my.ionos.co.uk:443/domain-details/DOMAIN
ipupdater    | https://my.ionos.co.uk:443/domain-dns-settings/DOMAIN?linkId=ct.txt.domainlist.dns-settings.pro&from=domain-details%2FDOMAIN
ipupdater    | https://my.ionos.co.uk:443/edit-dns-record/DOMAIN/YYYYYYYYYY?linkId=ct.link.dns.editrecord
ipupdater    | IP update complete.
ipupdater    | crond: USER root pid   8 cmd python3 /etc/ipupdater.py 2>&1
ipupdater    | Public IP (unchanged):XXX.XXX.XXX.XXX
ipupdater    | crond: USER root pid   9 cmd python3 /etc/ipupdater.py 2>&1
ipupdater    | Public IP (unchanged):XXX.XXX.XXX.XXX
ipupdater    | crond: USER root pid  10 cmd python3 /etc/ipupdater.py 2>&1
ipupdater    | Public IP (unchanged):XXX.XXX.XXX.XXX
```
