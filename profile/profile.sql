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


CREATE DATABASE IF NOT EXISTS "Profile" DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE 'Profile';

DROP TABLE IF EXISTS `Profile`;
CREATE TABLE IF NOT EXISTS `Profile_details` (
  `userId` varchar(64) NOT NULL,
  `name` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `ratings` float DEFAULT NULL,
  PRIMARY KEY (`isbn13`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;