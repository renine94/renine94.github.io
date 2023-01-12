# ssh pem 키 등록
```shell
Host {{name}}
  HostName {{ec2-url}}
  User ec2-user
  IdentityFile ~/.ssh/{{my_key.pem}}

chmod 700 ~/.ssh/config
```

# EC2 HostName 등록하기
```shell
sudo vim /etc/sysconfig/network

HOSTNAME={{hostname}}
sudo reboot

sudo vim /etc/hosts
127.0.0.1 {{위에서 등록한 hostName}}

curl {{hostName}}
```
