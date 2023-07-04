CREATE DATABASE VotaDB;

CREATE TABLE grupo (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255)
);

CREATE TABLE aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    senha VARCHAR(255),
    idgrupo INT,
    FOREIGN KEY (idgrupo) REFERENCES grupo(ID)
);
INSERT INTO GRUPO (nome) VALUES
('PATA7'),
('SQUAD DA QUEBRADA'),
('MANGO JOE'),
('SONECA');

CREATE TABLE votacao_app_vt (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  id_aluno BIGINT,
  id_grupo BIGINT,
  UNIQUE KEY (id_aluno),
  FOREIGN KEY (id_aluno) REFERENCES votacao_app_aluno(id),
  FOREIGN KEY (id_grupo) REFERENCES votacao_app_grupo(id)
);

INSERT INTO votacao_app_aluno (id, nome, email, codigo, grupo_id)
VALUES
(1, 'FERNANDO JUNIO SANTOS', 'fnandojrs@gmail.com', '0000', 1),
(2, 'MIGUEL MELO MUNIS', 'miguelmelomunis3@gmail.com', '0000', 1),
(3, 'DOUGLAS K.R. DA SILVA', 'drrds1996@gmail.com', '0000', 1),
(4, 'ANA LUIZA PAIVA SANTANA', 'analupaivasantana@gmail.com', '0000', 1),
(5, 'VALQUIRIA DA SILVA MARTINS', 'valquiriasilvamartinss@gmail.com', '0000', 1),
(6, 'VANESSA MARIA CAMARGOS', 'vm549674@gmail.com', '0000', 1),
(7, 'TAYNÁ CRISTINA DA SILVA', 'taah.criss@gmail.com', '0000', 4),
(8, 'ANA VITORIA GONTIJO', 'anaglgontijo@gmail.com', '0000', 4),
(9, 'UARLES LEMES DOS SANTOS', 'uarleslemesmkt21@gmail.com', '0000', 4),
(10, 'GABRIEL MOREIRA ROSA', 'gabrielmrdev@gmail.com', '0000', 4),
(11, 'KLIGER GUEDES SOARES LOPES', 'kligerguedessoares@gmail.com', '0000', 2),
(12, 'LUCAS TEIXEIRA SANTOS', 'lucastsantos14@gmail.com', '0000', 2),
(13, 'ANTONIO CLERIO DAS CHAGAS', 'clerioch@gmail.com', '0000', 2),
(14, 'GUSTAVO LUIS H. DOS SANTOS', 'gustavoluish.santos@gmail.com', '0000', 2),
(15, 'BRUNO HENRIQUE CERQUEIRA', 'bruno.dg2@gmail.com', '0000', 3),
(16, 'LINDAMARA M. COSTA', 'lindacosta020895@gmail.com', '0000', 2),
(17, 'KAYQUE DA SILVA OLIVEIRA', 'kayquesgp@gmail.com', '0000', 2),
(18, 'GUILHERME SANTOS LIMA', 'guilhermesemusa@gmail.com', '0000', 3),
(19, 'PEDRO HENRIQUE DA SILVA DURAO', 'pedroduraes77@gmail.com', '0000', 3),
(20, 'JOAO PAULO B. DE SALES VAZ', 'joaobvaz@outlook.com', '0000', 3),
(21, 'TULIO B. FERREIRA', 'tuliobf27@gmail.com', '0000', 3),
(22, 'RINALDO VIEIRA CAMPOS', 'rinaldovc80@bol.com.br', '0000', 4),
(23, 'DANIELA A. N.R. CORDEIRO', 'danielanevescordeiro@gmail.com', '0000', 4);


###########  trigger para o aluno nao votar no seu proprio grupo 

DELIMITER //

CREATE TRIGGER trg_check_id_aluno_id_grupo
BEFORE INSERT ON votacao_app_vt
FOR EACH ROW
BEGIN
    DECLARE aluno_grupo_id INT;
    
    SELECT grupo_id INTO aluno_grupo_id
    FROM votacao_app_aluno
    WHERE id = NEW.id_aluno;
    
    IF NEW.id_grupo = aluno_grupo_id THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'O aluno não pode votar no seu proprio grupo.';
    END IF;
END;
//

DELIMITER ;

############ fim trigger


############ alguns comandos para a tabela votacao
SELECT * FROM u751391022_votacao.votacao_app_vt;

delete FROM u751391022_votacao.votacao_app_vt where id > 0;

###########  zerar incremente tabela 
ALTER TABLE votacao_app_vt AUTO_INCREMENT = 1;




