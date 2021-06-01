DROP TABLE IF EXISTS Examens;
DROP TABLE IF EXISTS Etudiants;
DROP TABLE IF EXISTS Promotions;
DROP TABLE IF EXISTS Professeurs;
DROP TABLE IF EXISTS Cours;

PRAGMA FOREIGN_KEYS=ON;


CREATE TABLE Promotions (
		promo INTEGER NOT NULL,
		parcours TEXT NOT NULL,
		CONSTRAINT pk_prom_promo PRIMARY KEY  (promo)
		CONSTRAINT ck_prom_parcours CHECK ((parcours) IN ("INF", "INF+ges"))
);

CREATE TABLE  Etudiants (
		numero INTEGER NOT NULL,
		nom TEXT NOT NULL,
		prenom TEXT NOT NULL,
		promo TEXT NOT NULL,
		CONSTRAINT pk_etu_numero PRIMARY KEY (numero),
		CONSTRAINT fk_etu_promo FOREIGN KEY (promo) REFERENCES Promotions (promo)
);

CREATE TABLE Cours (
		matiere TEXT NOT NULL,
		credits INTEGER NOT NULL,
		CONSTRAINT pk_cours_matiere PRIMARY KEY  (matiere),
		CONSTRAINT ck_cours_credits CHECK (0<credits<7)
);

CREATE TABLE Examens (
		date_exam DATE,
		promo INTEGER NOT NULL,
		matiere TEXT NOT NULL,
		CONSTRAINT pk_exa_date PRIMARY KEY (date_exam),
		CONSTRAINT fk_exa_promo FOREIGN KEY (promo) REFERENCES Promotions (promo),
		CONSTRAINT fk_exa_matiere FOREIGN KEY (matiere) REFERENCES Cours (matiere)
);

CREATE TABLE Professeurs (
		nom TEXT NOT NULL,
		prenom TEXT NOT NULL,
		matiere TEXT NOT NULL,
		CONSTRAINT pk_prof_nom PRIMARY KEY (nom),
		CONSTRAINT fk_prof_matiere FOREIGN KEY (matiere) REFERENCES Cours (matiere)
);














		
		