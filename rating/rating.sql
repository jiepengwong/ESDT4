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

DROP TABLE IF EXISTS Profile;
CREATE TABLE IF NOT EXISTS Rating (
  userId varchar(64) NOT NULL,
  name varchar(64) NOT NULL,
  email varchar(64) NOT NULL,
  ratings float DEFAULT NULL,
  counts int DEFAULT NULL,
  temp float DEFAULT NULL,
  PRIMARY KEY (userID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO Rating
  (userId, name, email, ratings, count, temp) 

VALUES
    (1234, "the", "the@gmail.com", 3.4, 4, NULL),
    (4312, "market", "market@email.com", 2.3, 5, NULL),
    (2314, "place", "place@email.com", 5.0, 3, NULL);