resource "aws_instance" "auth_service" {
  ami           = var.ami_id
  instance_type = var.instance_type
  security_groups = [aws_security_group.ecommerce_sg.name]
  user_data = file("userdata/auth.sh")
  tags = {
    Name = "Auth-Service"
  }
}

resource "aws_instance" "product_service" {
  ami           = var.ami_id
  instance_type = var.instance_type
  security_groups = [aws_security_group.ecommerce_sg.name]
  user_data = file("userdata/product.sh")
  tags = {
    Name = "Product-Service"
  }
}

resource "aws_instance" "order_service" {
  ami           = var.ami_id
  instance_type = var.instance_type
  security_groups = [aws_security_group.ecommerce_sg.name]
  user_data = file("userdata/order.sh")
  tags = {
    Name = "Order-Service"
  }
}

resource "aws_instance" "inventory_service" {
  ami           = var.ami_id
  instance_type = var.instance_type
  security_groups = [aws_security_group.ecommerce_sg.name]
  user_data = file("userdata/inventory.sh")
  tags = {
    Name = "Inventory-Service"
  }
}

resource "aws_instance" "mongo_db" {
  ami           = var.ami_id
  instance_type = var.instance_type
  security_groups = [aws_security_group.ecommerce_sg.name]
  user_data = file("userdata/mongo.sh")
  tags = {
    Name = "MongoDB"
  }
}
