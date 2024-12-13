CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    PhoneNumber TEXT,
    DateOfBirth TEXT, -- Store as 'dd-mm-yyyy'
    Country TEXT,
    EmailAddress TEXT UNIQUE NOT NULL,
    Education TEXT,
    CollegeOrOrganization TEXT,
    PasswordHash TEXT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

