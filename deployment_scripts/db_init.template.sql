DROP DATABASE IF EXISTS <database.name>;
CREATE DATABASE <database.name>;
\c <database.name>
DROP USER IF EXISTS <database.user>;
CREATE USER <database.user> WITH PASSWORD '<database.password>';
ALTER ROLE <database.user> SET client_encoding TO 'utf8';
ALTER ROLE <database.user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <database.user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database.name> TO <database.user>;
GRANT ALL ON SCHEMA public TO <database.user>;