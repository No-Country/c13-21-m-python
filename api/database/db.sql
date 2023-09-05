CREATE DATABASE iF NOT EXISTS dbpetfinder;

CREATE TABLE users(
id SERIAL PRIMARY KEY,
email VARCHAR(150) NOT NULL,
pass_user VARCHAR(250) NOT NULL,
country VARCHAR(3) NOT NULL,
is_Active BOOLEAN DEFAULT true,
publication_id INT NOT NULL
);

COMMENT ON TABLE users IS 'The users of the application';

CREATE TABLE image_publication(
id SERIAL PRIMARY KEY,
image VARCHAR(100) NOT NULL,
url VARCHAR(200) NOT NULL,
publication_id INT NOT NULL
);

COMMENT ON TABLE image_publication IS 'Images of the publications';

CREATE TABLE publications(
id SERIAL PRIMARY KEY,
publication_date DATE,
pub_type VARCHAR(11),
city VARCHAR(100) NOT NULL,
address VARCHAR(100),
status VARCHAR(7) DEFAULT 'OPEN'
);

COMMENT ON TABLE publications IS 'Publications of pets';

CREATE TABLE pets(
id SERIAL PRIMARY KEY,
type VARCHAR(20) NOT NULL,
name VARCHAR(100) NULL,
age INT NULL,
genre VARCHAR(6) NOT NULL,
size VARCHAR(7) NOT NULL,
breed VARCHAR(50) NULL,
eye_color VARCHAR(8) NOT NULL,
description TEXT NULL,
fur VARCHAR(10) NULL,
necklace BOOLEAN DEFAULT true,
color VARCHAR(8) NOT NULL,
publication_id INT NOT NULL
);

COMMENT ON TABLE pets IS 'Pets';

CREATE TABLE profile(
id SERIAL PRIMARY KEY,
name VARCHAR(150) NULL,
phone VARCHAR(50) NULL,
state VARCHAR(50) NULL,
province VARCHAR(100) NULL,
postal_code VARCHAR(10) NULL,
user_id INT NOT NULL
);

COMMENT ON TABLE profile IS 'User Profile';

ALTER TABLE pets ADD FOREIGN KEY (publication_id) REFERENCES publications(id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE users ADD FOREIGN KEY (publication_id) REFERENCES publications(id) ON UPDATE CASCADE ON DELETE RESTRICT;
ALTER TABLE image_publication ADD FOREIGN KEY (publication_id) REFERENCES publications(id) ON UPDATE CASCADE ON DELETE RESTRICT;

ALTER TABLE profile ADD FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE RESTRICT;