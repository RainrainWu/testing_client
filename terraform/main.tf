provider "aws" {
  profile    = "default"
  region     = "us-east-2"
}

resource "aws_ecr_repository" "ecr-repo" {
  name = "udc/python-template"
}

