--Creating tables for FinalProjectDB
CREATE TABLE ziptable (
	zip VARCHAR(5) NOT NULL,
	typee VARCHAR(8),
	decommissioned VARCHAR(1),
	primary_city VARCHAR(25),
	acceptable_cities VARCHAR(1000),
	unacceptable_cities VARCHAR (1000),
	statee VARCHAR(2),
	county VARCHAR(50),
	timezone VARCHAR(50),
	area_codes VARCHAR(50),
	world_region VARCHAR(2),
	country VARCHAR(2),
	latitude VARCHAR(10),
	longitude VARCHAR(10),
	irs_estimated_population INT,
	PRIMARY KEY (zip) 
);
CREATE TABLE housedata (
	id_num VARCHAR(15) NOT NULL,
	datee DATE,
	price INT,
	bedrooms INT,
	bathrooms VARCHAR(5),
	sqft_living INT,
	sqft_lot INT,
	floors INT,
	waterfront VARCHAR(5),
	vieww VARCHAR(5),
	conditionn INT,
	grade INT,
	sqft_above INT,
	sqft_basement INT,
	yr_built VARCHAR(4),
	yr_renovated VARCHAR(4),
	zipcode VARCHAR(5),
	lat VARCHAR(10),
	long VARCHAR(10),
	sqft_living15 INT,
	sqft_lot15 INT,	
	FOREIGN KEY (zipcode) REFERENCES ziptable (zip),
PRIMARY KEY (id_num)
);
SELECT * FROM ziptable;