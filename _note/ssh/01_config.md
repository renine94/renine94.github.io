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

---

- 로컬컴퓨터 -> 원격서버 접속하기
  - `id_rsa.pub` 은 나의 공개 키
  - `authorized_keys` 파일은 다른 컴퓨터에서 생성한 공개 키들을 넣어두는 공간
    - 여기에 있는 공개키들만큼 원격서버들로부터 내 서버에 접속할 수 있게됨


따라서, 원격 서버에 접근하기 위해서는 로컬에서 생성된 id_rsa.pub 파일의 내용을 원격 서버의 authorized_keys 파일에 추가하는 것만으로 충분합니다.
