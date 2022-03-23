-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 12, 2020 at 02:17 AM
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
-- Database: `order`
--
CREATE DATABASE IF NOT EXISTS `notifications` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `notifications`;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `notifications`;
CREATE TABLE IF NOT EXISTS `notifications` (
  ` ` varchar(64) NOT NULL,
  `Seller_ID` varchar(10) NOT NULL,
  `Buyer_ID` varchar(10) NOT NULL,
  `Status` varchar(10) DEFAULT NULL,
  `Message` varchar(85) DEFAULT NULL,
  `DateTimeSQL` datetime NOT NULL,
  PRIMARY KEY (Notification_ID)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--   constraint comment_pk primary key(user_id, electronic_item, date_time),


--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` ( `Notification_ID`, `Seller_ID`, `Buyer_ID`, `Status`, `Message`, `DateTimeSQL`) VALUES
(123456, '6544321', 'NEW', 'FALALALLAL', '2020-06-12 02:14:55');

-- --------------------------------------------------------
