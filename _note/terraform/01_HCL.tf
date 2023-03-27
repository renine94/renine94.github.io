# HCL (하시코프 랭귀지)
# cli
# terraform init
# terraform apply
# terraform destroy


variable "user_names" {
  description = "Create IAM users with these names"
  type        = list(string)
  default     = ["aaa", "bbb", "ccc"]
}

resource "aws_iam_user" "example" {
  count = length(var.user_names)
  name = var.user_names[count.index]
}
