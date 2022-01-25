
locals {
  network_interface_private_ips = [var.private_ip]
}

resource "aws_network_interface" "foo" {
  subnet_id       = data.aws_subnet.subnet.id
  private_ips     = local.network_interface_private_ips
  security_groups = [data.aws_security_group.sg.id]
  tags = {
    Name = "primary_network_interface"
  }
}


resource "aws_instance" "foo" {
  ami           = "ami-0747bdcabd34c712a" // value should be fed from deployment code
  instance_type = "t2.micro"              // value should be fed from deployment code
  key_name      = "terraform"             // value should be fed from deployment code
  network_interface {
    network_interface_id = aws_network_interface.foo.id
    device_index         = 0
  }
  tags = {
    Name = "TerraformSS"
  }
}


resource "aws_eip" "lb" {
  instance                  = aws_instance.foo.id
  associate_with_private_ip = var.private_ip
  vpc                       = true
}
