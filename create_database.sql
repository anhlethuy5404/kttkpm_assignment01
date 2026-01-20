--
-- Table structure for table `domain_book`
--

DROP TABLE IF EXISTS `domain_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domain_book` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `domain_book_chk_1` CHECK ((`stock` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domain_book`
--

LOCK TABLES `domain_book` WRITE;
/*!40000 ALTER TABLE `domain_book` DISABLE KEYS */;
INSERT INTO `domain_book` VALUES (1,'The Great Gatsby','F. Scott Fitzgerald',15.99,50),(2,'To Kill a Mockingbird','Harper Lee',12.50,30),(3,'1984','George Orwell',10.99,100),(4,'The Catcher in the Rye','J.D. Salinger',14.25,45),(5,'The Hobbit','J.R.R. Tolkien',20.00,60),(6,'Pride and Prejudice','Jane Austen',9.99,80),(7,'The Da Vinci Code','Dan Brown',18.50,25),(8,'The Alchemist','Paulo Coelho',13.00,70),(9,'Harry Potter and the Sorcerers Stone','J.K. Rowling',25.99,120),(10,'The Little Prince','Antoine de Saint-Exupéry',8.50,150),(11,'Brave New World','Aldous Huxley',11.75,40),(12,'The Book Thief','Markus Zusak',16.20,35),(13,'Animal Farm','George Orwell',7.99,90),(14,'The Shining','Stephen King',19.99,20),(15,'Life of Pi','Yann Martel',14.50,55);
/*!40000 ALTER TABLE `domain_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `domain_customer`
--

DROP TABLE IF EXISTS `domain_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domain_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phoneNumber` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `domain_cart`
--

DROP TABLE IF EXISTS `domain_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domain_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domain_cart_customer_id_8461f080_fk_domain_customer_id` (`customer_id`),
  CONSTRAINT `domain_cart_customer_id_8461f080_fk_domain_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `domain_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `domain_cartitem`
--

DROP TABLE IF EXISTS `domain_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domain_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `book_id` bigint NOT NULL,
  `cart_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `domain_cartitem_book_id_d20ac288_fk_domain_book_id` (`book_id`),
  KEY `domain_cartitem_cart_id_b6450bb0_fk_domain_cart_id` (`cart_id`),
  CONSTRAINT `domain_cartitem_book_id_d20ac288_fk_domain_book_id` FOREIGN KEY (`book_id`) REFERENCES `domain_book` (`id`),
  CONSTRAINT `domain_cartitem_cart_id_b6450bb0_fk_domain_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `domain_cart` (`id`),
  CONSTRAINT `domain_cartitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


