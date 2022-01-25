# locals {
#   admin_user = {
#     for name, user in var.testvariable : name => user
#     if user.is_admin
#   }
# }

# output "admin" {
#   value = local.admin_user
# }

module "networking" {
  source              = "../../modules/networking"
  vpc_cidr_block      = var.vpc_cidr_block
  security_group_name = var.security_group_name
  security_groups     = var.security_groups
  subnets             = var.subnets
}
