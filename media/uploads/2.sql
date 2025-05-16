--
-- Create model UserBaseInfo
--
CREATE TABLE `userBaseInfo2` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `username` varchar(30) NOT NULL, `password` varchar(20) NOT NULL, `email` varchar(254) NOT NULL, `phone` varchar(11) NOT NULL, `status` varchar(1) NOT NULL, `createDate` datetime(6) NOT NULL);
