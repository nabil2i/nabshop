-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: nabshop
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add author',6,'add_author'),(22,'Can change author',6,'change_author'),(23,'Can delete author',6,'delete_author'),(24,'Can view author',6,'view_author'),(25,'Can add book',7,'add_book'),(26,'Can change book',7,'change_book'),(27,'Can delete book',7,'delete_book'),(28,'Can view book',7,'view_book'),(29,'Can add book edition',8,'add_bookedition'),(30,'Can change book edition',8,'change_bookedition'),(31,'Can delete book edition',8,'delete_bookedition'),(32,'Can view book edition',8,'view_bookedition'),(33,'Can add cart',9,'add_cart'),(34,'Can change cart',9,'change_cart'),(35,'Can delete cart',9,'delete_cart'),(36,'Can view cart',9,'view_cart'),(37,'Can add customer',10,'add_customer'),(38,'Can change customer',10,'change_customer'),(39,'Can delete customer',10,'delete_customer'),(40,'Can view customer',10,'view_customer'),(41,'Can view history',10,'view_history'),(42,'Can add discount',11,'add_discount'),(43,'Can change discount',11,'change_discount'),(44,'Can delete discount',11,'delete_discount'),(45,'Can view discount',11,'view_discount'),(46,'Can add order',12,'add_order'),(47,'Can change order',12,'change_order'),(48,'Can delete order',12,'delete_order'),(49,'Can view order',12,'view_order'),(50,'Can cancel an order',12,'cancel_order'),(51,'Can add publisher',13,'add_publisher'),(52,'Can change publisher',13,'change_publisher'),(53,'Can delete publisher',13,'delete_publisher'),(54,'Can view publisher',13,'view_publisher'),(55,'Can add review',14,'add_review'),(56,'Can change review',14,'change_review'),(57,'Can delete review',14,'delete_review'),(58,'Can view review',14,'view_review'),(59,'Can add order item',15,'add_orderitem'),(60,'Can change order item',15,'change_orderitem'),(61,'Can delete order item',15,'delete_orderitem'),(62,'Can view order item',15,'view_orderitem'),(63,'Can add genre',16,'add_genre'),(64,'Can change genre',16,'change_genre'),(65,'Can delete genre',16,'delete_genre'),(66,'Can view genre',16,'view_genre'),(67,'Can add book image',17,'add_bookimage'),(68,'Can change book image',17,'change_bookimage'),(69,'Can delete book image',17,'delete_bookimage'),(70,'Can view book image',17,'view_bookimage'),(71,'Can add address',18,'add_address'),(72,'Can change address',18,'change_address'),(73,'Can delete address',18,'delete_address'),(74,'Can view address',18,'view_address'),(75,'Can add cart item',19,'add_cartitem'),(76,'Can change cart item',19,'change_cartitem'),(77,'Can delete cart item',19,'delete_cartitem'),(78,'Can view cart item',19,'view_cartitem'),(79,'Can add user',20,'add_user'),(80,'Can change user',20,'change_user'),(81,'Can delete user',20,'delete_user'),(82,'Can view user',20,'view_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user`
--

DROP TABLE IF EXISTS `core_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user`
--

LOCK TABLES `core_user` WRITE;
/*!40000 ALTER TABLE `core_user` DISABLE KEYS */;
INSERT INTO `core_user` VALUES (1,'pbkdf2_sha256$390000$y98BcIi3KJXjpLgrEbuvlM$Cb77tVoEutGZ6/vJDSCS2fwuDdwGvxTJ1pOCpFgr95g=','2023-03-22 00:41:33.786368',1,'admin','','',1,1,'2023-03-22 00:41:12.210453','admin@gmail.com');
/*!40000 ALTER TABLE `core_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_groups`
--

DROP TABLE IF EXISTS `core_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_groups`
--

LOCK TABLES `core_user_groups` WRITE;
/*!40000 ALTER TABLE `core_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_user_permissions`
--

DROP TABLE IF EXISTS `core_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`),
  CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_user_permissions`
--

