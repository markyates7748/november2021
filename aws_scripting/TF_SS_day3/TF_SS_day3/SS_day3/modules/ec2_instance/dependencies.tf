data "aws_subnet" "subnet" {
  tags = {
    Name = var.subnet_name
  }
}

data "aws_security_group" "sg" {
  tags = {
    Name = var.security_group_name
  }
}
