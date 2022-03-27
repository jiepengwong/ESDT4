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
  `ItemID` varchar(64) NOT NULL,
  `ItemName` varchar(64) NOT NULL,
  `Seller_ID` varchar(10) NOT NULL,
  `ItemDesc` varchar(64) NOT NULL,
  `Category` varchar(64) NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `ItemStatus` varchar(64) DEFAULT NULL,

  PRIMARY KEY (`ItemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `item`
--

INSERT INTO `Item` (`ItemID`, `ItemName`, `Seller_ID`, `ItemDesc`, `Category`, `Price`, `ItemStatus`) VALUES
('1234567891', 'Test item 1', '9234567891', 'This is Test item 1', 'Test', 5.50, 'Open'),
('1234567892', 'Test item 2', '9234567892', 'This is Test item 2', 'Test', 7.50, 'Close'),
('1234567893', 'Test item 3', '9234567893', 'This is Test item 3', 'Test', 9.50, 'Pending'),
('1234567894', 'Test item 4', '9234567894', 'This is Test item 4', 'Test', 15.50, 'Open'),
('1234567895', 'Test item 5', '9234567895', 'This is Test item 5', 'Test', 17.50, 'Close'),
('1234567896', 'Test item 6', '9234567896', 'This is Test item 6', 'Test', 19.50, 'Pending');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
