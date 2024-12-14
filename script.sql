CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    PhoneNumber TEXT,
    DateOfBirth TEXT,  -- Store as 'dd-mm-yyyy'
    Country TEXT,
    EmailAddress TEXT UNIQUE NOT NULL,
    Education TEXT,
    CollegeOrOrganization TEXT,
    PasswordHash TEXT NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);
