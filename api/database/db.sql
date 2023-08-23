/* CREATE DATABASE iF NOT EXISTS petfinderdb; */

/* \c petfinderdb; */

CREATE TABLE users(
user_id SERIAL PRIMARY KEY,
email VARCHAR(150) NOT NULL,
pass_user VARCHAR(10) NOT NULL,
country VARCHAR(3) NOT NULL
);

COMMENT ON TABLE users IS 'The users of the application';

CREATE TABLE publications_user(
publications_user_id SERIAL PRIMARY KEY,
user_id INT NOT NULL,
publication_id INT NOT NULL
);

COMMENT ON TABLE publications_user IS 'Publications of the users';

CREATE TABLE image_publication(
image_publication_id SERIAL PRIMARY KEY,
image VARCHAR(300) NOT NULL,
publication_id INT NOT NULL
);

COMMENT ON TABLE image_publication IS 'Images of the publications';

CREATE TYPE PUBLICATION_TYPE AS ENUM ('Busqueda', 'En adopción', 'Encontrada', 'Adoptada');
CREATE TABLE publications(
publication_id SERIAL PRIMARY KEY,
publication_date DATE,
pub_type PUBLICATION_TYPE,
country VARCHAR(3) NOT NULL,
city VARCHAR(100) NOT NULL,
address VARCHAR(100),
image_publication_id INT NOT NULL,
pet_id INT NOT NULL,
user_id INT NOT NULL
);

COMMENT ON TABLE publications IS 'Publications of pets';

CREATE TABLE colors_pet(
colors_pet_id SERIAL PRIMARY KEY,
color VARCHAR(15) NOT NULL,
pet_id INT NOT NULL
);

COMMENT ON TABLE colors_pet IS 'Colors of the pets';

CREATE TYPE GENRE_ENUM AS ENUM ('Macho', 'Hembra');
CREATE TYPE SIZE_ENUM AS ENUM ('Pequeña', 'Chica', 'Mediana', 'Grande');
CREATE TABLE pets(
pet_id SERIAL PRIMARY KEY,
type VARCHAR(150) NOT NULL,
name VARCHAR(100) NULL,
age INT NULL,
genre GENRE_ENUM NOT NULL,
size SIZE_ENUM NOT NULL,
breed VARCHAR(50) NULL,
eye_color VARCHAR(20) NOT NULL,
distinctive_feature TEXT NULL,
colors_pet_id INT NOT NULL,
publication_id INT NOT NULL
);

COMMENT ON TABLE pets IS 'Pets';

CREATE TABLE profile(
profile_id SERIAL PRIMARY KEY,
name VARCHAR(150) NOT NULL,
phone VARCHAR(50) NULL,
state VARCHAR(50) NULL,
province VARCHAR(100) NULL,
postal_code VARCHAR(5) NULL,
user_id INT NOT NULL
);

COMMENT ON TABLE profile IS 'User Profile';

ALTER TABLE publications_user ADD FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE publications_user ADD FOREIGN KEY (publication_id) REFERENCES publications(publication_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE image_publication ADD FOREIGN KEY (publication_id) REFERENCES publications(publication_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE publications ADD FOREIGN KEY (image_publication_id) REFERENCES image_publication(image_publication_id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE publications ADD FOREIGN KEY (pet_id) REFERENCES pets(pet_id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE publications ADD FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE colors_pet ADD FOREIGN KEY (pet_id) REFERENCES pets(pet_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE pets ADD FOREIGN KEY (colors_pet_id) REFERENCES colors_pet(colors_pet_id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE pets ADD FOREIGN KEY (publication_id) REFERENCES publications(publication_id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE profile ADD FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE RESTRICT;