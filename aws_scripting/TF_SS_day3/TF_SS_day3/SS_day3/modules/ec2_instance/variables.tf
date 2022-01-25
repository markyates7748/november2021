variable "subnet_name" {
  type        = string
  description = "subnet that will host the EC2"
}
variable "security_group_name" {
  type        = string
  description = "security group for the subnet"
}

variable "private_ip" {
  type        = string
  description = "private ip for EC2"
}
