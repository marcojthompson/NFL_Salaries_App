USE NFL_PLAYER_SALARY_DATA;

CREATE TABLE IF NOT EXISTS player_cap_hits (
    player_name VARCHAR(50) NOT NULL,
    team_loc VARCHAR(3) NOT NULL,
    cap_hit VARCHAR(15) NOT NULL,
    cap_int BIGINT NOT NULL,
    PRIMARY KEY (player_name, team_loc)
);

