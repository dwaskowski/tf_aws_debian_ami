###############################################
# Module Debian AMI
###############################################

variable "region" {}
variable "distribution" {}
variable "instance_type" {}

variable "architecture" {
    default = "x86_64"
}
