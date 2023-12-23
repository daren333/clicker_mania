-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS clicker_mania;

-- Use the clicker_mania database
USE clicker_mania;

-- Create the users_table
CREATE TABLE IF NOT EXISTS `users_table` (
    `user_id` VARCHAR(255) PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `dob` DATE NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `phone_number` VARCHAR(255) NOT NULL,
    `creation_timestamp` TIMESTAMP NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Create the pets_table
CREATE TABLE IF NOT EXISTS `pets_table` (
    `pet_id` VARCHAR(255) PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `dob` DATE NOT NULL,
    `gender` VARCHAR(10) NOT NULL,
    `creation_timestamp` TIMESTAMP NOT NULL,
    `user_id` VARCHAR(255) NOT NULL,
    `age` INT NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users_table (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Create the tricks_table
CREATE TABLE IF NOT EXISTS `tricks_table` (
    `trick_id` VARCHAR(255) PRIMARY KEY,
    `trick_name` VARCHAR(255) NOT NULL,
    `pet_id` VARCHAR(255) NOT NULL,
    `user_id` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`pet_id`) REFERENCES pets_table (`pet_id`),
    FOREIGN KEY (`user_id`) REFERENCES users_table (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Create the clicks_table
CREATE TABLE IF NOT EXISTS `clicks_table` (
    `timestamp` TIMESTAMP NOT NULL PRIMARY KEY,
    `treat_likelihood` INT NOT NULL,
    `treated` BOOLEAN NOT NULL,
    `user_id` VARCHAR(255) NOT NULL,
    `pet_id` VARCHAR(255) NOT NULL,
    `trick_id` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users_table (`user_id`),
    FOREIGN KEY (`pet_id`) REFERENCES pets_table (`pet_id`),
    FOREIGN KEY (`trick_id`) REFERENCES tricks_table (`trick_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
