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

INSERT INTO user_account(user_name, account_password)
VALUES
	('ciem1976', 'CIEMBak1976'),
	('user0001', '1234b'),
	('user0002','1234c'),
	('user0003','1234d'),
	('user0004','1234e'),
	('user0005','1234f'),
	('user0006','1234g'),
	('user0007','1234h'),
	('user0008','1234i'),
	('user0009','1234j'),
	('user0010','1234k'),
	('user0011','1234l'),
	('user0012','1234m'),
	('user0013','1234n'),
	('user0014','1234o'),
	('user0015','1234p'),
	('user0016','1234q'),
	('user0017','1234r'),
	('user0018','1234s'),
	('user0019','1234t');



INSERT INTO person (valid_id, first_name, middle_name, last_name, suffix, birthdate, contact_number, emergency_contact_number, email, present_address, permanent_address, account_id)
VALUES
	('123456789a',	'Taylor',	'Alison',	'Swift', '',	'1999-12-13',	'09201912139',	'09291912139',	'taswift@gmail.com',	'Acacia Residence Hall, UP Diliman',	'Taguig City','1'),
	('123456789b',	'Taehyung','',	'Kim','', '2000-12-30',	'09202012305',	'09292012305',	'tkim@gmail.com',	'Kalayaan Residence Hall, UP Diliman',	'Makati City', '2'),
	('123456789c',	'Selena Marie',	'Cruz',	'Gomez','',	'2000-07-22',	'09202007222',	'09212007222',	'scgomez@gmail.com',	'Acacia Residence Hall, UP Diliman',	'Taguig City', '3'),
	('123456789d',	'Kathryn Chandria',	'Manuel',	'Bernardo',	'',	'2001-03-26',	'09202132696',	'09123456789',	'kmbernardo@gmail.com',	'Blue Residences, Katipunan',	'Makati City', '4'),
	('123456789e',	'Margot',	'Robbie',	'Fernandez', '', '2002-07-02',	'09202170290',	'09098456389',	'mrfernandez@gmail.com',	'Sampaguita Residence Hall, UP Diliman',	'Cebu City, Cebu', '5'),
	('123456789p',	'Kylie Jenna',	'Manalo',	'Jimenez', '',	'2002-08-10',	'09202110107',	'09456453109',	'kmjimenez@gmail.com',	'Guava Hills, Quezon City',	'Same as Present Address', '6'),
	('123456789q',	'Elizabeth Hope',	'Magsaysay',	'Soberano', '',	'2001-01-04',	'09202110498',	'09567000879',	'emsoberano@gmail.com',	'Krus na Ligas, Quezon City',	'Makati City', '7'),
	('123456789r',	'Enrique',	'Bacay',	'Gil',	'',	'2001-03-30',	'09202033002',	'09678000689',	'ebgil@gmail.com',	'Yakal Residence Hall, UP Diliman',	'Legazpi City, Albay', '8'),
	('123456789s',	'Dwayne Johnson',	'Sarmiento',	'Dela Cruz',	'',	'1999-05-02',	'09201952972',	'09111675889',	'dsdelacruz@gmail.com',	'Capitol Hills Drive, Quezon City',	'Cavite City', '9'),
	('123456789t',	'Jackie Chance',	'',	'Chua',	'',	'2000-04-17',	'09202004754',	'09210076890',	'jcchua@gmail.com',	'Cubao, Quezon City',	'Same as Present Address', '10'),
	('123456789f',	'Stephen Hawk',	'Ramos',	'Hernandez',	'',	'1999-01-08',	'09201918942',	'09989976753',	'srhernandez@gmail.com',	'Krus na Ligas, Quezon City',	'Laguna Province','11'),
	('123456789g',	'Anthony Starks', '',	'Reyes', '', '2000-05-29',	'09202052970',	'09112567899',	'asreyes@gmail.com',	'Taguig City',	'Same as Present Address', '12'),
	('123456789h',	'Ryan Bryan',	'Cabasag',	'Reynolds',	'',	'1999-10-23',	'09202010236',	'0977892076',	'rcreynolds@gmail.com',	'Makati City',	'Same as Present Address', '13'),
	('123456789i',	'Harry James',	'Torres',	'Potter',	'',	'2002-07-31',	'09202107310',	'09789002637',	'htpotter@gmail.com',	'Cubao, Quezon City',	'Same as Present Address', '14'),
	('123456789j',	'Trisha Ann',	'Mariano',	'Adamson',	'',	'2002-02-01',	'09369541995',	'09562788009',	'taadam@gmail.com',	'Acacia Estates, Taguig City', 'Same as Present Address', '15'),
	('123456789k',	'Ronald Weasle',	'Torres',	'Sanchez',	'',	'2001-03-01',	'09776289003',	'09990088776',	'rtsanchez@gmail.com',	'Caloocan City',	'Same as Present Address', '16'),
	('123456789l',	'Hermione Gail',	'Templo',	'Balagtas',	'',	'2002-09-19',	'09202191979',	'09112300989',	'htbalagtas@gmail.com',	'Lipa City, Batangas',	'Same as Present Address', '17'),
	('123456789m',	'Olivia Isabel',	'',	'Rodrigo',	'',	'2001-02-20',	'09202122003',	'09119920397',	'orodrigo@gmail.com',	'Kalayaan Residence Hall, UP Diliman',	'Cebu City, Cebu', '18'),
	('123456789n',	'Justin Ymanuel',	'Pabale',	'Chua',	'',	'2002-01-09',	'09328903102',	'09112983390',	'jypchua@gmail.com',	'San Pedro, Laguna',	'Same as Present Address', '19'),
	('123456789o',	'Rose Mei',	'Limcauco',	'Lee',	'',	'2002-11-06',	'09112899304',	'09902037556',	'rllee@gmail.com',	'Blue Residences, Katipunan',	'Baguio City','20');

