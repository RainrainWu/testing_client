terraform {
  backend "s3" {
    encrypt = true
    bucket  = "udc-dev-terraform-cicd"
    region  = "us-east-2"
    key     = "terraform.udc-dev-cicd.python-template.tfstate"
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-2"
}
resource "aws_ecr_repository" "python-template_ecr-repo" {
  name = "udc/python-template"
}

