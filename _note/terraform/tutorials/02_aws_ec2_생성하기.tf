provider "aws" {
  region     = "ap-northeast-2"
  access_key = ""
  secret_key = ""
}

resource "aws_instance" "my-ec2" {
  ami           = "something"
  instance_type = var.my-variable1
}