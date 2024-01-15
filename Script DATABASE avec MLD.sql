-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ProjetDBPY
-- -----------------------------------------------------
DROP DATABASE projetdbpy;
-- -----------------------------------------------------
-- Schema ProjetDBPY
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ProjetDBPY` DEFAULT CHARACTER SET utf8 ;
USE `ProjetDBPY` ;

-- -----------------------------------------------------
-- Table `ProjetDBPY`.`Players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjetDBPY`.`Players` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `alias` VARCHAR(30) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `student` BINARY(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `alias_UNIQUE` (`alias` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjetDBPY`.`Exercises`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjetDBPY`.`Exercises` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjetDBPY`.`Results`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjetDBPY`.`Results` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `start_date` DATETIME NOT NULL,
  `time` TIME NOT NULL,
  `number_done` INT NOT NULL,
  `max_number` INT NOT NULL,
  `exercise_id` INT NOT NULL,
  `player_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_results_Exercises1_idx` (`exercise_id` ASC) VISIBLE,
  INDEX `fk_Results_Players1_idx` (`player_id` ASC) VISIBLE,
  CONSTRAINT `fk_results_Exercises1`
    FOREIGN KEY (`exercise_id`)
    REFERENCES `ProjetDBPY`.`Exercises` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Results_Players1`
    FOREIGN KEY (`player_id`)
    REFERENCES `ProjetDBPY`.`Players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
