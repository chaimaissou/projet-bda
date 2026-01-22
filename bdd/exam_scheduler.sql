-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 13 jan. 2026 à 00:56
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `exam_scheduler`
--

-- --------------------------------------------------------

--
-- Structure de la table `administrateurs`
--

CREATE TABLE `administrateurs` (
  `id` int(11) NOT NULL,
  `matricule` varchar(20) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `role` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `departement_id` int(11) DEFAULT NULL,
  `actif` tinyint(1) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `administrateurs`
--

INSERT INTO `administrateurs` (`id`, `matricule`, `nom`, `prenom`, `role`, `email`, `departement_id`, `actif`, `created_at`) VALUES
(1, 'ADM001', 'Durand', 'Robert', 'Administrateur', 'r.durand@univ.edu', 1, 1, '2026-01-12 19:50:01'),
(2, 'ADM002', 'Lefevre', 'Catherine', 'Doyen', 'c.lefevre@univ.edu', NULL, 1, '2026-01-12 19:50:01'),
(3, 'ADM003', 'Morel', 'Philippe', 'Vice-doyen', 'p.morel@univ.edu', NULL, 1, '2026-01-12 19:50:01'),
(4, 'ADM004', 'Girard', 'Isabelle', 'Administrateur Examens', 'i.girard@univ.edu', 1, 1, '2026-01-12 19:50:01');

-- --------------------------------------------------------

--
-- Structure de la table `contraintes_speciales`
--

CREATE TABLE `contraintes_speciales` (
  `id` int(11) NOT NULL,
  `type_contrainte` varchar(50) NOT NULL,
  `entite_type` varchar(50) DEFAULT NULL,
  `entite_id` int(11) DEFAULT NULL,
  `date_debut` datetime DEFAULT NULL,
  `date_fin` datetime DEFAULT NULL,
  `raison` text DEFAULT NULL,
  `priorite` int(11) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `departements`
--

CREATE TABLE `departements` (
  `id` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `code` varchar(10) NOT NULL,
  `responsable_id` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `departements`
--

INSERT INTO `departements` (`id`, `nom`, `code`, `responsable_id`, `created_at`) VALUES
(1, 'Informatique', 'INFO', NULL, '2026-01-11 19:02:28'),
(2, 'Mathématiques', 'MATH', NULL, '2026-01-11 19:02:28'),
(3, 'Physique', 'PHYS', NULL, '2026-01-11 19:02:28'),
(4, 'Chimie', 'CHIM', NULL, '2026-01-11 19:02:28'),
(5, 'Biologie', 'BIO', NULL, '2026-01-11 19:02:28'),
(6, 'Sciences de la Terre', 'ST', NULL, '2026-01-11 19:02:28'),
(7, 'Langues et Littérature', 'LL', NULL, '2026-01-11 19:02:28');

-- --------------------------------------------------------

--
-- Structure de la table `etudiants`
--

CREATE TABLE `etudiants` (
  `id` int(11) NOT NULL,
  `matricule` varchar(20) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `formation_id` int(11) DEFAULT NULL,
  `promo` int(11) NOT NULL,
  `email` varchar(150) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `etudiants`
--

INSERT INTO `etudiants` (`id`, `matricule`, `nom`, `prenom`, `formation_id`, `promo`, `email`, `telephone`, `created_at`) VALUES
(1, 'ETU001', 'Dupont', 'Jean', 1, 2024, 'etu001@univ.edu', NULL, '2026-01-11 19:02:28'),
(2, 'ETU002', 'Martin', 'Marie', 1, 2024, 'etu002@univ.edu', NULL, '2026-01-11 19:02:28'),
(3, 'ETU003', 'Bernard', 'Pierre', 2, 2024, 'etu003@univ.edu', NULL, '2026-01-11 19:02:28'),
(4, 'ETU004', 'Thomas', 'Sophie', 2, 2024, 'etu004@univ.edu', NULL, '2026-01-11 19:02:28'),
(5, 'ETU005', 'Petit', 'Paul', 3, 2024, 'etu005@univ.edu', NULL, '2026-01-11 19:02:28'),
(6, 'ETU006', 'Robert', 'Julie', 3, 2024, 'etu006@univ.edu', NULL, '2026-01-11 19:02:28'),
(7, 'ETU007', 'Richard', 'Thomas', 4, 2024, 'etu007@univ.edu', NULL, '2026-01-11 19:02:28'),
(8, 'ETU008', 'Durand', 'Laura', 4, 2024, 'etu008@univ.edu', NULL, '2026-01-11 19:02:28'),
(9, 'ETU009', 'Dubois', 'Nicolas', 5, 2024, 'etu009@univ.edu', NULL, '2026-01-11 19:02:28'),
(10, 'ETU010', 'Moreau', 'Sarah', 5, 2024, 'etu010@univ.edu', NULL, '2026-01-11 19:02:28');

-- --------------------------------------------------------

--
-- Structure de la table `examens`
--

CREATE TABLE `examens` (
  `id` int(11) NOT NULL,
  `module_id` int(11) DEFAULT NULL,
  `date_heure` datetime NOT NULL,
  `duree_minutes` int(11) NOT NULL DEFAULT 120,
  `salle_id` int(11) DEFAULT NULL,
  `type_examen` varchar(50) DEFAULT 'Écrit',
  `surveillant_principal_id` int(11) DEFAULT NULL,
  `statut` varchar(20) DEFAULT 'Planifié',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déclencheurs `examens`
--
DELIMITER $$
CREATE TRIGGER `trigger_check_exam_conflict` BEFORE INSERT ON `examens` FOR EACH ROW BEGIN
    DECLARE conflict_count INT;
    
    -- Vérifier conflit de salle
    SELECT COUNT(*) INTO conflict_count
    FROM examens e
    WHERE e.salle_id = NEW.salle_id
    AND e.date_heure < DATE_ADD(NEW.date_heure, INTERVAL NEW.duree_minutes MINUTE)
    AND NEW.date_heure < DATE_ADD(e.date_heure, INTERVAL e.duree_minutes MINUTE)
    AND e.id != NEW.id;
    
    IF conflict_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Conflit de salle: Salle déjà occupée à cet horaire';
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trigger_limit_exams_per_student` BEFORE INSERT ON `examens` FOR EACH ROW BEGIN
    DECLARE student_exam_count INT;
    
    -- Compter les examens pour chaque étudiant ce jour-là
    SELECT COUNT(DISTINCT e.id) INTO student_exam_count
    FROM examens ex
    JOIN modules m ON ex.module_id = m.id
    JOIN inscriptions i ON m.id = i.module_id
    WHERE DATE(ex.date_heure) = DATE(NEW.date_heure)
    AND i.etudiant_id IN (
        SELECT etudiant_id FROM inscriptions 
        WHERE module_id = NEW.module_id
    );
    
    IF student_exam_count >= 1 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'L''étudiant a déjà un examen ce jour';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Structure de la table `exam_surveillance`
--

CREATE TABLE `exam_surveillance` (
  `id` int(11) NOT NULL,
  `examen_id` int(11) DEFAULT NULL,
  `professeur_id` int(11) DEFAULT NULL,
  `role` varchar(50) DEFAULT 'Surveillant',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `formations`
--

CREATE TABLE `formations` (
  `id` int(11) NOT NULL,
  `nom` varchar(150) NOT NULL,
  `code` varchar(20) NOT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `nb_modules` int(11) DEFAULT 7,
  `niveau` varchar(20) DEFAULT NULL,
  `effectif` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `formations`
--

INSERT INTO `formations` (`id`, `nom`, `code`, `dept_id`, `nb_modules`, `niveau`, `effectif`, `created_at`) VALUES
(1, 'Licence Informatique', 'LIC-INFO', 1, 8, 'L3', 250, '2026-01-11 19:02:28'),
(2, 'Master Mathématiques', 'MST-MATH', 2, 9, 'M2', 120, '2026-01-11 19:02:28'),
(3, 'Licence Physique', 'LIC-PHYS', 3, 7, 'L2', 180, '2026-01-11 19:02:28'),
(4, 'Master Chimie', 'MST-CHIM', 4, 9, 'M1', 90, '2026-01-11 19:02:28'),
(5, 'Licence Biologie', 'LIC-BIO', 5, 8, 'L1', 200, '2026-01-11 19:02:28'),
(6, 'Licence Sciences Terre', 'LIC-ST', 6, 7, 'L3', 80, '2026-01-11 19:02:28'),
(7, 'Master Langues', 'MST-LL', 7, 9, 'M2', 70, '2026-01-11 19:02:28');

-- --------------------------------------------------------

--
-- Structure de la table `inscriptions`
--

CREATE TABLE `inscriptions` (
  `id` int(11) NOT NULL,
  `etudiant_id` int(11) DEFAULT NULL,
  `module_id` int(11) DEFAULT NULL,
  `annee` int(11) NOT NULL,
  `session` varchar(10) DEFAULT 'Principale',
  `note` float DEFAULT NULL,
  `statut` varchar(20) DEFAULT 'Inscrit',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `inscriptions`
--

INSERT INTO `inscriptions` (`id`, `etudiant_id`, `module_id`, `annee`, `session`, `note`, `statut`, `created_at`) VALUES
(1, 1, 1, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(2, 1, 2, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(3, 2, 1, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(4, 2, 2, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(5, 3, 3, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(6, 4, 3, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(7, 5, 4, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(8, 6, 4, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(9, 7, 5, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(10, 8, 5, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(11, 9, 6, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28'),
(12, 10, 6, 2024, 'Principale', NULL, 'Inscrit', '2026-01-11 19:02:28');

-- --------------------------------------------------------

--
-- Structure de la table `lieu_examen`
--

CREATE TABLE `lieu_examen` (
  `id` int(11) NOT NULL,
  `code` varchar(20) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `capacite` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  `batiment` varchar(50) DEFAULT NULL,
  `etage` int(11) DEFAULT NULL,
  `equipements` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`equipements`)),
  `disponibilite` tinyint(1) DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `lieu_examen`
--

INSERT INTO `lieu_examen` (`id`, `code`, `nom`, `capacite`, `type`, `batiment`, `etage`, `equipements`, `disponibilite`, `created_at`) VALUES
(1, 'AMPHI-A', 'Amphithéâtre A', 300, 'Amphi', 'Bâtiment A', 0, '[\"Vidéoprojecteur\", \"Tableau\", \"Micro\"]', 1, '2026-01-11 19:02:28'),
(2, 'AMPHI-B', 'Amphithéâtre B', 250, 'Amphi', 'Bâtiment A', 0, '[\"Vidéoprojecteur\", \"Tableau\"]', 1, '2026-01-11 19:02:28'),
(3, 'SAL-101', 'Salle 101', 100, 'Salle', 'Bâtiment B', 1, '[\"Vidéoprojecteur\", \"Tableau\"]', 1, '2026-01-11 19:02:28'),
(4, 'SAL-102', 'Salle 102', 80, 'Salle', 'Bâtiment B', 1, '[\"Tableau\"]', 1, '2026-01-11 19:02:28'),
(5, 'SAL-103', 'Salle 103', 60, 'Salle', 'Bâtiment B', 1, '[\"Vidéoprojecteur\", \"Tableau\"]', 1, '2026-01-11 19:02:28'),
(6, 'LAB-201', 'Laboratoire 201', 40, 'Laboratoire', 'Bâtiment C', 2, '[\"Ordinateurs\", \"Matériel spécialisé\"]', 1, '2026-01-11 19:02:28');

-- --------------------------------------------------------

--
-- Structure de la table `logs_connexion`
--

CREATE TABLE `logs_connexion` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `user_role` varchar(50) DEFAULT NULL,
  `matricule` varchar(20) DEFAULT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  `user_agent` text DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `reason` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `logs_optimisation`
--

CREATE TABLE `logs_optimisation` (
  `id` int(11) NOT NULL,
  `session` varchar(50) NOT NULL,
  `date_generation` datetime DEFAULT current_timestamp(),
  `temps_execution_ms` int(11) DEFAULT NULL,
  `nb_examens` int(11) DEFAULT NULL,
  `nb_conflits_initial` int(11) DEFAULT NULL,
  `nb_conflits_final` int(11) DEFAULT NULL,
  `taux_occupation_salles` float DEFAULT NULL,
  `utilisateur_id` int(11) DEFAULT NULL,
  `parametres` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`parametres`)),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `modules`
--

CREATE TABLE `modules` (
  `id` int(11) NOT NULL,
  `code` varchar(20) NOT NULL,
  `nom` varchar(150) NOT NULL,
  `credits` int(11) DEFAULT 3,
  `formation_id` int(11) DEFAULT NULL,
  `professeur_id` int(11) DEFAULT NULL,
  `pre_requis_id` int(11) DEFAULT NULL,
  `coefficient` float DEFAULT 1,
  `volume_horaire` int(11) DEFAULT 30,
  `semestre` varchar(10) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `modules`
--

INSERT INTO `modules` (`id`, `code`, `nom`, `credits`, `formation_id`, `professeur_id`, `pre_requis_id`, `coefficient`, `volume_horaire`, `semestre`, `created_at`) VALUES
(1, 'MOD001', 'Algorithmique Avancée', 6, 1, 1, NULL, 1, 30, 'S1', '2026-01-11 19:02:28'),
(2, 'MOD002', 'Base de Données', 5, 1, 2, NULL, 1, 30, 'S1', '2026-01-11 19:02:28'),
(3, 'MOD003', 'Algèbre Linéaire', 4, 2, 3, NULL, 1, 30, 'S1', '2026-01-11 19:02:28'),
(4, 'MOD004', 'Mécanique Quantique', 6, 3, 4, NULL, 1, 30, 'S2', '2026-01-11 19:02:28'),
(5, 'MOD005', 'Chimie Organique', 5, 4, 5, NULL, 1, 30, 'S1', '2026-01-11 19:02:28'),
(6, 'MOD006', 'Biologie Moléculaire', 4, 5, 6, NULL, 1, 30, 'S2', '2026-01-11 19:02:28'),
(7, 'MOD007', 'Géologie Structurale', 5, 6, 7, NULL, 1, 30, 'S1', '2026-01-11 19:02:28');

-- --------------------------------------------------------

--
-- Structure de la table `professeurs`
--

CREATE TABLE `professeurs` (
  `id` int(11) NOT NULL,
  `matricule` varchar(20) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `specialite` varchar(150) DEFAULT NULL,
  `email` varchar(150) NOT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `statut` varchar(50) DEFAULT NULL,
  `max_examens_jour` int(11) DEFAULT 3,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `professeurs`
--

INSERT INTO `professeurs` (`id`, `matricule`, `nom`, `prenom`, `dept_id`, `specialite`, `email`, `telephone`, `statut`, `max_examens_jour`, `created_at`) VALUES
(1, 'PROF001', 'Martin', 'Jean', 1, 'Algorithmique', 'j.martin@univ.edu', NULL, NULL, 3, '2026-01-11 19:02:28'),
(2, 'PROF002', 'Durand', 'Marie', 1, 'Base de Données', 'm.durand@univ.edu', NULL, NULL, 3, '2026-01-11 19:02:28'),
(3, 'PROF003', 'Dubois', 'Pierre', 2, 'Algèbre', 'p.dubois@univ.edu', NULL, NULL, 3, '2026-01-11 19:02:28'),
(4, 'PROF004', 'Leroy', 'Sophie', 3, 'Mécanique', 's.leroy@univ.edu', NULL, NULL, 3, '2026-01-11 19:02:28'),
(5, 'PROF005', 'Moreau', 'Paul', 4, 'Chimie Organique', 'p.moreau@univ.edu', NULL, NULL, 3, '2026-01-11 19:02:28'),
(6, 'PROF006', 'Simon', 'Julie', 5, 'Biologie Cellulaire', 'j.simon@univ.edu', NULL, NULL, 3, '2026-01-11 19:02:28'),
(7, 'PROF007', 'Laurent', 'Thomas', 6, 'Géologie', 't.laurent@univ.edu', NULL, NULL, 3, '2026-01-11 19:02:28');

-- --------------------------------------------------------

--
-- Structure de la table `sessions`
--

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `token` varchar(64) NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_role` varchar(50) NOT NULL,
  `user_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`user_data`)),
  `ip_address` varchar(45) DEFAULT NULL,
  `user_agent` text DEFAULT NULL,
  `active` tinyint(1) DEFAULT 1,
  `expires_at` datetime NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `last_activity` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `vue_statistiques_globales`
-- (Voir ci-dessous la vue réelle)
--
CREATE TABLE `vue_statistiques_globales` (
`total_etudiants` bigint(21)
,`total_professeurs` bigint(21)
,`total_examens` bigint(21)
,`total_salles` bigint(21)
,`capacite_moyenne_salles` decimal(14,4)
,`capacite_totale` decimal(32,0)
,`total_departements` bigint(21)
,`total_formations` bigint(21)
);

-- --------------------------------------------------------

--
-- Structure de la vue `vue_statistiques_globales`
--
DROP TABLE IF EXISTS `vue_statistiques_globales`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vue_statistiques_globales`  AS SELECT (select count(0) from `etudiants`) AS `total_etudiants`, (select count(0) from `professeurs`) AS `total_professeurs`, (select count(0) from `examens`) AS `total_examens`, (select count(0) from `lieu_examen`) AS `total_salles`, (select avg(`lieu_examen`.`capacite`) from `lieu_examen`) AS `capacite_moyenne_salles`, (select sum(`lieu_examen`.`capacite`) from `lieu_examen`) AS `capacite_totale`, (select count(0) from `departements`) AS `total_departements`, (select count(0) from `formations`) AS `total_formations` ;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `administrateurs`
--
ALTER TABLE `administrateurs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `matricule` (`matricule`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `departement_id` (`departement_id`);

--
-- Index pour la table `contraintes_speciales`
--
ALTER TABLE `contraintes_speciales`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `departements`
--
ALTER TABLE `departements`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Index pour la table `etudiants`
--
ALTER TABLE `etudiants`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `matricule` (`matricule`),
  ADD KEY `idx_etudiants_formation` (`formation_id`);

--
-- Index pour la table `examens`
--
ALTER TABLE `examens`
  ADD PRIMARY KEY (`id`),
  ADD KEY `surveillant_principal_id` (`surveillant_principal_id`),
  ADD KEY `idx_examens_date` (`date_heure`),
  ADD KEY `idx_examens_salle` (`salle_id`),
  ADD KEY `idx_examens_module` (`module_id`);

--
-- Index pour la table `exam_surveillance`
--
ALTER TABLE `exam_surveillance`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_surveillance` (`examen_id`,`professeur_id`),
  ADD KEY `professeur_id` (`professeur_id`);

--
-- Index pour la table `formations`
--
ALTER TABLE `formations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `idx_formations_dept` (`dept_id`);

--
-- Index pour la table `inscriptions`
--
ALTER TABLE `inscriptions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_inscription` (`etudiant_id`,`module_id`,`annee`,`session`),
  ADD KEY `idx_inscriptions_etudiant` (`etudiant_id`),
  ADD KEY `idx_inscriptions_module` (`module_id`);

--
-- Index pour la table `lieu_examen`
--
ALTER TABLE `lieu_examen`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Index pour la table `logs_connexion`
--
ALTER TABLE `logs_connexion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_logs_connexion_user` (`user_id`),
  ADD KEY `idx_logs_connexion_date` (`created_at`);

--
-- Index pour la table `logs_optimisation`
--
ALTER TABLE `logs_optimisation`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `modules`
--
ALTER TABLE `modules`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `pre_requis_id` (`pre_requis_id`),
  ADD KEY `idx_modules_formation` (`formation_id`),
  ADD KEY `idx_modules_professeur` (`professeur_id`);

--
-- Index pour la table `professeurs`
--
ALTER TABLE `professeurs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `matricule` (`matricule`),
  ADD KEY `idx_professeurs_dept` (`dept_id`);

--
-- Index pour la table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token` (`token`),
  ADD KEY `idx_sessions_token` (`token`),
  ADD KEY `idx_sessions_expires` (`expires_at`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `administrateurs`
--
ALTER TABLE `administrateurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `contraintes_speciales`
--
ALTER TABLE `contraintes_speciales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `departements`
--
ALTER TABLE `departements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `etudiants`
--
ALTER TABLE `etudiants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `examens`
--
ALTER TABLE `examens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `exam_surveillance`
--
ALTER TABLE `exam_surveillance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `formations`
--
ALTER TABLE `formations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `inscriptions`
--
ALTER TABLE `inscriptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `lieu_examen`
--
ALTER TABLE `lieu_examen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `logs_connexion`
--
ALTER TABLE `logs_connexion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `logs_optimisation`
--
ALTER TABLE `logs_optimisation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `modules`
--
ALTER TABLE `modules`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `professeurs`
--
ALTER TABLE `professeurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `administrateurs`
--
ALTER TABLE `administrateurs`
  ADD CONSTRAINT `administrateurs_ibfk_1` FOREIGN KEY (`departement_id`) REFERENCES `departements` (`id`) ON DELETE SET NULL;

--
-- Contraintes pour la table `etudiants`
--
ALTER TABLE `etudiants`
  ADD CONSTRAINT `etudiants_ibfk_1` FOREIGN KEY (`formation_id`) REFERENCES `formations` (`id`) ON DELETE SET NULL;

--
-- Contraintes pour la table `examens`
--
ALTER TABLE `examens`
  ADD CONSTRAINT `examens_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `modules` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `examens_ibfk_2` FOREIGN KEY (`salle_id`) REFERENCES `lieu_examen` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `examens_ibfk_3` FOREIGN KEY (`surveillant_principal_id`) REFERENCES `professeurs` (`id`) ON DELETE SET NULL;

--
-- Contraintes pour la table `exam_surveillance`
--
ALTER TABLE `exam_surveillance`
  ADD CONSTRAINT `exam_surveillance_ibfk_1` FOREIGN KEY (`examen_id`) REFERENCES `examens` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `exam_surveillance_ibfk_2` FOREIGN KEY (`professeur_id`) REFERENCES `professeurs` (`id`) ON DELETE CASCADE;

--
-- Contraintes pour la table `formations`
--
ALTER TABLE `formations`
  ADD CONSTRAINT `formations_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `departements` (`id`) ON DELETE CASCADE;

--
-- Contraintes pour la table `inscriptions`
--
ALTER TABLE `inscriptions`
  ADD CONSTRAINT `inscriptions_ibfk_1` FOREIGN KEY (`etudiant_id`) REFERENCES `etudiants` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `inscriptions_ibfk_2` FOREIGN KEY (`module_id`) REFERENCES `modules` (`id`) ON DELETE CASCADE;

--
-- Contraintes pour la table `modules`
--
ALTER TABLE `modules`
  ADD CONSTRAINT `modules_ibfk_1` FOREIGN KEY (`formation_id`) REFERENCES `formations` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `modules_ibfk_2` FOREIGN KEY (`professeur_id`) REFERENCES `professeurs` (`id`) ON DELETE SET NULL,
  ADD CONSTRAINT `modules_ibfk_3` FOREIGN KEY (`pre_requis_id`) REFERENCES `modules` (`id`) ON DELETE SET NULL;

--
-- Contraintes pour la table `professeurs`
--
ALTER TABLE `professeurs`
  ADD CONSTRAINT `professeurs_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `departements` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
