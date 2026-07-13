-- Runs automatically the first time the "db" container starts with an empty
-- data volume (see docker-compose.yml). If you need to re-run this after
-- changing it, use `make up-clean` to reset the database volume first.

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id VARCHAR(64) NOT NULL PRIMARY KEY,
    property_id VARCHAR(3) NOT NULL,
    arrival DATE NOT NULL,
    departure DATE NOT NULL,
    adults INT NOT NULL DEFAULT 0,
    children INT NOT NULL DEFAULT 0,
    status VARCHAR(32) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
