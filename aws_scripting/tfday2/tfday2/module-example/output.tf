output "tf_vpc" {
    value = module.networking.aws_vpc
}

output "tf_security_group" {
    value = module.networking.aws_security_group
}