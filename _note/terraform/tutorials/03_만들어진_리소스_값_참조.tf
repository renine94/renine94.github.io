resource "aws_eip" "myeip" {

}

resource "aws_security_group" "my-simple-group" {
  name        = ""
  description = ""
  vpc_id      = "aws"

  ingress = {
    cidr = aws_eip.myeip.public_ip
  }
}