INSERT INTO manager (acad_year, valid_id)
VALUES
	('AY 2023-2024','123456789o');

INSERT INTO affiliation (member_id, membership_type, app_batch, year_standing, Degree_Program, other_org_affiliation, comm_firstchoice, comm_secondchoice, comm_thirdchoice, comm_fourthchoice, comm_fifthchoice, comm_sixthchoice, adhoc_firstchoice , adhoc_secondchoice, adhoc_thirdchoice, adhoc_fourthchoice, adhoc_fifthchoice, adhoc_sixthchoice, adhoc_seventhchoice, gwa, reaff_fee, manager_id, valid_id)

VALUES
	('2019-12139',	'Regular',	'19A - LabingCIEM: Kaya 19 to',	'4',	'BS Industrial Engineering',	'UP Choir',	'External Affairs Committee',	'Internal Affairs Committee',	'Academic Affairs Committee',	'Publications and Records Committee',	'Finance Committee',	'Membership and Recruitment Committee','Creatives', 'Documentation', 'Logtech', 'IEshikawa', 'Marketing', 'Engg Week', 'Anniv', '1.36',	'pay as I submit',	'1',	'123456789a'),
	('2020-12305',	'Regular',	'20B - BituIEn',	'4',	'BS Industrial Engineering',	'UP Streetdance',	'Membership and Recruitment Committee',	'Internal Affairs Committee',	'External Affairs Committee',	'Publications and Records Committee',	'Finance Committee',	'Academic Affairs Committee', 'Documentation', 'Creatives', 'Logtech', 'IEshikawa', 'Marketing', 'Engg Week', 'Anniv',	'1.85',	'pay as I submit',	'1',	'123456789b'),
	('2020-07222',	'Regular',	'20A - CIEMa-sama Hanggang Dulo',	'4',	'BS Industrial Engineering',	'N/A',	'External Affairs Committee',	'Finance Committee',	'Publications and Records Committee',	'Membership and Recruitment Committee',	'Academic Affairs Committee',	'Internal Affairs Committee','Logtech', 'Documentation', 'Creatives', 'IEshikawa', 'Marketing', 'Engg Week', 'Anniv',	'1.92',	'pay as I submit',	'1',	'123456789c'),
	('2021-32696',	'Regular',	'21A - 21 Jump StrIEt',	'4',	'BS Industrial Engineering',	'N/A',	'Internal Affairs Committee',	'Academic Affairs Committee',	'Publications and Records Committee',	'Finance Committee',	'External Affairs Committee',	'Membership and Recruitment Committee','IEshikawa', 'Documentation', 'Creatives', 'Logtech', 'Marketing', 'Engg Week', 'Anniv',	'1.76', 'pay as I submit',	'1',	'123456789d'),
	('2021-70290',	'Non-Regular',	'21B - CIEMa ng Loob',	'4',	'BS Electrical Engineering',	'UP Electrical Engineering Club',	'Finance Committee',	'Academic Affairs Committee',	'Membership and Recruitment Committee',	'External Affairs Committee',	'Internal Affairs Committee',	'Publications and Records Committee', 'Anniv', 'Documentation', 'Creatives', 'IEshikawa', 'Marketing', 'Engg Week', 'Logtech',	'2.12',	'pay as I submit',	'1',	'123456789e'),
	('2021-10107',	'Non-Regular',	'21A - 21 Jump StrIEt',	'4',	'BS Computer Engineering',	'UP Computer Society, UP Circle of Entrepreneurs',	'Membership and Recruitment Committee',	'External Affairs Committee',	'Finance Committee',	'Publications and Records Committee',	'Internal Affairs Committee',	'Academic Affairs Committee','Marketing', 'Documentation', 'Creatives', 'IEshikawa', 'Anniv', 'Engg Week', 'Logtech',	'2.06',	'pay as I submit',	'1',	'123456789p'),
	('2021-10498',	'Regular',	'21A - 21 Jump StrIEt',	'4',	'BS Industrial Engineering',	'UP Career Assistance Program',	'Academic Affairs Committee',	'External Affairs Committee',	'Finance Committee',	'Internal Affairs Committee',	'Membership and Recruitment Committee',	'Publications and Records Committee','Engg Week', 'Documentation', 'Creatives', 'IEshikawa', 'Anniv', 'Marketing', 'Logtech',		'1.65',	'pay as I submit', '1',	'123456789q'),
	('2020-33002',	'Regular',	'20A - CIEMa-sama Hanggang Dulo',	'3',	'BS Industrial Engineering',	'UP Career Assistance Program',	'Membership and Recruitment Committee',	'Internal Affairs Committee',	'Publications and Records Committee',	'External Affairs Committee',	'Academic Affairs Committee',	'Finance Committee','Documentation', 'Engg Week', 'Creatives', 'IEshikawa', 'Anniv', 'Marketing', 'Logtech',		'2.38',	'pay as I submit', '1',	'123456789r'),
	('2019-52972',	'Regular',	'19A - LabingCIEM: Kaya 19 to',	'3',	'BS Industrial Engineering',	'UP Beta Epsilon',	'Membership and Recruitment Committee',	'External Affairs Committee',	'Academic Affairs Committee',	'Internal Affairs Committee',	'Finance Committee',	'Publications and Records Committee', 'Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing',	'2.56',	'pay as I submit', '1', '123456789s'),
	('2020-04754',	'Regular',	'21A - 21 Jump StrIEt',	'3',	'BS Industrial Engineering',	'UP Chinese Student Association',	'External Affairs Committee',	'Publications and Records Committee',	'Finance Committee',	'Academic Affairs Committee',	'Membership and Recruitment Committee',	'Internal Affairs Committee','Anniv', 'IEshikawa', 'Marketing', 'Engg Week', 'Creatives', 'Logtech', 'Documentation',		'1.51',	'pay as I submit', '1',	'123456789t'),
	('2019-18942',	'Regular',	'19A - LabingCIEM: Kaya 19 to',	'4',	'BS Industrial Engineering',	'N/A',	'Academic Affairs Committee',	'Finance Committee',	'External Affairs Committee',	'Internal Affairs Committee',	'Publications and Records Committee',	'Membership and Recruitment Committee',	'Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing',	'1.12',	'pay as I submit', '1',	'123456789f'),
	('2020-52970',	'Regular',	'21A - 21 Jump StrIEt',	'3',	'BS Industrial Engineering',	'UP Beta Epsilon, UP Corps of Cadets',	'Finance Committee',	'Internal Affairs Committee',	'Publications and Records Committee',	'Academic Affairs Committee',	'External Affairs Committee',	'Membership and Recruitment Committee','Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing',	'1.36',	'pay as I submit',	'1',	'123456789g'),
	('2020-10236',	'Non-Regular',	'21A - 21 Jump StrIEt',	'4',	'BS Electrical Engineering',	'N/A',	'Publications and Records Committee',	'External Affairs Committee',	'Membership and Recruitment Committee',	'Finance Committee',	'Academic Affairs Committee',	'Internal Affairs Committee', 'Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing',	'1.89',	'pay as I submit', '1',	'123456789h'),
	('2021-07310',	'Regular',	'21B - CIEMa ng Loob',	'4',	'BS Industrial Engineering',	'N/A',	'Internal Affairs Committee',	'Academic Affairs Committee',	'Membership and Recruitment Committee',	'External Affairs Committee',	'Publications and Records Committee',	'Finance Committee','Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing',	'1.67',	'pay as I submit', '1',	'123456789i'),
	('2021-02157',	'Regular',	'21A - 21 Jump StrIEt',	'4',	'BS Industrial Engineering',	'N/A',	'External Affairs Committee',	'Finance Committee',	'Internal Affairs Committee',	'Publications and Records Committee',	'Membership and Recruitment Committee',	'Academic Affairs Committee', 'Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing',		'1.31',	'pay as I submit', '1',	'123456789j'),
	('2020-03010',	'Regular',	'20A - CIEMa-sama Hanggang Dulo',	'4',	'BS Industrial Engineering',	'UP CAPES',	'Internal Affairs Committee',	'Finance Committee',	'Publications and Records Committee',	'Membership and Recruitment Committee',	'External Affairs Committee',	'Academic Affairs Committee',	'Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing','2.21',	'pay as I submit',	'1',	'123456789k'),
	('2021-91979',	'Regular',	'21A - 21 Jump StrIEt',	'5',	'BS Industrial Engineering',	'N/A',	'Academic Affairs Committee',	'External Affairs Committee',	'Finance Committee',	'Internal Affairs Committee',	'Membership and Recruitment Committee',	'Publications and Records Committee','Documentation', 'IEshikawa', 'Anniv', 'Engg Week', 'Creatives', 'Logtech', 'Marketing',	'1.18',	'pay as I submit',	'1',	'123456789l'),
	('2020-22003',	'Regular',	'21B - CIEMa ng Loob',	'4',	'BS Industrial Engineering',	'UP Engg Choir',	'Internal Affairs Committee',	'Academic Affairs Committee',	'External Affairs Committee',	'Publications and Records Committee',	'Membership and Recruitment Committee',	'Finance Committee',	'Engg Week', 'Documentation', 'Creatives', 'IEshikawa', 'Anniv', 'Marketing', 'Logtech',	'1.29',	'pay as I submit',	'1',	'123456789m'),
	('2019-07905',	'Regular',	'21B - CIEMa ng Loob',	'4',	'BS Industrial Engineering',	'UP Chinese Society Association',	'Publications and Records Committee',	'Membership and Recruitment Committee',	'Finance Committee',	'Academic Affairs Committee',	'Internal Affairs Committee',	'External Affairs Committee','Engg Week', 'Documentation', 'Creatives', 'IEshikawa', 'Anniv', 'Marketing', 'Logtech',		'1.19',	'pay as I submit',	'1',	'123456789n'),
	('2019-61100',	'Regular',	'20A - CIEMa-sama Hanggang Dulo',	'3',	'BS Industrial Engineering',	'UP Streetdance',	'Publications and Records Committee',	'Internal Affairs Committee',	'Academic Affairs Committee',	'External Affairs Committee',	'Finance Committee',	'Membership and Recruitment Committee','Engg Week', 'Documentation', 'Creatives', 'IEshikawa', 'Anniv', 'Marketing', 'Logtech',		'1.54',	'pay as I submit',	'1',	'123456789o');


