-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: ProyectoIntegrador
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.2

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('f07b2eeff5c2');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contagiados`
--

DROP TABLE IF EXISTS `contagiados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contagiados` (
  `DNI` int NOT NULL,
  `Nombre` varchar(250) DEFAULT NULL,
  `Apellido` varchar(250) DEFAULT NULL,
  `Edad` int DEFAULT NULL,
  `Sexo` varchar(25) DEFAULT NULL,
  `Obra_social` varchar(250) DEFAULT NULL,
  `Asistencia` varchar(5) DEFAULT NULL,
  `Telefono` int DEFAULT NULL,
  `Email` varchar(250) DEFAULT NULL,
  `Domicilio` varchar(250) DEFAULT NULL,
  `Barrio` varchar(250) DEFAULT NULL,
  `Fecha_positivo` varchar(250) DEFAULT NULL,
  `Variante` varchar(250) DEFAULT NULL,
  `Fecha_primerosSintomas` varchar(250) DEFAULT NULL,
  `Sintomas` varchar(250) DEFAULT NULL,
  `Comorbilidad` varchar(250) DEFAULT NULL,
  `Fecha_alta` varchar(250) DEFAULT NULL,
  `Fecha_muerte` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contagiados`
--

LOCK TABLES `contagiados` WRITE;
/*!40000 ALTER TABLE `contagiados` DISABLE KEYS */;
INSERT INTO `contagiados` VALUES (11111111,'Karla','Perez',32,'Femenino','No','No',111222444,'kperez@mail.com','San Martin 550','Nueva Cordoba','05/05/2021','Base','01/05/2021','No','No','06/08/2021','99/99/9999'),(12345678,'Juan','Perez',30,'Masculino','OSDE','Si',111222333,'jperez@mail.com','San Martin 500','Centro','03/08/2021','Manaos','29/07/2021','Dolor de cabeza,Tos,Fiebre','Deabetes','99/99/9999','99/99/9999'),(98765432,'Marcos','Gomez',85,'Masculino','PAMI','Si',222333111,'mgomez@mail.com','Av. Las eras 100','Nueva Cordoba','04/07/2021','Base','01/07/2021','Dolor de cuerpo,Fiebre,Dolor de cabeza-Falta de aire','Deabetes,Renal,Cardiaco','99/99/9999','04/08/2021');
/*!40000 ALTER TABLE `contagiados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-22 11:49:27
