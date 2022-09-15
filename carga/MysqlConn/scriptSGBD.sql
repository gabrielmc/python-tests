-- CREATE TABLE
CREATE TABLE Carga (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    carga VARCHAR(600) NOT NULL,
    data DATE,
    status BOOLEAN NOT NULL
)

-- INSERT TABLE
INSERT INTO Carga(nome, carga, `data`, status) VALUES("gabriel teste", "lkoicaneffahsoiws987654111", NOW(), 0)
INSERT INTO Carga(nome, carga, `data`, status) VALUES('roberto teste', 'lkoicaneffahsoiws321654987', NOW(), 1);
INSERT INTO Carga(nome, carga, `data`, status) VALUES('weslay teste', 'lkoicaneffahsoiws741741741', NOW()+1, 0);
INSERT INTO Carga(nome, carga, `data`, status) VALUES('kekel teste', 'lkoicaneffahsoiasd45698777', NOW()+2, 1);