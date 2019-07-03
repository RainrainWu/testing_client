terraform {
  provider "aws" {
    profile    = "default"
    region     = "us-east-2"
  }

  backend "s3" {
    encrypt = true
    bucket  = "udc-dev-cicd"
    region  = "us-east-2"
    key     = "terraform.udc-dev-cicd.tfstate"
  }

  resource "aws_ecr_repository" "ecr-repo" {
    name = "udc/python-template"
  }
}
