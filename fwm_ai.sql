-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 12, 2024 at 05:23 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fwm_ai`
--

-- --------------------------------------------------------

--
-- Table structure for table `fwm_address`
--

CREATE TABLE `fwm_address` (
  `street` varchar(255) NOT NULL,
  `barangay` varchar(255) NOT NULL,
  `municipality` varchar(255) NOT NULL,
  `province` varchar(255) NOT NULL,
  `zip_code` varchar(255) NOT NULL,
  `address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fwm_address`
--

INSERT INTO `fwm_address` (`street`, `barangay`, `municipality`, `province`, `zip_code`, `address_id`) VALUES
('Luisito St.', 'Barangay Dos', 'Daet', 'Camarines Norte', '4600', 1),
('Roxas Avenue', 'Malabanias', 'Angeles City', 'Pampanga', '2009', 2),
('Lacson Street', 'Mandaluyong', 'Bacolod City', 'Negros Occidental', '6100', 3),
('Quezon Avenue', 'Lahug', 'Cebu City', 'Cebu', '6000', 4),
('Taft Avenue', 'San Lorenzo', 'Makati', 'Metro Manila', '1231', 5),
('Mabini Street', 'Poblacion', 'Makati', 'Metro Manila', '1234', 6);

-- --------------------------------------------------------

--
-- Table structure for table `fwm_customer`
--

CREATE TABLE `fwm_customer` (
  `cus_id` int(11) NOT NULL,
  `cus_name` varchar(255) NOT NULL,
  `cus_contact` varchar(13) NOT NULL,
  `cus_email` varchar(255) NOT NULL,
  `cus_address` int(11) NOT NULL,
  `cus_uname` varchar(20) NOT NULL,
  `cus_pass` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fwm_customer`
--

INSERT INTO `fwm_customer` (`cus_id`, `cus_name`, `cus_contact`, `cus_email`, `cus_address`, `cus_uname`, `cus_pass`) VALUES
(1, 'Dennis Hamilton', '+639856754323', 'dennisham@gmail.com', 1, 'denham@24', '0a43a2e18dcb8ddcdba03faa69a04cdbe61a4819'),
(3, 'John Doe', '123456789', 'johndoe@example.com', 4, 'johndoe123', 'cbfdac6008f9cab4083784cbd1874f76618d2a97'),
(4, 'Jane Smith', '987654321', 'janesmith@example.com', 3, 'janesmith456', '0c6f6845bb8c62b778e9147c272ac4b5bdb9ae71'),
(5, 'Michael Johnson', '555444333', 'michaeljohnson@example.com', 2, 'mjohnson789', '7f6d5eea1bcef5ca6209d33b28e3aaeb3db26f24'),
(6, 'Emily Brown', '222333444', 'emilybrown@example.com', 1, 'ebrown101', '523cf99e800d57d0ff0ac7b97e04ebc2b9b4b263'),
(7, 'David Wilson', '777888999', 'davidwilson@example.com', 5, 'dwilson202', '6d10233e04f1913b74d8f96079a96b32eabb0335');

-- --------------------------------------------------------

--
-- Table structure for table `fwm_orders`
--

