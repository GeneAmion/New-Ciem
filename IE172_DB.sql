CREATE TABLE user_account (
	account_id serial PRIMARY KEY,
	user_name varchar (8) NOT NULL,
	account_password varchar(32) NOT NULL,
	user_account_delete bool
);

CREATE TABLE person (
	valid_id varchar(50) PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	middle_name varchar(50),
	last_name varchar(50) NOT NULL,
	suffix varchar(10),
	birthdate date NOT NULL,
	contact_number varchar(11) NOT NULL,
	emergency_contact_number varchar(11) NOT NULL,
	email varchar(100) NOT NULL,
	present_address varchar(512) NOT NULL,
	permanent_address varchar(512) NOT NULL,
	account_id int,
	person_delete bool,

	CONSTRAINT person_account_id_fkey FOREIGN KEY (account_id)
		REFERENCES user_account(account_id)
);

CREATE TABLE manager (
	manager_id serial PRIMARY KEY,
	acad_year varchar(512),	
	valid_id varchar(50),
	manager_delete bool,
	CONSTRAINT manager_valid_id_fkey FOREIGN KEY (valid_id)
		REFERENCES person(valid_id)
	
);

CREATE TABLE affiliation (
	affiliation_id serial PRIMARY KEY, 
	member_id varchar(10),
	membership_type varchar(50),
	app_batch varchar(50),
	year_standing int,
	degree_program varchar(50),
	other_org_affiliation varchar(512),
	comm_firstchoice varchar(512) ,
	comm_secondchoice varchar(512),
	comm_thirdchoice varchar(512),
	comm_fourthchoice varchar(512),
	comm_fifthchoice varchar(512),
	comm_sixthchoice varchar(512),
	adhoc_firstchoice varchar(512) ,
	adhoc_secondchoice varchar(512),
	adhoc_thirdchoice varchar(512),
	adhoc_fourthchoice varchar(512),
	adhoc_fifthchoice varchar(512),
	adhoc_sixthchoice varchar(512),
	adhoc_seventhchoice varchar(512),
	gwa varchar(512),
	reaff_fee varchar(512),
	manager_id int,
	valid_id varchar(50),
	affiliation_delete bool,
	
	CONSTRAINT affiliation_manager_id_fkey FOREIGN KEY (manager_id)
		REFERENCES manager(manager_id),
	CONSTRAINT affiliation_valid_id_fkey FOREIGN KEY (valid_id)
		REFERENCES person(valid_id)

);

CREATE TABLE status (
	status_id serial PRIMARY KEY,
	status_date timestamp DEFAULT CURRENT_TIMESTAMP, 
	account_id int,
	manager_id int,
	status_name varchar(512),
	status_delete bool,
	
	CONSTRAINT status_account_id_fkey FOREIGN KEY (account_id) 
		REFERENCES user_account(account_id),
	CONSTRAINT status_manager_id_fkey FOREIGN KEY (manager_id) 
		REFERENCES manager(manager_id)
);

CREATE TABLE committee (
	committee_id serial PRIMARY KEY,
	committee_name varchar(512),
	guide_book varchar(512),
	projects varchar(512) NOT NULL,
	core_team varchar(512) NOT NULL,
	committee_delete bool
);

CREATE TABLE UPCIEM_Member (
	UPCIEM_Member_id serial PRIMARY KEY,
	active_status varchar(512),
 	valid_id varchar(10),
	affiliation_id int,
	Committee_id int,
	UPCIEM_Member_delete bool,
	
	CONSTRAINT UPCIEM_Member_valid_id_fkey FOREIGN KEY (valid_id)
		REFERENCES person(valid_id),
	CONSTRAINT UPCIEM_Member_affiliation_id_fkey FOREIGN KEY (affiliation_id)
		REFERENCES affiliation(affiliation_id),
	CONSTRAINT UPCIEM_Member_committee_id_fkey FOREIGN KEY (committee_id)
		REFERENCES committee(committee_id)
);



CREATE TABLE project_headship (
	headship_id serial PRIMARY KEY,
	headship_name varchar (512),
	comm_proj varchar(512) NOT NULL,
	adhoc_comm varchar(512) NOT NULL,
	project_headship_delete bool
);


CREATE TABLE performance (
	performance_id serial PRIMARY KEY,
	UPCIEM_Member_id int,
	committee_id int,
	headship_id int,
	evaluation varchar(255),
	performance_delete bool,

	CONSTRAINT performance_UPCIEM_Member_id_fkey FOREIGN KEY (UPCIEM_Member_id)
		REFERENCES UPCIEM_Member(UPCIEM_Member_id),
	CONSTRAINT performance_committee_id_fkey FOREIGN KEY (committee_id)
		REFERENCES committee(committee_id),
	CONSTRAINT performance_headship_id_fkey FOREIGN KEY (headship_id)
		REFERENCES project_headship(headship_id)
);

CREATE TABLE alumni (
	alumni_id varchar(10) PRIMARY KEY, 
	specialization varchar(512) NOT NULL,
	valid_id varchar(10),
	alumni_remarks varchar(512),
	alumni_delete bool,
	
	CONSTRAINT alumni_valid_id_fkey FOREIGN KEY (valid_id)
		REFERENCES person(valid_id)
);

ALTER TABLE affiliation ADD COLUMN is_new BOOLEAN DEFAULT False;
