
resource "aws_instance" "notesapp" {
  ami             = "ami-0d1622042e957c247"  # Amazon Linux 2 AMI
  instance_type   = var.instance_type
  key_name        = var.key_name

  user_data = file("userdata.sh")

  tags = {
    Name = "notesapp-instance"
  }
}
