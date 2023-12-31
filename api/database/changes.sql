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
update publications set status = 'CLOSE' where id in (3,6);
update image_publication set url='https://fotos-petfinder-c13-21-m.s3.us-west-1.amazonaws.com/fotos/8202023-08-30090717494535-siames.jpg' where id=4;
update image_publication set url='https://fotos-petfinder-c13-21-m.s3.us-west-1.amazonaws.com/fotos/82002023-08-30100020567957-french.jpg' where id in (6,7);

ALTER TABLE pets ADD COLUMN fur VARCHAR(10);
ALTER TABLE pets ADD COLUMN necklace BOOLEAN DEFAULT true;

update publications set pub_type='perdidos' where id in (1,2,4);
update publications set pub_type='adoptados' where id = 6 ;
update publications set pub_type='encontrados' where id =3;
update publications set pub_type='disponibles' where id =5;

ALTER TABLE profile ALTER COLUMN name DROP NOT NULL;
ALTER TABLE profile RENAME COLUMN address TO province;

ALTER TABLE access_tokens ADD COLUMN expiration_date TIMESTAMP;

ALTER TABLE users DROP COLUMN publication_id;
ALTER TABLE publications ADD COLUMN name VARCHAR(200);
ALTER TABLE publications ADD COLUMN phone VARCHAR(16);

update publications set name='Ramon Gutierrez' where id=1;
update publications set name='Laura Cordoba' where id=2;
update publications set name='Pedro Enriquez' where id=3;
update publications set name='Leticia Samano' where id=4;
update publications set name='Julieta Dominguez' where id=5;
update publications set name='Ernesto Alacantara' where id=6;
update publications set phone='+525556783734' where id=1;
update publications set phone='+525545672100' where id=2;
update publications set phone='+525534002167' where id=3;
update publications set phone='+541123900056' where id=4;
update publications set phone='+541110280641' where id=5;
update publications set phone='+541129260739' where id=6;

update publications set status = 'OPEN' where id in (1,2,4,5);
update publications set status = 'CLOSE' where id in (3,6);

update publications set pub_type='perdidos' where id in (1,2,4);
update publications set pub_type='adoptados' where id = 6 ;
update publications set pub_type='encontrados' where id =3;
update publications set pub_type='disponibles' where id =5;

update publications set phone='+541110280641' where id=5;

ALTER TABLE publications ALTER COLUMN phone TYPE VARCHAR(30);
