-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 18/12/2024 às 19:05
-- Versão do servidor: 8.3.0
-- Versão do PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `apirest`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

DROP TABLE IF EXISTS `produto`;
CREATE TABLE IF NOT EXISTS `produto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_interno` varchar(150) NOT NULL,
  `nome_externo` varchar(150) NOT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  `fabricante` varchar(50) DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `produto`
--

INSERT INTO `produto` (`id`, `nome_interno`, `nome_externo`, `descricao`, `fabricante`, `ativo`) VALUES
(1, 'coca-cola', 'Coca-Cola', 'Refrigerante carbonato', 'The Coca-Cola Company', 1),
(12, 'fanta', 'Fanta', 'Refrigerante de sabores variados', 'The Coca-Cola Company', 1),
(9, 'sprite', 'Sprite', 'Refrigerante de limão', 'The Coca-Cola Company', 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `sku`
--

DROP TABLE IF EXISTS `sku`;
CREATE TABLE IF NOT EXISTS `sku` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cod` char(13) DEFAULT NULL,
  `nome` varchar(50) NOT NULL,
  `estoque` int NOT NULL,
  `preco_tab` float(8,2) NOT NULL,
  `preco_lis` float(8,2) DEFAULT NULL,
  `id_produto` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cod` (`cod`),
  KEY `id_produto` (`id_produto`)
) ENGINE=MyISAM AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `sku`
--

INSERT INTO `sku` (`id`, `cod`, `nome`, `estoque`, `preco_tab`, `preco_lis`, `id_produto`) VALUES
(1, '1530578000014', 'CC-2ML-NOR', 130, 4.50, 2.80, 1),
(2, '1530578000021', 'CC-5ML-NOR', 80, 6.00, 5.20, 1),
(3, '1530578000038', 'CC-10ML-NOR', 54, 14.00, 8.00, 1),
(4, '1530578000076', 'CC-2ML-ZER', 100, 4.50, 2.80, 1),
(5, '1530578000083', 'CC-5ML-ZER', 60, 6.00, 5.20, 1),
(6, '1530578000090', 'CC-10ML-ZER', 20, 14.00, 8.00, 1),
(7, '1530578000040', 'SP-2ML-NOR', 115, 4.50, 2.80, 9),
(8, '1530578000052', 'SP-5ML-NOR', 75, 6.00, 5.20, 9),
(9, '1530578000069', 'SP-10ML-NOR', 20, 14.00, 8.00, 9),
(10, '1530578000106', 'SP-2ML-ZER', 92, 4.50, 2.80, 9),
(11, '1530578000113', 'SP-5ML-ZER', 51, 6.00, 5.20, 9),
(12, '1530578000120', 'SP-10ML-ZER', 7, 14.00, 8.00, 9),
(14, '1530578000137', 'FN-UVA-2ML', 71, 4.50, 2.80, 12),
(15, '1530578000144', 'FN-UVA-5ML', 32, 6.00, 5.20, 12),
(16, '1530578000151', 'FN-UVA-10ML', 9, 14.00, 8.00, 12),
(17, '1530578000168', 'FN-LAR-2ML', 70, 4.50, 2.80, 12),
(18, '1530578000175', 'FN-LAR-5ML', 24, 6.00, 5.20, 12),
(19, '1530578000182', 'FN-LAR-10ML', 12, 14.00, 8.00, 12),
(20, '1530578000199', 'FN-CAJ-2ML', 21, 4.50, 2.80, 12),
(21, '1530578000205', 'FN-CAJ-5ML', 14, 6.00, 5.20, 12),
(22, '1530578000212', 'FN-CAJ-10ML', 2, 14.00, 8.00, 12);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
