INSERT INTO
    IS601_S_Items (
        id,
        name,
        description,
        category,
        stock,
        cost,
        image
    )
VALUES (
        -1,
        "Health Boost",
        "Live longer",
        "Life",
        9999999,
        10,
        ""
    ), (
        -2,
        "Agility",
        "Become the flash",
        "Skill",
        9999999,
        15,
        ""
    ), (
        -3,
        "Quick Shot",
        "More pew pew",
        "Amo",
        9999999,
        5,
        ""
    ), (
        -4,
        "Large Caliber",
        "One shot wonder",
        "Amo",
        9999999,
        20,
        ""
    ), (
        -5,
        "Vaccuum",
        "Channel your inner Kirby",
        "Skill",
        9999999,
        1,
        ""
    ) ON DUPLICATE KEY
UPDATE
    modified = CURRENT_TIMESTAMP()