INSERT INTO UPCIEM_Member (active_status, valid_id, affiliation_id)
VALUES
	('Active',	'123456789a',	'1'),
	('Active',	'123456789b',	'2'),
	('Active',	'123456789c',	'3'),
	('Active',	'123456789d',	'4'),
	('Active',	'123456789e',	'5'),
	('Active',	'123456789p',	'6'),
	('Active',	'123456789q',	'7'),
	('Active',	'123456789r',	'8'),
	('Active',	'123456789s',	'9'),
	('Active',	'123456789t',	'10'),
	('Inactive',	'123456789f',	'11'),
	('Inactive',	'123456789g',	'12'),
	('Inactive',	'123456789h',	'13'),
	('Inactive',	'123456789i',	'14'),
	('Inactive',	'123456789j',	'15'),
	('Inactive',	'123456789k',	'16'),
	('Active',	'123456789l',	'17'),
	('Active',	'123456789m',	'18'),
	('Active',	'123456789n',	'19'),
	('Active',	'123456789o',	'20');

INSERT INTO project_headship (headship_name, comm_proj, adhoc_comm)
VALUES
	('Director for Accounting',	'Findahan, Fin Series',	'IEshikawa 17'),
	('Vice Chairperson for Membership and Recruitment',	'Consti Quiz, Induction, Recruitment Tracker',	'Anniversary 46, Marketing'),
	('IEshikawa 17 Communications Manager',	'Exte Bootcamp, IEmpact',	'IEshikawa 17, LogTech'),
	('N/A',	'AcadPortal, CIEM Reviews and Tutorials ',	'Marketing, Documentation'),
	('IEshikawa 17 Finance Manager',	'Findahan, Fin Series, Financial Tracker',	'N/A'),
	('N/A',	' ',	'Documentation'),
	('Director for Application Process',	'Applicant Interview, Consti Quiz','N/A'),
	('Vice Chairperson for Academic Affairs',	'AcadPortal, CIEM Reviews and Tutorials',	'Anniversary 46'),
	('N/A',	'Projection',	'Marketing, Creatives'),
	('Director for Academic Welfare',	'AcadCommplishments',	'N/A'),
	('Anniversary Project Manager for Members Week',	'Tambayanihan',	'Anniversary 46, LogTech, Documentation'),
	('Director for Sports and Recreation',	'SemStarter, Tambayanihan, InteKa Muna', 'Creatives'),
	('IEshikawa Programs Manager',	'Leadtime',	'IEshikawa 17, Documentation'),
	('Anniversary Publicity and Creatives Manager',	'Projections, Leadtime',	'Anniversary 46, Creatives'),
	('Director for Marketing',	'IEmpact',	'Marketing'),
	('N/A',	'Findahan',	'N/A'),
	('N/A',	'Projections',	'Documentation'),
	('IEshikawa Administrative Secretary',	'Induction, Recruitment Tracker',	'IEshikawa 17, LogTech'),
	('Creatives Director',	'CIEM Brand Manual, Leadtime',	'Creatives'),
	('Vice Chairperson for Finance',	'Findahan, Financial Tracker',	'N/A');


