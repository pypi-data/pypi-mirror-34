<h1>zec2</h1>

<p>Easily ssh to your AWS EC2 instances</p>

<h2>INSTALL</h2>

```bash
pip install zec2
```

<h2>USAGE</h2>

```bash
# list all EC2 instances
> zec2 ls

# ssh to 1st instance from the list
> $(zec2 ssh 1)

# ssh using different user (the default is ec2-user)
> $(zec2 ssh 1 -u ubuntu)

# ssh using different pem key path (the default is ~/.ssh/__instance_key_pair__.pem)
> $(zec2 ssh 1 -i ~/path/to/key.pem)
```

