query = """SELECT p.address, p.city, s.name as estado, p.price,
            p.description FROM property p
            LEFT JOIN status_history sh  on (sh.property_id = p.id)
            LEFT JOIN status s  on (s.id  = sh.status_id)
            WHERE s.id in (3, 4, 5)
            AND p.description IS NOT NULL AND p.description <> ''
            AND p.address IS NOT NULL AND  p.address <> ''
            AND p.city IS NOT NULL AND p.city <> ''
            AND p.`year` IS NOT NULL AND p.`year` <> ''
            AND p.price IS NOT NULL AND p.price > 0
        """