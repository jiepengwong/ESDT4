-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `item`
--
CREATE DATABASE IF NOT EXISTS `item` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `item`;

-- --------------------------------------------------------

--
-- Table structure for table `Item`
--

DROP TABLE IF EXISTS `item`;
CREATE TABLE IF NOT EXISTS `Item` (
  `ItemID` int(10) NOT NULL,
  `ItemName` varchar(64) NOT NULL,
  `Seller_ID` int(15) NOT NULL,
  `ItemDesc` varchar(64) NOT NULL,
  `Category` varchar(64) NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `ItemStatus` varchar(64) DEFAULT NULL,

  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `item`
--

INSERT INTO `Item` (`ItemID`, `ItemName`, `UserID_Seller`, `QtyAvail`, `ItemDesc`, `Reviews`, `Price`) VALUES
('0000000001', 'Test item 1', '0000000001', 2, 'This is Test item 1', 'Test item 1 is great', 5.50);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
