<h1>zec2</h1>

[![PyPI version](https://badge.fury.io/py/zec2.svg)](https://badge.fury.io/py/zec2)

<p>Easily ssh to your AWS EC2 instances</p>

<h2>INSTALL</h2>

```bash
pip install zec2
```

<h2>USAGE</h2>

```bash
# list all EC2 instances
> zec2 ls

# list all EC2 instances using custom aws profile (applies to all commands)
> zec2 -p work ls

# live list all EC2 instances
> zec2 ls -f

# ssh to 1st instance from the list
> $(zec2 ssh 1)

# ssh using different user (the default is ec2-user)
> $(zec2 ssh 1 -u ubuntu)

# ssh using different pem key path (the default is ~/.ssh/__instance_key_pair__.pem)
> $(zec2 ssh 1 -i ~/path/to/key.pem)

# stop 1st EC2 instance from the list
> zec2 stop 1

# start 1st EC2 instance from the list
> zec2 start 1

# restart 1st EC2 instance from the list
> zec2 restart 1

# terminate 1st EC2 instance from the list
> zec2 terminate 1
```

