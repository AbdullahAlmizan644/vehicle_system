-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2022 at 09:24 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vehicle_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `insurance`
--

CREATE TABLE `insurance` (
  `id` int(12) NOT NULL,
  `username` varchar(200) NOT NULL,
  `card` varchar(200) NOT NULL,
  `car_number` varchar(200) NOT NULL,
  `card_cvv` varchar(200) NOT NULL DEFAULT 'cvv',
  `address` varchar(200) NOT NULL,
  `validity` datetime(6) NOT NULL,
  `date` datetime(6) NOT NULL,
  `price` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `insurance`
--

INSERT INTO `insurance` (`id`, `username`, `card`, `car_number`, `card_cvv`, `address`, `validity`, `date`, `price`) VALUES
(1, 'mizan', 'MasterCard', '12345', 'cvv', 'Chittagong,Bangladesh', '2022-11-20 19:01:44.872747', '2022-05-18 19:01:44.872747', '5000'),
(2, 'mizan', 'Visa', '12345', 'cvv', 'Chittagong,Bangladesh', '2022-11-20 19:04:05.792349', '2022-05-18 19:04:05.792349', '5000');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(12) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `product_price` varchar(200) NOT NULL,
  `product_image` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `state` varchar(200) NOT NULL,
  `zip` varchar(200) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `card_type` varchar(200) NOT NULL,
  `card_number` varchar(200) NOT NULL,
  `card_cvv` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL,
  `active` int(2) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `product_name`, `product_price`, `product_image`, `address`, `city`, `state`, `zip`, `phone`, `card_type`, `card_number`, `card_cvv`, `username`, `email`, `date`, `active`) VALUES
