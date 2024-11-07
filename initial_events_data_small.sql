-- Create the events table if it doesn't exist
CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

-- Insert some sample data
INSERT INTO events (name, description, latitude, longitude) VALUES
('Sample Event 1', 'Description for Sample Event 1', 53.3498, -6.2603),
('Sample Event 2', 'Description for Sample Event 2', 51.5074, -0.1278),
('Sample Event 3', 'Description for Sample Event 3', 40.7128, -74.0060);
