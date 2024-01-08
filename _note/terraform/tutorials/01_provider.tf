provider "aws" {
  region = "ap-northeast-2"
}

resource "aws_vpc" "myVPC" {
  cidr_block = "10.0.0.0/24"
}

provider "kubernetes" {
  config_context_auth_info = "ops"
  config_context_cluster   = "myCluster"
}

resource "kubernetes_namespace" "my-first-namespace" {
  metadata {
    name = "my-first-namespace"
  }
}

# cli
# terraform init
# terraform apply
# terraform destroy

# variable "user_names" {
#   description = "Create IAM users with these names"
#   type        = list(string)
#   default     = ["aaa", "bbb", "ccc"]
# }

# resource "aws_iam_user" "example" {
#   count = length(var.user_names)
#   name = var.user_names[count.index]
# }
