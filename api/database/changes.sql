DROP TABLE publications_user;
ALTER TABLE profile RENAME COLUMN province TO address;
ALTER TABLE profile ALTER COLUMN postal_code TYPE VARCHAR(10);
ALTER TABLE publications ALTER COLUMN pub_type TYPE VARCHAR(11);
ALTER TABLE image_publication ADD COLUMN url VARCHAR(200);
ALTER TABLE image_publication ALTER COLUMN image TYPE VARCHAR(100);
ALTER TABLE publications RENAME COLUMN publication_id TO id;
ALTER TABLE image_publication RENAME image_publication_id TO id;
ALTER TABLE colors_pet RENAME colors_pet_id TO id;
ALTER TABLE pets RENAME pet_id TO id;
ALTER TABLE profile RENAME profile_id TO id;
ALTER TABLE users RENAME user_id TO id;
ALTER TABLE publications ADD COLUMN status VARCHAR(7);

update publications set status = 'OPEN' where id in (1,2,4,5);
update publications set status = 'CLOSE' where id in (3,6,7);
update image_publication set url='https://fotos-petfinder-c13-21-m.s3.us-west-1.amazonaws.com/fotos/8202023-08-30090717494535-siames.jpg' where id=4;
update image_publication set url='https://fotos-petfinder-c13-21-m.s3.us-west-1.amazonaws.com/fotos/82002023-08-30100020567957-french.jpg' where id in (6,7);

ALTER TABLE pets ADD COLUMN fur VARCHAR(10);
ALTER TABLE pets ADD COLUMN necklace BOOLEAN DEFAULT true;

update publications set pub_type='perdidos' where id in (1,2,4);
update publications set pub_type='adoptados' where id in (6,7);
update publications set pub_type='encontrados' where id =3;
update publications set pub_type='disponibles' where id =5;

ALTER TABLE profile ALTER COLUMN name DROP NOT NULL;
ALTER TABLE profile RENAME COLUMN address TO province;

ALTER TABLE users DROP COLUMN pass_user;