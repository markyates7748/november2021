resource "aws_vpc" "my_vpc" {
  cidr_block = var.vpc_cidr_block
  tags = {
    Name = "SmoothStackTeraform"
  }
}

# data "aws_vpc" "my_vpc" {
#   id = "vpc-05b8984761a8a2424"
# }

# resource "aws_internet_gateway" "gw" {
#   vpc_id     = data.aws_vpc.my_vpc.id
#   depends_on = [data.aws_vpc.my_vpc]
# }

# resource "aws_security_group" "allow_ssh" {
#   name        = var.security_group_name
#   description = "Allow SSH inbound traffic"
#   vpc_id      = data.aws_vpc.my_vpc.id

#   ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
#   tags = {
#     Name = "allow_ssh"
#   }
#   depends_on = [data.aws_vpc.my_vpc]
# }


# resource "aws_route_table" "my_route_table" {
#   vpc_id = data.aws_vpc.my_vpc.id
#   route {
#     cidr_block = "0.0.0.0/0"
#     gateway_id = aws_internet_gateway.gw.id
#   }
#   tags = {
#     Name = "SmoothStackTFRouteTabl"
#   }
# }

# resource "aws_subnet" "my_subnet" {
#   vpc_id     = data.aws_vpc.my_vpc.id
#   cidr_block = var.subnet_cidr_block

#   tags = {
#     Name = "tf-example"
#   }
#   depends_on = [data.aws_vpc.my_vpc]
# }

# resource "aws_main_route_table_association" "vpc_association" {
#   vpc_id         = data.aws_vpc.my_vpc.id
#   route_table_id = aws_route_table.my_route_table.id
# }

# resource "aws_network_interface" "foo" {
#   subnet_id       = aws_subnet.my_subnet.id
#   private_ips     = var.private_ip_network_interface
#   security_groups = [aws_security_group.allow_ssh.id]
#   tags = {
#     Name = "primary_network_interface"
#   }
# }

# resource "aws_instance" "foo" {
#   ami           = "ami-0747bdcabd34c712a"
#   instance_type = "t2.micro"
#   key_name      = "terraform"
#   network_interface {
#     network_interface_id = aws_network_interface.foo.id
#     device_index         = 0
#   }
#   tags = {
#     Name = "TerraformSS"
#   }
# }

# resource "aws_eip" "lb" {
#   instance                  = aws_instance.foo.id
#   associate_with_private_ip = join(",", var.private_ip_network_interface)
#   vpc                       = true
# }