INSERT INTO committee (committee_name, guide_book, projects, core_team)
VALUES

('Academic Affairs',	'',	'AcadCommplishments, AcadPortal, CIEM Reviews and Tutorials ',	'Vice Chairperson for Academic Affairs, Director for Academic Resources, Director for Academic Welfare'),
('External Affairs',	' ',	'Exte Bootcamp, Exte Playlist, IEmpact',	'Vice Charperson for External Affairs, Director for Community Relations, Director for External Linkages, Director for Local Relations, Director for Marketing'), 
('Finance',	' ',	'Findahan, Fin Series, Financial Tracker',	'Vice Chairperson for Finance, Director for Accounting, Director for Financial Advisory, Director for Ways and Means'),
('Internal Affairs',	' ',	'SemStarter, Tambayanihan, InteKa Muna',	'Vice Chairperson for Internal Affairs, Director for Sports and Recreation, Director for Members Welfare'),
('Membership and Recruitment',	' ',	'Consti Quiz, Induction, Recruitment Tracker',	'Vice Chairperson for Membership and Recruitment, Director for Recruitment, Director for Application Process, Director for Membership Evaluation'),
('Publications and Records',	' ',	'Projections, CIEM Brand Manual, Leadtime',	'Vice Chairperson for Publications and Records, Director for Accounts and Records, Creatives Director');


INSERT INTO performance (UPCIEM_Member_id, committee_id, headship_id, evaluation)
VALUES
 
('1',	'3',	'1',	'0.87'),
('2',	'5',	'2',	'0.79'), 
('3',	'2',	'3',	'0.45'), 
('4',	'1',	'4',	'0.39'), 
('5',	'3',	'5',	'0.78'), 
('6',	'4',	'6',	'0.92'), 
('7',	'5',	'7',	'0.56'), 
('8',	'1',	'8',	'0.9'), 
('9',	'6',	'9',	'0.88'), 
('10',	'1',	'10',	'0.32'), 
('11',	'4',	'11',	'0.49'), 
('12',	'4',	'12',	'0.52'), 
('13',	'6',	'13',	'0.38'), 
('14',	'6',	'14',	'0.5'), 
('15',	'2',	'15',	'0.81'), 
('16',	'3',	'16',	'0.72'), 
('17',	'6',	'17',	'0.38'), 
('18',	'5',	'18',	'0.48'), 
('19',	'6',	'19',	'0.96'),
('20',	'3',	'20',	'0.35');


