###############################################
# Module Debian AMI
###############################################

module "virttype" {
    source = "github.com/terraform-community-modules/tf_aws_virttype"
    instance_type = "${var.instance_type}"
}
