variable "vpc_cidr_block" {
  type        = string
  description = "The CIDR block for the VPC."
}

variable "security_group_name" {
  type        = string
  description = "The name of the security group"
}

variable "subnet_cidr_block" {
  type        = string
  description = "The CIDR block for the Subnet."
}

variable "private_ip_network_interface" {
  type        = list(string)
  description = "The Private IP of the netowrk interface"
}

