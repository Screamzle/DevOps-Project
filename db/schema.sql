CREATE DATABASE IF NOT EXISTS `workoutdb`;
USE `workoutdb`;


CREATE TABLE IF NOT EXISTS `exercises` (
  `exercise_ID` int NOT NULL AUTO_INCREMENT,
  `exercise_name` varchar(50) NOT NULL,
  `repetitions` int NOT NULL,
  `sets` int NOT NULL,
  PRIMARY KEY (`exercise_ID`),
  UNIQUE KEY `exercise_name` (`exercise_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `users` (
  `user_ID` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(15) NOT NULL,
  `password` varchar(100) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email_address` varchar(75) NOT NULL,
  `date_created` datetime NOT NULL,
  PRIMARY KEY (`user_ID`),
  UNIQUE KEY `user_name` (`user_name`),
  UNIQUE KEY `email_address` (`email_address`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `workout_exercises` (
  `plan_id` int NOT NULL,
  `exercise_id` int NOT NULL,
  PRIMARY KEY (`plan_id`,`exercise_id`),
  KEY `exercise_id` (`exercise_id`),
  CONSTRAINT `workout_exercises_ibfk_1` FOREIGN KEY (`plan_id`) REFERENCES `workout_plans` (`plan_id`),
  CONSTRAINT `workout_exercises_ibfk_2` FOREIGN KEY (`exercise_id`) REFERENCES `exercises` (`exercise_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `workout_names` (
  `workout_name` varchar(30) NOT NULL,
  PRIMARY KEY (`workout_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `workout_plans` (
  `plan_id` int NOT NULL AUTO_INCREMENT,
  `workout_name` varchar(30) NOT NULL,
  `user_ID` int NOT NULL,
  `exercise_ID` int NOT NULL,
  PRIMARY KEY (`plan_id`),
  KEY `workout_name` (`workout_name`),
  KEY `user_ID` (`user_ID`),
  KEY `exercise_ID` (`exercise_ID`),
  CONSTRAINT `workout_plans_ibfk_1` FOREIGN KEY (`workout_name`) REFERENCES `workout_names` (`workout_name`),
  CONSTRAINT `workout_plans_ibfk_2` FOREIGN KEY (`user_ID`) REFERENCES `users` (`user_ID`),
  CONSTRAINT `workout_plans_ibfk_3` FOREIGN KEY (`exercise_ID`) REFERENCES `exercises` (`exercise_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;