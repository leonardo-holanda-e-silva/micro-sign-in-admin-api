CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Criação da tabela Company
CREATE TABLE company (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Department
CREATE TABLE department (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    company_id UUID REFERENCES company(id)
);

-- Criação da tabela Function
CREATE TABLE function (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Group
CREATE TABLE "group" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Permission
CREATE TABLE permission (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela System
CREATE TABLE system (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL
);

-- Criação da tabela User
CREATE TABLE "user" (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    mails JSONB NOT NULL,
    addresses JSONB NOT NULL,
    birth DATE NOT NULL,
    entry_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    phones JSONB NOT NULL
);

-- Criação das tabelas intermediárias para relacionamentos many-to-many

-- Tabela intermediária user_companies
CREATE TABLE user_companies (
    user_id UUID REFERENCES "user"(id) ON DELETE CASCADE,
    company_id UUID REFERENCES company(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, company_id)
);

-- Tabela intermediária user_departments
CREATE TABLE user_departments (
    user_id UUID REFERENCES "user"(id) ON DELETE CASCADE,
    department_id UUID REFERENCES department(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, department_id)
);

-- Tabela intermediária user_functions
CREATE TABLE user_functions (
    user_id UUID REFERENCES "user"(id) ON DELETE CASCADE,
    function_id UUID REFERENCES function(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, function_id)
);

-- Tabela intermediária user_groups
CREATE TABLE user_groups (
    user_id UUID REFERENCES "user"(id) ON DELETE CASCADE,
    group_id UUID REFERENCES "group"(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, group_id)
);

-- Tabela intermediária group_permissions
CREATE TABLE group_permissions (
    group_id UUID REFERENCES "group"(id) ON DELETE CASCADE,
    permission_id UUID REFERENCES permission(id) ON DELETE CASCADE,
    PRIMARY KEY (group_id, permission_id)
);

-- Tabela intermediária group_systems
CREATE TABLE group_systems (
    group_id UUID REFERENCES "group"(id) ON DELETE CASCADE,
    system_id UUID REFERENCES system(id) ON DELETE CASCADE,
    PRIMARY KEY (group_id, system_id)
);