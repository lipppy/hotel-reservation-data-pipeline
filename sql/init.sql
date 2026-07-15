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

-- Seeds 100 random reservations each for BER, VIE and MUC, with arrivals
-- spread across May-July 2026, so the dashboard's demo hotel codes have data
-- to show without waiting on the live Apaleo pipeline.
DELIMITER $$

CREATE PROCEDURE seed_demo_reservations()
BEGIN
    DECLARE property_index INT DEFAULT 0;
    DECLARE reservation_index INT;
    DECLARE property_code VARCHAR(3);
    DECLARE arrival_date DATE;
    DECLARE departure_date DATE;

    WHILE property_index < 3 DO
        SET property_code = ELT(property_index + 1, 'BER', 'VIE', 'MUC');
        SET reservation_index = 1;

        WHILE reservation_index <= 100 DO
            -- 2026-05-01 plus 0-91 days lands anywhere in May, June or July 2026.
            SET arrival_date = DATE_ADD('2026-05-01', INTERVAL FLOOR(RAND() * 92) DAY);
            SET departure_date = DATE_ADD(arrival_date, INTERVAL (1 + FLOOR(RAND() * 7)) DAY);

            INSERT INTO reservations
                (reservation_id, property_id, arrival, departure, adults, children, status)
            VALUES (
                CONCAT('RES-', property_code, '-', LPAD(reservation_index, 3, '0')),
                property_code,
                arrival_date,
                departure_date,
                1 + FLOOR(RAND() * 4),
                FLOOR(RAND() * 3),
                ELT(1 + FLOOR(RAND() * 5), 'Confirmed', 'InHouse', 'CheckedOut', 'Canceled', 'NoShow')
            );

            SET reservation_index = reservation_index + 1;
        END WHILE;

        SET property_index = property_index + 1;
    END WHILE;
END$$

DELIMITER ;

CALL seed_demo_reservations();
DROP PROCEDURE seed_demo_reservations;
