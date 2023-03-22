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

USE nabshop;
--
-- Dumping data for table `store_author`
--

LOCK TABLES `store_author` WRITE;
/*!40000 ALTER TABLE `store_author` DISABLE KEYS */;
INSERT INTO `store_author` VALUES (1,'Nabil','Affo',NULL,NULL),(2,'Nabil','Alshaaeir',NULL,NULL);
/*!40000 ALTER TABLE `store_author` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `store_book`
--

LOCK TABLES `store_book` WRITE;
/*!40000 ALTER TABLE `store_book` DISABLE KEYS */;
INSERT INTO `store_book` VALUES (1,'Chants de lettres','chants-de-lettres','Dans son deuxième recueil de poèmes, Chants de lettres, Nabil Affo nourrit la ferme et intime conviction que le bonheur attend chacun de nous quels que soient les obstacles qui se dressent sur notre chemin. Ses Chants de lettres racontent l’histoire d’un cœur détruit par l’amour, la séparation, la mort, l’injustice… mais qui est absolument résolu à renaître de ses cendres et à sortir de ce gouffre sinistre qui l’a vu sommeiller, pour en fin de compte s’élever et être heureux. C’est un chant d’espoir qui appelle, par sa musicalité, sa sensibilité et sa dextérité, à canaliser l’énergie de la souffrance pour en sortir une force indéfectible qui permettra d’avancer et de renouer avec tous les instants de la vie, quitte à s’évader et à parcourir tout l’univers pour y répandre la paix, l’amour et la joie.\r\n\r\n« A cette âme qui veut réaliser un rêve\r\nVivre un bonheur qui jamais ne s’achève\r\nIl est temps qu’elle s’élève »','2023-03-22 00:43:55.651284','2023-03-22 00:43:55.651304',1,1),(2,'Le voyage','le-voyage','Le voyage est un roman de Nabil Affo qui raconte les aventures d’un personnage qui est résolu à partir sur un coup de tête pour une destination qui lui est totalement inconnue, à tout quitter pour trouver les réponses aux questions profondes qui sommeillent en lui. Il rencontrera des êtres étranges mais aussi fascinants les uns que les autres. Parviendra-t-il à trouver ce qu’il cherche véritablement?','2023-03-22 00:44:58.215679','2023-03-22 00:47:24.898777',1,2),(3,'Serenata: Sur le chemin de l\'Orient','serenata','L\'amour ne s\'explique pas,\r\nil se ressent...\r\n\r\n“Serenata: Sur le chemin de l\'Orient\" est une collection de vers romantiques qui, par leur musicalité et leur cadence, font voguer sur des eaux sentimentales au gré du souffle des cœurs en quête d’amour. Ce recueil de poèmes est un chef-d’œuvre inouï qui se veut révélateur des ferveurs du cœur.\r\n\r\n“Je ne sais pas où je vais maintenant\r\nUne lueur dans tes yeux me retient\r\nMa tête baigne dans un océan\r\nMais mon souffle jamais ne s’éteint\"','2023-03-22 00:46:08.367365','2023-03-22 00:46:08.367385',1,1),(4,'Eastern Storms','eastern-storms','\"Eastern Storms\" is a collection of poetry that depicts a period spent in the far East marked by huge storms of life. The reader is driven between emotions of anxiety, loss, depression, quest for love, spirituality and more.','2023-03-22 00:47:12.154564','2023-03-22 00:47:12.154583',2,1);
/*!40000 ALTER TABLE `store_book` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `store_bookedition`
--

LOCK TABLES `store_bookedition` WRITE;
/*!40000 ALTER TABLE `store_bookedition` DISABLE KEYS */;
INSERT INTO `store_bookedition` VALUES (1,'chants-de-lettres-ebook','Ebook','1724275305',2.99,70,'Ebook','2018-08-15',1000000,'2023-03-22 00:49:11.851116','2023-03-22 00:49:11.851133',1,1),(2,'chants-de-lettres-paperback','Paperback','978-1724275301',7.80,108,'Paperback (5.24 x 0.26 x 7.99 inches)','2018-08-16',1000000,'2023-03-22 00:50:26.907818','2023-03-22 00:50:26.907843',1,1),(3,'le-voyage-ebook','Ebook','1724252496',2.99,66,'Ebook','2018-07-26',1000000,'2023-03-22 00:51:37.966035','2023-03-22 00:51:37.966052',2,1),(4,'le-voyage-paperback','Paperback','978-1724252494',7.80,126,'Paperback (5.25 x 0.3 x 8 inches)','2018-07-27',1000000,'2023-03-22 00:52:42.183382','2023-03-22 00:52:42.183407',2,1),(5,'eastern-storms','Ebook','1983298271',2.99,114,'Ebook','2022-02-14',1000000,'2023-03-22 00:53:39.061895','2023-03-22 00:53:39.061911',4,1),(6,'eastern-storms-paperback','Paperback','978-1983298271',10.50,112,'Paperback (5 x 0.26 x 8 inches)','2022-02-15',1000000,'2023-03-22 00:54:41.401467','2023-03-22 00:54:41.401481',4,1),(7,'sereneta-ebook','Ebook','1717887759',1.99,40,'Ebook','2019-05-17',1000000,'2023-03-22 00:55:47.471736','2023-03-22 00:55:47.471763',3,1),(8,'serenata-paperback','Paperback','978-1717887757',5.57,100,'Paperback (5 x 0.25 x 8 inches)','2019-05-18',1000000,'2023-03-22 00:57:21.275771','2023-03-22 00:57:21.275785',3,1);
/*!40000 ALTER TABLE `store_bookedition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `store_genre`
--

LOCK TABLES `store_genre` WRITE;
/*!40000 ALTER TABLE `store_genre` DISABLE KEYS */;
INSERT INTO `store_genre` VALUES (1,'Poetry','poetry','','2023-03-22 00:42:30.654747',NULL),(2,'Prose','prose','','2023-03-22 00:42:42.163879',NULL);
/*!40000 ALTER TABLE `store_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `store_publisher`
--

LOCK TABLES `store_publisher` WRITE;
/*!40000 ALTER TABLE `store_publisher` DISABLE KEYS */;
INSERT INTO `store_publisher` VALUES (1,'Self Published',NULL,NULL);
/*!40000 ALTER TABLE `store_publisher` ENABLE KEYS */;
UNLOCK TABLES;



-- Dump completed on 2023-03-22  1:04:02
