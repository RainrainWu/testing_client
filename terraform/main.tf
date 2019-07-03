terraform {
  backend "s3" {
    encrypt = true
    bucket  = "udc-dev-terraform-cicd"
    region  = "us-east-2"
    key     = "terraform.udc-dev-cicd.tfstate"
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-2"
} 
resource "aws_ecr_repository" "ecr-repo" {
  name = "udc/python-template"
}

