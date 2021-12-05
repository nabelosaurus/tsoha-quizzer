CREATE TABLE competition (
    id integer NOT NULL,
    user_id integer NOT NULL,
    quiz_id integer NOT NULL,
    date timestamp without time zone NOT NULL,
    score integer NOT NULL
);

CREATE SEQUENCE competition_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE competition_id_seq OWNED BY competition.id;

CREATE TABLE question (
    id integer NOT NULL,
    question character varying(200) NOT NULL,
    answer character varying(50) NOT NULL,
    quiz_id integer NOT NULL
);

CREATE SEQUENCE question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE question_id_seq OWNED BY question.id;


CREATE TABLE quiz (
    id integer NOT NULL,
    date timestamp without time zone NOT NULL
);


CREATE SEQUENCE quiz_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE quiz_id_seq OWNED BY quiz.id;

CREATE TABLE "user" (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(200) NOT NULL,
    password character varying(200) NOT NULL,
    is_admin integer NOT NULL
);

CREATE SEQUENCE user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE user_id_seq OWNED BY "user".id;


CREATE TABLE users (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(200) NOT NULL,
    password character varying(200) NOT NULL,
    is_admin integer NOT NULL
);


CREATE SEQUENCE users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE users_id_seq OWNED BY users.id;


ALTER TABLE ONLY competition ALTER COLUMN id SET DEFAULT nextval('competition_id_seq'::regclass);


ALTER TABLE ONLY question ALTER COLUMN id SET DEFAULT nextval('question_id_seq'::regclass);


ALTER TABLE ONLY quiz ALTER COLUMN id SET DEFAULT nextval('quiz_id_seq'::regclass);


ALTER TABLE ONLY "user" ALTER COLUMN id SET DEFAULT nextval('user_id_seq'::regclass);


ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


ALTER TABLE ONLY competition
    ADD CONSTRAINT competition_pkey PRIMARY KEY (id);


ALTER TABLE ONLY question
    ADD CONSTRAINT question_pkey PRIMARY KEY (id);


ALTER TABLE ONLY quiz
    ADD CONSTRAINT quiz_pkey PRIMARY KEY (id);


ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


ALTER TABLE ONLY "user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


ALTER TABLE ONLY users
    ADD CONSTRAINT users_email_key UNIQUE (email);


ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


ALTER TABLE ONLY users
    ADD CONSTRAINT users_username_key UNIQUE (username);


ALTER TABLE ONLY competition
    ADD CONSTRAINT competition_quiz_id_fkey FOREIGN KEY (quiz_id) REFERENCES quiz(id);


ALTER TABLE ONLY competition
    ADD CONSTRAINT competition_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id);


ALTER TABLE ONLY question
    ADD CONSTRAINT question_quiz_id_fkey FOREIGN KEY (quiz_id) REFERENCES quiz(id);