DROP TABLE publications_user;
ALTER TABLE profile RENAME COLUMN province TO address;
ALTER TABLE profile ALTER COLUMN postal_code TYPE VARCHAR(10);
ALTER TABLE publications ALTER COLUMN pub_type TYPE VARCHAR(11);