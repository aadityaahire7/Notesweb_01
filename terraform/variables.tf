variable "instance_type" {
  default = "t2.medium"  # Instance type
}

variable "docker_image" {
  default = "21070122001/notesapp:latest"  # Docker image
}

variable "key_name" {
  description = "Key name for SSH access"
  default     = "terraform_notes"  # You can specify your key pair name here
}

variable "region" {
  default = "ap-south-1"  # Mumbai region
}
