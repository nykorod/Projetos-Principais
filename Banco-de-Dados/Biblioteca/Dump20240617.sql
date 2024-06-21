CREATE DATABASE  IF NOT EXISTS `cadastro` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cadastro`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: cadastro
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `id` int DEFAULT NULL,
  `nome` varchar(40) NOT NULL,
  `descr` text,
  `carga` int unsigned DEFAULT NULL,
  `aulas` int DEFAULT NULL,
  `ano` year DEFAULT '2016',
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gafanhotos`
--

DROP TABLE IF EXISTS `gafanhotos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gafanhotos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `prof` varchar(20) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `sexo` enum('M','F') DEFAULT NULL,
  `peso` decimal(5,2) DEFAULT NULL,
  `altura` decimal(3,2) DEFAULT NULL,
  `nacionalidade` varchar(20) DEFAULT 'brasil',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gafanhotos`
--

LOCK TABLES `gafanhotos` WRITE;
/*!40000 ALTER TABLE `gafanhotos` DISABLE KEYS */;
INSERT INTO `gafanhotos` VALUES (1,'nykorod',NULL,'2006-11-22','M',100.56,1.85,'brasil'),(2,'feeeer',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(3,'feeeer',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(4,'feeeer',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(5,'feeeer',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(6,'feeeer',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(7,'feeeer',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(8,'feeeer',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(9,'maria',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(10,'maria',NULL,'2004-09-17','F',50.26,1.60,'brasil'),(11,'enrick',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(12,'enrick',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(13,'paulin',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(14,'pinho',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(15,'simas',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(16,'turbo(caracol',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(17,'enrick',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(18,'paulin',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(19,'pinho',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(20,'simas',NULL,'2003-02-04','M',60.23,1.80,'brasil'),(21,'turbo(caracol',NULL,'2003-02-04','M',60.23,1.80,'brasil');
/*!40000 ALTER TABLE `gafanhotos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-17 15:34:15
