vpc_cidr_block  = "172.17.0.0/16"
security_group_name = "allow_ssh"
security_groups = {
    sg1={
        name = "SSH security group1"
        description = "ssh1"
        from_port = 22
        to_port = 22
        protocol = "tcp"
    },
    sg2 = {
        name = "ssl"
        description = "ssh2"
        from_port = 443
        to_port = 443
        protocol = "tcp"
    }
}

subnets = {
    subnet1 = {
        cidr_block = "172.17.10.0/24",
        tag_name = "sub1"
    },
    subnet2 = {
        cidr_block = "172.17.11.0/24",
        tag_name = "sub2"
    }
}

//Just a simple demonstration FOR loop
# testvariable = {
#     test1 = {
#         name = "joby"
#         is_admin = true
#     },
#     test2 = {
#         name = "santhosh"
#         is_admin = true
#     }
# }