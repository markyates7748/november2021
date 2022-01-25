resource "aws_vpc" "my_vpc" {
  cidr_block = var.vpc_cidr_block
  tags = {
    Name = "SmoothStackTeraform"
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id     = aws_vpc.my_vpc.id
  depends_on = [aws_vpc.my_vpc]
}

resource "aws_security_group" "allow_ssh" {
  for_each    = var.security_groups
  name        = each.value["name"]
  description = each.value["description"]
  vpc_id      = aws_vpc.my_vpc.id

  ingress {
    from_port   = each.value["from_port"]
    to_port     = each.value["to_port"]
    protocol    = each.value["protocol"]
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_ssh"
  }
  depends_on = [aws_vpc.my_vpc]
}

resource "aws_route_table" "my_route_table" {
  vpc_id = aws_vpc.my_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
  tags = {
    Name = "SmoothStackTFRouteTable"
  }
}

resource "aws_subnet" "my_subnets" {
  for_each   = var.subnets
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = each.value["cidr_block"]
  tags = {
    Name = each.value["tag_name"] == "" ? "default_value" : each.value["tag_name"]
  }
  depends_on = [aws_vpc.my_vpc]
}

