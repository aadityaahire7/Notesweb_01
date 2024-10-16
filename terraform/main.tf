
resource "aws_instance" "notesapp" {
  ami             = "ami-00f251754ac5da7f0"  # Amazon Linux 2 AMI
  instance_type   = var.instance_type
  key_name        = var.key_name

  user_data = file("userdata.sh")

  tags = {
    Name = "notesapp-instance"
  }
}
