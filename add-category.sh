#!/bin/sh

# 명령어들의 트랜잭션을 보장함, (하나라도 실패하면 전체 롤백))
( set -e

echo ">>> Enter new categoryName : "

# sh 에서 사용자 input 받아 변수로 저장
read categoryName

# root password 를 sudo 커맨드 입력값으로 전달
echo jaegu | sudo -S chmod 777 $(pwd)/_posts
sleep 0.1
mkdir -p $(pwd)/_posts/$categoryName

echo jaegu | sudo -S chmod 777 $(pwd)/_pages
sleep 0.1
mkdir -p $(pwd)/_pages/categories

# sed -i 's/기존 내용/변경할 내용/g' 파일명.txt > 저장할_파일명
sed "s/aws/$categoryName/" $(pwd)/_pages/categories/category-aws.md > $(pwd)/_pages/categories/category-$categoryName.md

sleep 0.1
vi "$(pwd)/_pages/categories/category-${categoryName}.md"
vi $(pwd)/_data/navigation.yml

echo ">>> github 로 push 합니다."
sleep 0.2

git add _posts _pages _data
git commit -m "새로운 카테고리 추가 : ${categoryName}"
git push origin master
)

