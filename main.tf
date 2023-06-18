terraform {
  required_providers{
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">=1.1.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "app_server" {
  key_name = "iac-projetoClima"
  ami = "ami-03f65b8614a860c29"
  instance_type = "t2.micro"

  tags = {
    Name = "ProjetoClimaTempo"
  }
}