LOCK TABLES `core_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `core_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_core_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-03-22 00:42:03.921250','1','Nabil Affo',1,'[{\"added\": {}}]',6,1),(2,'2023-03-22 00:42:14.036378','2','Nabil Alshaaeir',1,'[{\"added\": {}}]',6,1),(3,'2023-03-22 00:42:30.655415','1','Poetry',1,'[{\"added\": {}}]',16,1),(4,'2023-03-22 00:42:42.164728','2','Prose',1,'[{\"added\": {}}]',16,1),(5,'2023-03-22 00:42:53.421033','1','Self Published',1,'[{\"added\": {}}]',13,1),(6,'2023-03-22 00:43:55.652995','1','Chants de lettres',1,'[{\"added\": {}}, {\"added\": {\"name\": \"book image\", \"object\": \"BookImage object (1)\"}}]',7,1),(7,'2023-03-22 00:44:58.218492','2','Le voyage',1,'[{\"added\": {}}, {\"added\": {\"name\": \"book image\", \"object\": \"BookImage object (2)\"}}]',7,1),(8,'2023-03-22 00:46:08.369955','3','Serenata: Sur le chemin de l\'Orient',1,'[{\"added\": {}}, {\"added\": {\"name\": \"book image\", \"object\": \"BookImage object (3)\"}}]',7,1),(9,'2023-03-22 00:47:12.155823','4','Eastern Storms',1,'[{\"added\": {}}, {\"added\": {\"name\": \"book image\", \"object\": \"BookImage object (4)\"}}]',7,1),(10,'2023-03-22 00:47:24.899396','2','Le voyage',2,'[{\"changed\": {\"fields\": [\"Genre\"]}}]',7,1),(11,'2023-03-22 00:49:11.853519','1','Chants de lettres-Ebook',1,'[{\"added\": {}}]',8,1),(12,'2023-03-22 00:50:26.909833','2','Chants de lettres-Paperback',1,'[{\"added\": {}}]',8,1),(13,'2023-03-22 00:51:37.968256','3','Le voyage-Ebook',1,'[{\"added\": {}}]',8,1),(14,'2023-03-22 00:52:42.186074','4','Le voyage-Paperback',1,'[{\"added\": {}}]',8,1),(15,'2023-03-22 00:53:39.063955','5','Eastern Storms-Ebook',1,'[{\"added\": {}}]',8,1),(16,'2023-03-22 00:54:41.402762','6','Eastern Storms-Paperback',1,'[{\"added\": {}}]',8,1),(17,'2023-03-22 00:55:47.475780','7','Serenata: Sur le chemin de l\'Orient-Ebook',1,'[{\"added\": {}}]',8,1),(18,'2023-03-22 00:57:21.277028','8','Serenata: Sur le chemin de l\'Orient-Paperback',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(20,'core','user'),(5,'sessions','session'),(18,'store','address'),(6,'store','author'),(7,'store','book'),(8,'store','bookedition'),(17,'store','bookimage'),(9,'store','cart'),(19,'store','cartitem'),(10,'store','customer'),(11,'store','discount'),(16,'store','genre'),(12,'store','order'),(15,'store','orderitem'),(13,'store','publisher'),(14,'store','review');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-03-22 00:40:37.517641'),(2,'contenttypes','0002_remove_content_type_name','2023-03-22 00:40:37.546451'),(3,'auth','0001_initial','2023-03-22 00:40:37.669650'),(4,'auth','0002_alter_permission_name_max_length','2023-03-22 00:40:37.698208'),(5,'auth','0003_alter_user_email_max_length','2023-03-22 00:40:37.704654'),(6,'auth','0004_alter_user_username_opts','2023-03-22 00:40:37.710039'),(7,'auth','0005_alter_user_last_login_null','2023-03-22 00:40:37.716764'),(8,'auth','0006_require_contenttypes_0002','2023-03-22 00:40:37.719633'),(9,'auth','0007_alter_validators_add_error_messages','2023-03-22 00:40:37.725628'),(10,'auth','0008_alter_user_username_max_length','2023-03-22 00:40:37.731629'),(11,'auth','0009_alter_user_last_name_max_length','2023-03-22 00:40:37.739392'),(12,'auth','0010_alter_group_name_max_length','2023-03-22 00:40:37.749966'),(13,'auth','0011_update_proxy_permissions','2023-03-22 00:40:37.755747'),(14,'auth','0012_alter_user_first_name_max_length','2023-03-22 00:40:37.761584'),(15,'core','0001_initial','2023-03-22 00:40:37.903047'),(16,'admin','0001_initial','2023-03-22 00:40:37.968731'),(17,'admin','0002_logentry_remove_auto_add','2023-03-22 00:40:37.974802'),(18,'admin','0003_logentry_add_action_flag_choices','2023-03-22 00:40:37.980049'),(19,'sessions','0001_initial','2023-03-22 00:40:38.003766'),(20,'store','0001_initial','2023-03-22 00:40:38.638296');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1p86slxy1orby8s0kv9bthcixr2q8m7n','.eJxVjDsOwjAQBe_iGll21r9Q0nMGa-1d4wBypDipEHeHSCmgfTPzXiLitta4dV7iROIstDj9bgnzg9sO6I7tNss8t3WZktwVedAurzPx83K4fwcVe_3WoRAhWGSPORE6rVUxECA70pCUyQO6xIU9O2NHEyCBYrYKBx61tyzeHw0BOIM:1pemXl:L7m-Je-7HXBa0Vnjxt6uwIRVU-27KX07HV7nAJw_yoo','2023-04-05 00:41:33.788943');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_address`
--

DROP TABLE IF EXISTS `store_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `zipcode` smallint NOT NULL,
  `street` varchar(255) NOT NULL,
  `building` varchar(255) NOT NULL,
  `shippingstatus` varchar(1) NOT NULL,
  `billingstatus` varchar(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_address_customer_id_080cf871_fk_store_customer_id` (`customer_id`),
  CONSTRAINT `store_address_customer_id_080cf871_fk_store_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_address`
--

LOCK TABLES `store_address` WRITE;
/*!40000 ALTER TABLE `store_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_author`
--

DROP TABLE IF EXISTS `store_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_author` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_author`
--

LOCK TABLES `store_author` WRITE;
/*!40000 ALTER TABLE `store_author` DISABLE KEYS */;
INSERT INTO `store_author` VALUES (1,'Nabil','Affo',NULL,NULL),(2,'Nabil','Alshaaeir',NULL,NULL);
/*!40000 ALTER TABLE `store_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_book`
--

DROP TABLE IF EXISTS `store_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_book` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `author_id` bigint NOT NULL,
  `genre_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_book_genre_id_b0358a30_fk_store_genre_id` (`genre_id`),
  KEY `store_book_author_id_b581e597_fk_store_author_id` (`author_id`),
  KEY `store_book_slug_e5087f7b` (`slug`),
  CONSTRAINT `store_book_author_id_b581e597_fk_store_author_id` FOREIGN KEY (`author_id`) REFERENCES `store_author` (`id`),
  CONSTRAINT `store_book_genre_id_b0358a30_fk_store_genre_id` FOREIGN KEY (`genre_id`) REFERENCES `store_genre` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_book`
--

LOCK TABLES `store_book` WRITE;
/*!40000 ALTER TABLE `store_book` DISABLE KEYS */;
INSERT INTO `store_book` VALUES (1,'Chants de lettres','chants-de-lettres','Dans son deuxième recueil de poèmes, Chants de lettres, Nabil Affo nourrit la ferme et intime conviction que le bonheur attend chacun de nous quels que soient les obstacles qui se dressent sur notre chemin. Ses Chants de lettres racontent l’histoire d’un cœur détruit par l’amour, la séparation, la mort, l’injustice… mais qui est absolument résolu à renaître de ses cendres et à sortir de ce gouffre sinistre qui l’a vu sommeiller, pour en fin de compte s’élever et être heureux. C’est un chant d’espoir qui appelle, par sa musicalité, sa sensibilité et sa dextérité, à canaliser l’énergie de la souffrance pour en sortir une force indéfectible qui permettra d’avancer et de renouer avec tous les instants de la vie, quitte à s’évader et à parcourir tout l’univers pour y répandre la paix, l’amour et la joie.\r\n\r\n« A cette âme qui veut réaliser un rêve\r\nVivre un bonheur qui jamais ne s’achève\r\nIl est temps qu’elle s’élève »','2023-03-22 00:43:55.651284','2023-03-22 00:43:55.651304',1,1),(2,'Le voyage','le-voyage','Le voyage est un roman de Nabil Affo qui raconte les aventures d’un personnage qui est résolu à partir sur un coup de tête pour une destination qui lui est totalement inconnue, à tout quitter pour trouver les réponses aux questions profondes qui sommeillent en lui. Il rencontrera des êtres étranges mais aussi fascinants les uns que les autres. Parviendra-t-il à trouver ce qu’il cherche véritablement?','2023-03-22 00:44:58.215679','2023-03-22 00:47:24.898777',1,2),(3,'Serenata: Sur le chemin de l\'Orient','serenata','L\'amour ne s\'explique pas,\r\nil se ressent...\r\n\r\n“Serenata: Sur le chemin de l\'Orient\" est une collection de vers romantiques qui, par leur musicalité et leur cadence, font voguer sur des eaux sentimentales au gré du souffle des cœurs en quête d’amour. Ce recueil de poèmes est un chef-d’œuvre inouï qui se veut révélateur des ferveurs du cœur.\r\n\r\n“Je ne sais pas où je vais maintenant\r\nUne lueur dans tes yeux me retient\r\nMa tête baigne dans un océan\r\nMais mon souffle jamais ne s’éteint\"','2023-03-22 00:46:08.367365','2023-03-22 00:46:08.367385',1,1),(4,'Eastern Storms','eastern-storms','\"Eastern Storms\" is a collection of poetry that depicts a period spent in the far East marked by huge storms of life. The reader is driven between emotions of anxiety, loss, depression, quest for love, spirituality and more.','2023-03-22 00:47:12.154564','2023-03-22 00:47:12.154583',2,1);
/*!40000 ALTER TABLE `store_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_bookedition`
--

DROP TABLE IF EXISTS `store_bookedition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_bookedition` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `slug` varchar(50) NOT NULL,
  `booktype` varchar(10) NOT NULL,
  `isbn` varchar(255) NOT NULL,
  `unit_price` decimal(5,2) NOT NULL,
  `pages` int unsigned NOT NULL,
  `bookformat` varchar(255) NOT NULL,
  `publicationdate` date NOT NULL,
  `stock` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `book_id` bigint NOT NULL,
  `publisher_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_bookedition_publisher_id_d00d4d63_fk_store_publisher_id` (`publisher_id`),
  KEY `store_bookedition_book_id_f704ff9d_fk_store_book_id` (`book_id`),
  KEY `store_bookedition_slug_46428e8e` (`slug`),
  CONSTRAINT `store_bookedition_book_id_f704ff9d_fk_store_book_id` FOREIGN KEY (`book_id`) REFERENCES `store_book` (`id`),
  CONSTRAINT `store_bookedition_publisher_id_d00d4d63_fk_store_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `store_publisher` (`id`),
  CONSTRAINT `store_bookedition_chk_1` CHECK ((`pages` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_bookedition`
--

LOCK TABLES `store_bookedition` WRITE;
/*!40000 ALTER TABLE `store_bookedition` DISABLE KEYS */;
INSERT INTO `store_bookedition` VALUES (1,'chants-de-lettres-ebook','Ebook','1724275305',2.99,70,'Ebook','2018-08-15',1000000,'2023-03-22 00:49:11.851116','2023-03-22 00:49:11.851133',1,1),(2,'chants-de-lettres-paperback','Paperback','978-1724275301',7.80,108,'Paperback (5.24 x 0.26 x 7.99 inches)','2018-08-16',1000000,'2023-03-22 00:50:26.907818','2023-03-22 00:50:26.907843',1,1),(3,'le-voyage-ebook','Ebook','1724252496',2.99,66,'Ebook','2018-07-26',1000000,'2023-03-22 00:51:37.966035','2023-03-22 00:51:37.966052',2,1),(4,'le-voyage-paperback','Paperback','978-1724252494',7.80,126,'Paperback (5.25 x 0.3 x 8 inches)','2018-07-27',1000000,'2023-03-22 00:52:42.183382','2023-03-22 00:52:42.183407',2,1),(5,'eastern-storms','Ebook','1983298271',2.99,114,'Ebook','2022-02-14',1000000,'2023-03-22 00:53:39.061895','2023-03-22 00:53:39.061911',4,1),(6,'eastern-storms-paperback','Paperback','978-1983298271',10.50,112,'Paperback (5 x 0.26 x 8 inches)','2022-02-15',1000000,'2023-03-22 00:54:41.401467','2023-03-22 00:54:41.401481',4,1),(7,'sereneta-ebook','Ebook','1717887759',1.99,40,'Ebook','2019-05-17',1000000,'2023-03-22 00:55:47.471736','2023-03-22 00:55:47.471763',3,1),(8,'serenata-paperback','Paperback','978-1717887757',5.57,100,'Paperback (5 x 0.25 x 8 inches)','2019-05-18',1000000,'2023-03-22 00:57:21.275771','2023-03-22 00:57:21.275785',3,1);
/*!40000 ALTER TABLE `store_bookedition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_bookedition_discounts`
--

DROP TABLE IF EXISTS `store_bookedition_discounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_bookedition_discounts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bookedition_id` bigint NOT NULL,
  `discount_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `store_bookedition_discou_bookedition_id_discount__e024e8f6_uniq` (`bookedition_id`,`discount_id`),
  KEY `store_bookedition_di_discount_id_dc7720b4_fk_store_dis` (`discount_id`),
  CONSTRAINT `store_bookedition_di_bookedition_id_30d52807_fk_store_boo` FOREIGN KEY (`bookedition_id`) REFERENCES `store_bookedition` (`id`),
  CONSTRAINT `store_bookedition_di_discount_id_dc7720b4_fk_store_dis` FOREIGN KEY (`discount_id`) REFERENCES `store_discount` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_bookedition_discounts`
--

LOCK TABLES `store_bookedition_discounts` WRITE;
/*!40000 ALTER TABLE `store_bookedition_discounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_bookedition_discounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_bookimage`
--

DROP TABLE IF EXISTS `store_bookimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_bookimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `book_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_bookimage_book_id_c420bb13_fk_store_book_id` (`book_id`),
  CONSTRAINT `store_bookimage_book_id_c420bb13_fk_store_book_id` FOREIGN KEY (`book_id`) REFERENCES `store_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_bookimage`
--

LOCK TABLES `store_bookimage` WRITE;
/*!40000 ALTER TABLE `store_bookimage` DISABLE KEYS */;
INSERT INTO `store_bookimage` VALUES (1,'store/images/cdl.jpg','store/thumbnails/store/images/cdl.jpg','2023-03-22 00:58:42.246092',1),(2,'store/images/lv.jpg','store/thumbnails/store/images/lv.jpg','2023-03-22 00:47:15.216284',2),(3,'store/images/s.jpg','store/thumbnails/store/images/s.jpg','2023-03-22 00:58:42.904900',3),(4,'store/images/es.jpg','store/thumbnails/store/images/es.jpg','2023-03-22 00:58:42.279670',4);
/*!40000 ALTER TABLE `store_bookimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_cart`
--

DROP TABLE IF EXISTS `store_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_cart` (
  `id` char(32) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_cart`
--

LOCK TABLES `store_cart` WRITE;
/*!40000 ALTER TABLE `store_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_cartitem`
--

DROP TABLE IF EXISTS `store_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` smallint unsigned NOT NULL,
  `bookedition_id` bigint NOT NULL,
  `cart_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `store_cartitem_cart_id_bookedition_id_b849e1b3_uniq` (`cart_id`,`bookedition_id`),
  KEY `store_cartitem_bookedition_id_583268a3_fk_store_bookedition_id` (`bookedition_id`),
  CONSTRAINT `store_cartitem_bookedition_id_583268a3_fk_store_bookedition_id` FOREIGN KEY (`bookedition_id`) REFERENCES `store_bookedition` (`id`),
  CONSTRAINT `store_cartitem_cart_id_4f60ac05_fk_store_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `store_cart` (`id`),
  CONSTRAINT `store_cartitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_cartitem`
--

LOCK TABLES `store_cartitem` WRITE;
/*!40000 ALTER TABLE `store_cartitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_customer`
--

DROP TABLE IF EXISTS `store_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone` varchar(255) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `store_customer_user_id_04276401_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_customer`
--

LOCK TABLES `store_customer` WRITE;
/*!40000 ALTER TABLE `store_customer` DISABLE KEYS */;
INSERT INTO `store_customer` VALUES (1,'',NULL,1);
/*!40000 ALTER TABLE `store_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_discount`
--

DROP TABLE IF EXISTS `store_discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_discount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `discount_status` varchar(1) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext,
  `discount_percent` decimal(3,2) NOT NULL,
  `starts_at` datetime(6) NOT NULL,
  `ends_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_discount`
--

LOCK TABLES `store_discount` WRITE;
/*!40000 ALTER TABLE `store_discount` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_genre`
--

DROP TABLE IF EXISTS `store_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_genre` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext,
  `updated_at` datetime(6) NOT NULL,
  `featured_book_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `store_genre_featured_book_id_42baf1e1_fk_store_book_id` (`featured_book_id`),
  KEY `store_genre_slug_9154915a` (`slug`),
  CONSTRAINT `store_genre_featured_book_id_42baf1e1_fk_store_book_id` FOREIGN KEY (`featured_book_id`) REFERENCES `store_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_genre`
--

LOCK TABLES `store_genre` WRITE;
/*!40000 ALTER TABLE `store_genre` DISABLE KEYS */;
INSERT INTO `store_genre` VALUES (1,'Poetry','poetry','','2023-03-22 00:42:30.654747',NULL),(2,'Prose','prose','','2023-03-22 00:42:42.163879',NULL);
/*!40000 ALTER TABLE `store_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_order`
--

DROP TABLE IF EXISTS `store_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `payment_status` varchar(1) NOT NULL,
  `placed_at` datetime(6) DEFAULT NULL,
  `fullname` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `shippingaddress` varchar(255) NOT NULL,
  `zipcode` varchar(255) NOT NULL,
  `street` varchar(255) NOT NULL,
  `total_amount` decimal(8,2) DEFAULT NULL,
  `stripe_token` varchar(255) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_order_customer_id_13d6d43e_fk_store_customer_id` (`customer_id`),
  CONSTRAINT `store_order_customer_id_13d6d43e_fk_store_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_order`
--

LOCK TABLES `store_order` WRITE;
/*!40000 ALTER TABLE `store_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_orderitem`
--

DROP TABLE IF EXISTS `store_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` smallint unsigned NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `bookedition_id` bigint NOT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_orderitem_bookedition_id_8bd09ad8_fk_store_bookedition_id` (`bookedition_id`),
  KEY `store_orderitem_order_id_acf8722d_fk_store_order_id` (`order_id`),
  CONSTRAINT `store_orderitem_bookedition_id_8bd09ad8_fk_store_bookedition_id` FOREIGN KEY (`bookedition_id`) REFERENCES `store_bookedition` (`id`),
  CONSTRAINT `store_orderitem_order_id_acf8722d_fk_store_order_id` FOREIGN KEY (`order_id`) REFERENCES `store_order` (`id`),
  CONSTRAINT `store_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_orderitem`
--

LOCK TABLES `store_orderitem` WRITE;
/*!40000 ALTER TABLE `store_orderitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_publisher`
--

DROP TABLE IF EXISTS `store_publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_publisher` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `publisherhouse` varchar(255) NOT NULL,
  `city` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_publisher`
--

LOCK TABLES `store_publisher` WRITE;
/*!40000 ALTER TABLE `store_publisher` DISABLE KEYS */;
INSERT INTO `store_publisher` VALUES (1,'Self Published',NULL,NULL);
/*!40000 ALTER TABLE `store_publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_review`
--

DROP TABLE IF EXISTS `store_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` longtext NOT NULL,
  `created_at` date NOT NULL,
  `book_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_review_book_id_8b84a83d_fk_store_book_id` (`book_id`),
  KEY `store_review_customer_id_8a20ccc2_fk_store_customer_id` (`customer_id`),
  CONSTRAINT `store_review_book_id_8b84a83d_fk_store_book_id` FOREIGN KEY (`book_id`) REFERENCES `store_book` (`id`),
  CONSTRAINT `store_review_customer_id_8a20ccc2_fk_store_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `store_customer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_review`
--

LOCK TABLES `store_review` WRITE;
/*!40000 ALTER TABLE `store_review` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_review` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-22  1:04:02
