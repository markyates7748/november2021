
module "ec2" {
  source              = "../../modules/ec2_instance"
  subnet_name         = var.subnet_name
  security_group_name = var.security_group_name
  private_ip          = var.private_ip
}
