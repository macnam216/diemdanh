-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 05, 2019 at 04:31 AM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tt_rtos`
--

-- --------------------------------------------------------

--
-- Table structure for table `luong`

--
CREATE DATABASE `quanlinhanvien`;

CREATE TABLE `luong` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `luong`
--

INSERT INTO `luong` (`id`, `name`, `salary`) VALUES
(1, 'bac nguyen', 3000000),
(3, 'ngoc thanh', 4000000),
(4, 'nam', 3600000),
(6, 'tung', 2400000);

-- --------------------------------------------------------

--
-- Table structure for table `quan_li_nv`
--

CREATE TABLE `quan_li_nv` (
  `id` int(11) NOT NULL,
  `code` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `branch` text DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `hourwork` int(11) DEFAULT NULL,
  `hoursalary` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `quan_li_nv`
--

INSERT INTO `quan_li_nv` (`id`,`code`, `name`, `branch`, `phone`, `address`, `hourwork`, `hoursalary`) VALUES
(1,'bacnv', 'bac nguyen', 'IT', 911871, 'hcm city', 100, 30),
(3,'ngoctn', 'ngoc thanh', 'Sale', 8234765, 'da nang', 200, 20),
(4,'nammv', 'nam', 'Support', 22666, 'thu duc', 120, 30),
(6,'tungtt', 'tung', 'Support', 2222, 'qnam', 120, 20);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `luong`
--
ALTER TABLE `luong`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `quan_li_nv`
--
ALTER TABLE `quan_li_nv`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `luong`
--
ALTER TABLE `luong`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `quan_li_nv`
--
ALTER TABLE `quan_li_nv`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
