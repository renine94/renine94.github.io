# 테라폼 초기화
terraform init
terraform refresh

# 현재 상태를 보여줌
terraform plan
terraform plan -refresh=false (이미 만들어진 애들 정보는 안보이고 업데이트 된애만)
terraform plan -target={filename} (특정 파일의 변경사항만 보고 싶음)

terraform apply
terraform destroy

# 유용한 CLI
- 테라폼파일들의 포멧형식을 통일시킴 (python black 과 비슷)
terraform fmt

- 테라폼 파일의 유효성검사 (허용되지 않는 파라미터 등 체크 가능, plan 하면 자동으로 체크함)
terraform validate 

# 이미 있는 자원이 손상되어 재생성
terraform taint
terraform apply -replace="aws_instance.myec2" (테라폼 최신버전 v0.15.2 이상)

# 출력값 보기
terraform output {outputName}
