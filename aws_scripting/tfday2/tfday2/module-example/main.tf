
module "networking" {
    source = "./module-networking"
    vpc_cidr_block = var.vpc_cidr_block
    security_group_name = var.security_group_name
    subnet_cidr_block = var.subnet_cidr_block
    private_ip_network_interface = var.private_ip_network_interface
}