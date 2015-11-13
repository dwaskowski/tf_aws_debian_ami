tf_aws_debian_ami
=================

Terraform module to get the current set of publicly available Debian AMIs.

List of AMIs was generated using AWS CLI.

For generate that list you'll need:

  * Python
  * AWS CLI (https://aws.amazon.com/cli/)


## Input variables

  * region - E.g. eu-west-1
  * distribution - squeeze/wheezy/jessie
  * architecture - x86_64/i386 (default: x86_64)
  * instance_type - E.g. t2.micro

## Outputs

  * ami_id

## Example use

    module "ami" {
      source = "github.com/dwaskowski/tf_aws_debian_ami"
      region = "eu-west-1"
      distribution = "wheezy"
      architecture = "x86_64"
      instance_type = "t2.micro"
    }

    resource "aws_instance" "web" {
      ami = "${module.ami.ami_id}"
      instance_type = "t2.micro"
    }

## License

Apache2 - see the included LICENSE file for more details.

