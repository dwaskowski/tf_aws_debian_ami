###############################################
# Module Debian AMI
###############################################

output "ami_id" {
    value = "${lookup(var.amis, format(\"%s-%s-%s-%s\", var.region, var.architecture, module.virttype.prefer_hvm, var.distribution))}"
}