CREATE TABLE `fwm_orders` (
  `order_id` int(11) NOT NULL,
  `order_refNum` varchar(255) NOT NULL,
  `setter_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  `order_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `fwm_organization`
--

CREATE TABLE `fwm_organization` (
  `org_id` int(11) NOT NULL,
  `org_name` varchar(255) NOT NULL,
  `org_contact` varchar(13) NOT NULL,
  `org_email` varchar(255) NOT NULL,
  `org_address` int(11) NOT NULL,
  `org_uname` varchar(20) NOT NULL,
  `org_pass` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fwm_organization`
--

INSERT INTO `fwm_organization` (`org_id`, `org_name`, `org_contact`, `org_email`, `org_address`, `org_uname`, `org_pass`) VALUES
(1, 'ABC Corporation', '123456789', 'abc@example.com', 1, 'abc_corp', 'cbfdac6008f9cab4083784cbd1874f76618d2a97'),
(2, 'XYZ Company', '987654321', 'xyz@example.com', 2, 'xyz_company', '0c6f6845bb8c62b778e9147c272ac4b5bdb9ae71'),
(3, 'PQR Enterprises', '555444333', 'pqr@example.com', 3, 'pqr_enterprises', '7f6d5eea1bcef5ca6209d33b28e3aaeb3db26f24'),
(4, 'LMN Ltd.', '222333444', 'lmn@example.com', 4, 'lmn_ltd', '523cf99e800d57d0ff0ac7b97e04ebc2b9b4b263'),
(5, 'EFG Inc.', '777888999', 'efg@example.com', 5, 'efg_inc', '6d10233e04f1913b74d8f96079a96b32eabb0335');

-- --------------------------------------------------------

--
-- Table structure for table `fwm_products`
--

CREATE TABLE `fwm_products` (
  `prod_id` int(11) NOT NULL,
  `prod_name` varchar(255) NOT NULL,
  `vendor_id` int(11) NOT NULL,
  `prod_price` decimal(11,2) NOT NULL,
  `prod_quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `fwm_vendor`
--

CREATE TABLE `fwm_vendor` (
  `vendor_id` int(11) NOT NULL,
  `vendor_name` varchar(255) NOT NULL,
  `vendor_address` int(11) NOT NULL,
  `vendor_contact` varchar(13) NOT NULL,
  `vendor_email` varchar(255) NOT NULL,
  `vendor_uname` varchar(20) NOT NULL,
  `vendor_pass` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fwm_address`
--
ALTER TABLE `fwm_address`
  ADD PRIMARY KEY (`address_id`);

--
-- Indexes for table `fwm_customer`
--
ALTER TABLE `fwm_customer`
  ADD PRIMARY KEY (`cus_id`),
  ADD UNIQUE KEY `cus_contact` (`cus_contact`,`cus_email`,`cus_uname`),
  ADD KEY `cus_address` (`cus_address`);

--
-- Indexes for table `fwm_orders`
--
ALTER TABLE `fwm_orders`
  ADD PRIMARY KEY (`order_id`),
  ADD UNIQUE KEY `order_refNum` (`order_refNum`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `vendor_id` (`vendor_id`),
  ADD KEY `setter_id_2` (`setter_id`),
  ADD KEY `setter_id` (`setter_id`);

--
-- Indexes for table `fwm_organization`
--
ALTER TABLE `fwm_organization`
  ADD PRIMARY KEY (`org_id`),
  ADD UNIQUE KEY `org_contact` (`org_contact`,`org_email`,`org_uname`),
  ADD KEY `org_address` (`org_address`);

--
-- Indexes for table `fwm_products`
--
ALTER TABLE `fwm_products`
  ADD PRIMARY KEY (`prod_id`),
  ADD KEY `vendor_id` (`vendor_id`);

--
-- Indexes for table `fwm_vendor`
--
ALTER TABLE `fwm_vendor`
  ADD PRIMARY KEY (`vendor_id`),
  ADD UNIQUE KEY `vendor_contact` (`vendor_contact`,`vendor_email`,`vendor_uname`),
  ADD KEY `vendor_address` (`vendor_address`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fwm_address`
--
ALTER TABLE `fwm_address`
  MODIFY `address_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `fwm_customer`
--
ALTER TABLE `fwm_customer`
  MODIFY `cus_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `fwm_orders`
--
ALTER TABLE `fwm_orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `fwm_organization`
--
ALTER TABLE `fwm_organization`
  MODIFY `org_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `fwm_products`
--
ALTER TABLE `fwm_products`
  MODIFY `prod_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `fwm_vendor`
--
ALTER TABLE `fwm_vendor`
  MODIFY `vendor_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `fwm_customer`
--
ALTER TABLE `fwm_customer`
  ADD CONSTRAINT `fwm_customer_ibfk_1` FOREIGN KEY (`cus_address`) REFERENCES `fwm_address` (`address_id`);

--
-- Constraints for table `fwm_orders`
--
ALTER TABLE `fwm_orders`
  ADD CONSTRAINT `fwm_orders_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `fwm_products` (`prod_id`),
  ADD CONSTRAINT `fwm_orders_ibfk_2` FOREIGN KEY (`vendor_id`) REFERENCES `fwm_vendor` (`vendor_id`),
  ADD CONSTRAINT `fwm_orders_ibfk_3` FOREIGN KEY (`setter_id`) REFERENCES `fwm_customer` (`cus_id`),
  ADD CONSTRAINT `fwm_orders_ibfk_4` FOREIGN KEY (`setter_id`) REFERENCES `fwm_organization` (`org_id`);

--
-- Constraints for table `fwm_organization`
--
ALTER TABLE `fwm_organization`
  ADD CONSTRAINT `fwm_organization_ibfk_1` FOREIGN KEY (`org_address`) REFERENCES `fwm_address` (`address_id`);

--
-- Constraints for table `fwm_products`
--
ALTER TABLE `fwm_products`
  ADD CONSTRAINT `fwm_products_ibfk_1` FOREIGN KEY (`vendor_id`) REFERENCES `fwm_vendor` (`vendor_id`);

--
-- Constraints for table `fwm_vendor`
--
ALTER TABLE `fwm_vendor`
  ADD CONSTRAINT `fwm_vendor_ibfk_1` FOREIGN KEY (`vendor_address`) REFERENCES `fwm_address` (`address_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
