-- CREATE TABLE
--Carga
CREATE TABLE dbaseTest.Carga (
    id          SERIAL NOT NULL,
    nome        VARCHAR(200) NULL,
    carga       VARCHAR(300) NULL,
    status      boolean NULL,
    data        Date NOT NULL,
    PRIMARY KEY (id)
) WITH ( OIDS=FALSE );

ALTER TABLE dbaseTest.Carga OWNER TO postgres;
GRANT ALL ON TABLE dbaseTest.Carga TO postgres;

-- INSERT TABLE
INSERT INTO dbaseTest.Carga(id, nome, carga, data, status) VALUES
    (1, 'Gabriel TESTE', '596845oijhdej-SATELE-10', '2017-03-28', 0),
    (2, 'Wesley TESTE', '05552965oijhdej-SATELE-1', '2020-05-10', 0),
    (3, 'Roberto TESTE', '562785oijhdej-SATELE-5', '2021-06-18', 1),
    (4, 'Lucas TESTE', '88416895lojdddej-SATELE-1', '2021-09-19', 1),
    (5, 'Marta TESTE', '4551115oijhdej-SATELE-9', '2021-07-19', 0),
    (5, 'Silvana TESTE', '455115oijhdej-SATELE-8', '2021-07-19', 0);