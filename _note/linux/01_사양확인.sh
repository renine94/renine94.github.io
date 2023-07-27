# https://andante-sloth.tistory.com/92

# cpu 코어 확인
cat /proc/cpuinfo | egrep 'siblings|cpu cores' | head -2

# memory 확인
free -h

# 그래픽카드 확인
lspci | grep VGA

# Disk 확인
lsblk -d -o name,rota
sudo fdisk -l
