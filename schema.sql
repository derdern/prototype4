--DROP TABLE IF EXISTS tbl_add_user_data;
--DROP TABLE IF EXISTS post;

CREATE TABLE tbl_add_user_data (
  --id INTEGER PRIMARY KEY AUTOINCREMENT,
  --created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  age TEXT,
  gender TEXT
);

/*CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);*/