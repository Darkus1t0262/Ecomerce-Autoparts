variable "ami_id" {
  default = "ami-032ae1bccc5be78ca"  # ✅ Replace with your latest AMI
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  default = "ecomerce"  # ✅ Use your AWS key pair name
}