(22, 'ferrari', '1000000', 'Ferrari S.p.A. (/fəˈrɑːri/; Italian: [ferˈraːri]) is an Italian luxury sports car manufacturer based in Maranello, Italy. Founded by Enzo Ferrari in 1939 from the Alfa Romeo racing division as Auto Av', 'Chittagong,Bangladesh', 'Chittagong', 'Chittagong', '4217', '01862856218', 'MasterCard', '12345', '12345', 'mizan', 'mizan@gmail.com', '2022-05-18 16:20:37.008510', 0);

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `post_id` int(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` varchar(10000) NOT NULL,
  `writer` varchar(20) NOT NULL DEFAULT 'writer',
  `image` varchar(1000) NOT NULL DEFAULT 'blog.jpg',
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`post_id`, `title`, `content`, `writer`, `image`, `date`) VALUES
(1, 'This is post 1', 'aasasasaaaa', 'writer', 'blog.jpg', '2022-03-13 13:33:22.000000'),
(2, 'this is post 2', 'asasasaasasas', 'writer', 'blog.jpg', '2022-03-13 13:33:22.000000'),
(6, 'this is 4th post', ' asamsamsa', 'mizan', 'blog.jpg', '2022-03-13 20:18:54.536971'),
(9, 'nx,nZ<xnZNx', ' SASBsASGAvZVxvzxvzxvx', 'mizan', '2022-04-24.png', '2022-05-17 23:14:12.451359');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  `description` varchar(10000) NOT NULL,
  `image` varchar(200) NOT NULL DEFAULT 'product.jpg',
  `category` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL,
  `type` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `name`, `price`, `description`, `image`, `category`, `date`, `type`) VALUES
(5, 'ferrari', '1000000', 'Ferrari S.p.A. (/fəˈrɑːri/; Italian: [ferˈraːri]) is an Italian luxury sports car manufacturer based in Maranello, Italy. Founded by Enzo Ferrari in 1939 from the Alfa Romeo racing division as Auto Avio Costruzioni, the company built its first car in 1940, and produced its first Ferrari-badged car in 1947.\r\n\r\nFiat S.p.A. acquired 50% of Ferrari in 1969 and expanded its stake to 90% in 1988.[4] In October 2014, Fiat Chrysler Automobiles (FCA) announced its intentions to separate Ferrari S.p.A. from FCA; as of the announcement FCA owned 90% of Ferrari.[5][6][7] The separation began in October 2015 with a restructuring that established Ferrari N.V. (a company incorporated in the Netherlands) as the new holding company of the Ferrari S.p.A. group,[8] and the subsequent sale by FCA of 10% of the shares in an IPO and concurrent listing of common shares on the New York Stock Exchange.[9] Through the remaining steps of the separation, FCA\'s interest in Ferrari\'s business was distributed to shareholders of FCA, with 10% continuing to be owned by Piero Ferrari.[10] The spin-off was completed on the 3rd of January 2016.[9]\r\n\r\nThroughout its history, the company has been noted for its continued participation in racing, especially in Formula One, where it is the oldest and most successful racing team, holding the most constructors\' championships (16) and having produced the highest number of drivers\' championship wins (15).[11] Ferrari road cars are generally seen as a symbol of speed, luxury and wealth.[12] Ferrari cars are built at the 165,000 square-metre (16.5-hectare) Maranello factory.[13] In 2014 Ferrari was rated the world\'s most powerful brand by Brand Finance.[14] In June 2018, a 1963 250 GTO became the most expensive car in history, setting an all-time record selling price of $70 million.[15][16] As of 2021, Ferrari is the 10th-largest car manufacturer by market capitalisation, with $52.21 billion.[17]', 'car-ferrari-portofino-m_splash.jpg', 'Buy', '2022-05-16 11:41:57.178437', 'Car'),
(6, 'Bike', '20000', 'Fiat S.p.A. acquired 50% of Ferrari in 1969 and expanded its stake to 90% in 1988.[4] In October 2014, Fiat Chrysler Automobiles (FCA) announced its intentions to separate Ferrari S.p.A. from FCA; as of the announcement FCA owned 90% of Ferrari.[5][6][7] The separation began in October 2015 with a restructuring that established Ferrari N.V. (a company incorporated in the Netherlands) as the new holding company of the Ferrari S.p.A. group,[8] and the subsequent sale by FCA of 10% of the shares in an IPO and concurrent listing of common shares on the New York Stock Exchange.[9] Through the remaining steps of the separation, FCA\'s interest in Ferrari\'s business was distributed to shareholders of FCA, with 10% continuing to be owned by Piero Ferrari.[10] The spin-off was completed on the 3rd of January 2016.[9]', 're-meteor-1604664469.jpg', 'Rent', '2022-05-16 11:43:24.590516', 'Bike'),
(7, 'car', '10000000', 'acnamcnmNmMcnm,xc', 'pexels-mike-170811.jpg', 'Rent', '2022-05-16 11:43:53.359668', 'Car'),
(8, 'Bike2', '121311', 'ncmmnCmCmc<', 're-meteor-1604664469.jpg', 'Buy', '2022-05-16 11:44:47.085872', 'Bike');

-- --------------------------------------------------------

--
-- Table structure for table `rents`
--

CREATE TABLE `rents` (
  `rent_id` int(12) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `rent_price` varchar(200) NOT NULL,
  `rent_date` datetime(6) NOT NULL,
  `validity` datetime(6) NOT NULL,
  `card` varchar(200) NOT NULL,
  `card_number` varchar(200) NOT NULL,
  `card_cvv` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rents`
--

INSERT INTO `rents` (`rent_id`, `username`, `email`, `address`, `product_name`, `rent_price`, `rent_date`, `validity`, `card`, `card_number`, `card_cvv`) VALUES
(1, 'mizan', 'mizan@gmail.com', 'Chittagong,Bangladesh', 'Bike', '20000', '2022-05-18 20:05:43.727343', '2022-06-18 20:05:43.727343', 'MasterCard', '12345', '12345'),
(2, 'mizan', 'mizan@gmail.com', 'Chittagong,Bangladesh', 'Bike', '20000', '2022-05-18 20:06:20.163218', '2022-06-18 20:06:20.163218', 'MasterCard', '12345', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `repairs`
--

CREATE TABLE `repairs` (
  `repair_id` int(12) NOT NULL,
  `username` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `vehicle_name` varchar(200) NOT NULL,
  `vehicle_model` varchar(200) NOT NULL,
  `service_time` time(6) NOT NULL,
  `service_date` date NOT NULL,
  `address` varchar(200) NOT NULL,
  `active` int(6) NOT NULL DEFAULT 0,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `repairs`
--

INSERT INTO `repairs` (`repair_id`, `username`, `category`, `vehicle_name`, `vehicle_model`, `service_time`, `service_date`, `address`, `active`, `date`) VALUES
(1, 'mizan', 'Car', 'ferari', '10x', '00:02:00.000000', '2022-05-16', 'ctg,gec moor', 1, '2022-05-16 00:02:29.115303'),
(4, 'jubaer', 'Bike', 'platina', 'platina', '22:53:00.000000', '2022-05-18', 'rangunia,ctg', 0, '2022-05-18 22:53:25.947861');

-- --------------------------------------------------------

--
-- Table structure for table `review_comments`
--

CREATE TABLE `review_comments` (
  `id` int(12) NOT NULL,
  `username` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL,
  `message` varchar(200) NOT NULL,
  `post_id` int(12) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `review_comments`
--

INSERT INTO `review_comments` (`id`, `username`, `image`, `message`, `post_id`, `date`) VALUES
(1, 'mizan', 'fahad.jpg', 'very nice post', 1, '2022-05-18 17:35:56.353703'),
(2, 'mizan', 'fahad.jpg', 'vcvcvcvcvcv', 1, '2022-05-18 17:47:02.193075'),
(4, 'jubaer', 'user.png', 'cmnmcn\r\n', 6, '2022-05-19 01:23:08.947412');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL DEFAULT 'user.png',
  `password` varchar(20) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `username`, `email`, `image`, `password`, `date`) VALUES
(1, 'mizan', 'mizan@gmail.com', '2022-04-24.png', '12345678', '2022-03-10 20:23:34.814038'),
(3, 'jubaer', 'jubaer@gmail.com', 'user.png', '12345678', '2022-05-18 22:26:23.974852');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `insurance`
--
ALTER TABLE `insurance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`post_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `rents`
--
ALTER TABLE `rents`
  ADD PRIMARY KEY (`rent_id`);

--
-- Indexes for table `repairs`
--
ALTER TABLE `repairs`
  ADD PRIMARY KEY (`repair_id`);

--
-- Indexes for table `review_comments`
--
ALTER TABLE `review_comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `insurance`
--
ALTER TABLE `insurance`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `post_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `rents`
--
ALTER TABLE `rents`
  MODIFY `rent_id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `repairs`
--
ALTER TABLE `repairs`
  MODIFY `repair_id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `review_comments`
--
ALTER TABLE `review_comments`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
