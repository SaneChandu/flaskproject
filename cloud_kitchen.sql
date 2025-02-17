-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: cloud
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adddish`
--

DROP TABLE IF EXISTS `adddish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adddish` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `menu` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adddish`
--

LOCK TABLES `adddish` WRITE;
/*!40000 ALTER TABLE `adddish` DISABLE KEYS */;
INSERT INTO `adddish` VALUES (6,'Chicken Dum Biriyani','Chicken Dum Biryani is a fragrant, spiced rice dish with tender chicken, cooked together in a sealed pot for rich flavors.','Maincourse',300.00,'E6nC9rP2q.jpg','2024-12-23 08:24:26','Non-Veg'),(7,'Mutton Biriyani','Mutton Biryani is a rich and spicy rice dish with succulent mutton pieces, infused with aromatic herbs and spices.','Maincourse',380.00,'Q2yT7rG9i.jpg','2024-12-23 08:24:56','Non-Veg'),(8,'Tandoori Chicken','Tandoori Chicken is a flavorful, tender chicken marinated in a blend of yogurt and spices, then grilled to a smoky finish.','Starters',300.00,'I2bP3fH6y.jpg','2024-12-23 08:33:17','Non-Veg'),(9,'Butter Naan','Butter Naan is a soft, fluffy Indian flatbread topped with melted butter.','Breads',15.00,'N1eK8qJ3e.jpg','2024-12-23 08:34:26',NULL),(10,'Grill Chicken','Grill Chicken is a tender, smoky chicken dish, marinated in flavorful spices and grilled to a perfect crisp','Starters',300.00,'O9xC2yP1b.jpg','2024-12-23 08:35:30','Non-Veg'),(11,'CupCakes','A cupcake is a small, sweet, individually-sized cake, typically topped with frosting and decorations.','Desserts',79.00,'X4uK4lS4d.jpg','2024-12-24 10:02:43',NULL),(12,'Donut','A donut is a sweet, fried or baked pastry, typically ring-shaped.','Desserts',49.00,'Q7mI3sG1t.jpg','2024-12-24 10:04:54',NULL),(13,'Roti','A simple, round Indian flatbread made from whole wheat flour.','Breads',25.00,'F0bI9xJ0w.jpg','2024-12-25 14:33:31',NULL),(14,'Garlic Naan','Naan bread topped with a garlic butter spread.','Breads',30.00,'I4tL4yJ2j.jpg','2024-12-25 14:38:45',NULL),(15,'Gulab Jamun','Soft, round milk-based dumplings soaked in sweet, fragrant sugar syrup.','Desserts',15.00,'U0dI1wB9w.jpg','2024-12-25 14:48:23',NULL),(16,'Gajar Ka Halwa','A rich, sweet dessert made from grated carrots, milk, sugar, and ghee, garnished with nuts.(250gms)','Desserts',200.00,'M3tT8mA9f.jpg','2024-12-25 16:38:36',NULL),(19,'Paneer Tikka','Grilled paneer cubes marinated with aromatic spices and yogurt.','Starters',190.00,'U6sH3vV6y.jpg','2024-12-25 17:05:43','Veg'),(20,'Gobi Manchurian','Crispy cauliflower in a spicy, tangy sauce.','Starters',110.00,'D4qA6xG3o.jpg','2024-12-25 17:06:06','Veg'),(21,'Egg Fried Rice','Stir-fried rice with scrambled eggs and mixed vegetables.','Maincourse',190.00,'B0mQ6fQ2o.jpg','2024-12-25 17:07:13','Non-Veg'),(22,'Chicken Fried Rice','Spicy chicken stir-fried with rice, vegetables, and savory seasonings.','Maincourse',250.00,'E8nX6bE9o.jpg','2024-12-25 17:08:16','Non-Veg'),(23,'Fish Fry','Crispy fried fish coated in flavorful spices and herbs.','Starters',220.00,'K0rS8fF5k.jpg','2024-12-25 17:09:45','Non-Veg'),(24,'Gobi Fried Rice','A flavorful rice dish made with crispy fried cauliflower, vegetables, and a hint of soy sauce.','Maincourse',170.00,'R5fF9qG0h.jpg','2024-12-25 17:11:56','Veg'),(25,'Mutton Curry','Mutton curry is a savory dish made with tender mutton in a spiced gravy.','Maincourse',310.00,'Q0wE4lV5e.jpg','2024-12-25 17:46:07','Non-Veg'),(26,'Chicken Lollipops','Chicken Lollipops are crispy, flavorful chicken wings shaped like lollipops, marinated in spices and fried to perfection.','Starters',200.00,'U1sM6gI6n.jpg','2024-12-25 17:47:38','Non-Veg'),(27,'Gongura Chicken Curry','Gongura Chicken is a tangy, spicy chicken curry made with Gongura leaves and spices.','Maincourse',230.00,'E6zJ7rZ6u.jpg','2024-12-25 17:50:12','Non-Veg'),(28,'Kaju Masala','Kaju Curry is a rich, creamy curry made with cashew nuts and flavorful spices.','Maincourse',210.00,'U8aC9yD2p.jpg','2024-12-25 17:53:38','Veg'),(29,'Butter Chicken','Butter Chicken is a creamy and mildly spiced chicken dish cooked in a rich tomato-based gravy.','Maincourse',240.00,'O4sQ3sV1l.jpg','2024-12-25 17:55:56','Non-Veg'),(30,'Prawns Biriyani','Prawns Biryani is a flavorful rice dish made with succulent prawns, aromatic spices, and fragrant basmati rice.','Maincourse',400.00,'Z6iD7wN5l.jpg','2024-12-25 17:59:19','Non-Veg'),(31,'Prawns Fry','Prawns Fry is a crispy and flavorful dish made with marinated prawns, fried to golden perfection.','Starters',459.00,'W2rS5wD6q.jpg','2024-12-25 18:00:39','Non-Veg');
/*!40000 ALTER TABLE `adddish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'chandana','sanechandana24@gmail.com','chandu');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(100) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `comment` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int DEFAULT NULL,
  `dish_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders_summary` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_items`
--

LOCK TABLES `order_items` WRITE;
/*!40000 ALTER TABLE `order_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `dish_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `order_status` enum('Pending','Completed','Cancelled','Failed') DEFAULT 'Pending',
  `order_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `address` varchar(255) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `razorpay_order_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  KEY `dish_id` (`dish_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `user` (`id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`dish_id`) REFERENCES `adddish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (16,7,25,1,310.00,'Completed','2025-01-08 15:01:08','hyd','Online',NULL),(18,6,10,1,300.00,'Completed','2025-01-10 10:05:00','atp','COD',NULL),(19,6,20,1,110.00,'Pending','2025-01-10 10:05:00','atp','COD',NULL),(20,6,11,1,79.00,'Pending','2025-01-12 06:26:14','hyd','COD',NULL),(21,6,7,1,380.00,'Pending','2025-01-12 06:54:48','hyd','Online',NULL);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_summary`
--

DROP TABLE IF EXISTS `orders_summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_summary` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `order_status` enum('Pending','Completed','Cancelled','Failed') DEFAULT 'Pending',
  `order_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `address` varchar(255) DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `razorpay_order_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_summary`
--

LOCK TABLES `orders_summary` WRITE;
/*!40000 ALTER TABLE `orders_summary` DISABLE KEYS */;
INSERT INTO `orders_summary` VALUES (10,7,310.00,'Pending','2025-01-08 15:01:08','hyd','Online',NULL),(11,6,190.00,'Pending','2025-01-09 08:26:01','hyd','Online',NULL),(12,6,410.00,'Pending','2025-01-10 10:05:00','atp','COD',NULL),(13,6,79.00,'Pending','2025-01-12 06:26:14','hyd','COD',NULL),(14,6,380.00,'Pending','2025-01-12 06:54:48','hyd','Online',NULL);
/*!40000 ALTER TABLE `orders_summary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(200) NOT NULL,
  `gender` enum('Male','Female','Other') DEFAULT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'chandana','sanechandana24@gmail.com','123',NULL,NULL),(2,'chandana','chandanasane77@gmail.com','chandana',NULL,NULL),(6,'niharika','saneniharika72@gmail.com','123456','Female','2003-05-24'),(7,'vandana','vandana@gmail.com','vandu',NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-13 14:49:49
