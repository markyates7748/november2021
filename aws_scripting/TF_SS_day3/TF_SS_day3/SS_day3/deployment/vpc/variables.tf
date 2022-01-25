variable "vpc_cidr_block" {
  type        = string
  description = "The CIDR block for the VPC."
}

variable "security_group_name" {
  type        = string
  description = "The name of the security group"
}

variable "security_groups" {
  type = map(object({
    name        = string
    description = string
    from_port   = number
    to_port     = number
    protocol    = string
  }))
  description = "The security group"
}

variable "subnets" {
  type = map(object({
    cidr_block = string
    tag_name   = string
  }))
  description = "Subnets for the VPC"
}

# variable "testvariable" {
#   type = map(object({
#     name     = string
#     is_admin = string
#   }))
#   description = "check whether the user is admin"
# }

