# Legacy Perl Weather API

A deliberately outdated Perl CGI weather service that mimics legacy production systems with "poetic" Perl, global variables, inconsistent naming, and zero documentation.

## Features

- Returns weather data in XML format for any city
- Randomized temperature generation (biased around 10°C)
- 20 weather conditions mapped to numeric codes (100-119)
- Special case: London is always rainy
- Authentic legacy code patterns (hard to read and maintain)

## Running the Service

1. **Start the HTTP server:**
   ```bash
   cd src
   python3 -m http.server --cgi 8000
   ```

2. **The API will be available at:**
   ```
   http://localhost:8000/cgi-bin/weather.cgi?city=<city_name>
   ```

## Usage Examples

### Basic weather request:
```bash
curl http://localhost:8000/cgi-bin/weather.cgi?city=Paris
```

**Response:**
```xml
<?xml version="1.0"?>
<weather>
  <location>Paris</location>
  <temperature>12.3</temperature>
  <unit>Celsius</unit>
  <description>sunny</description>
  <code>100</code>
</weather>
```

### London (always rainy):
```bash
curl http://localhost:8000/cgi-bin/weather.cgi?city=London
```

**Response:**
```xml
<?xml version="1.0"?>
<weather>
  <location>London</location>
  <temperature>8.7</temperature>
  <unit>Celsius</unit>
  <description>rainy</description>
  <code>102</code>
</weather>
```

### City with spaces and punctuation:
```bash
curl "http://localhost:8000/cgi-bin/weather.cgi?city=New York, NY"
```

**Response:**
```xml
<?xml version="1.0"?>
<weather>
  <location>New York, NY</location>
  <temperature>15.1</temperature>
  <unit>Celsius</unit>
  <description>cloudy</description>
  <code>101</code>
</weather>
```

### Error handling (no city):
```bash
curl http://localhost:8000/cgi-bin/weather.cgi
```

**Response:**
```xml
<?xml version="1.0"?>
<error>
<message>No city specified</message>
</error>
```

## Weather Codes

| Code | Description | Code | Description |
|------|-------------|------|-------------|
| 205  | sunny       | 318  | thunderstorm |
| 142  | cloudy      | 267  | hail |
| 189  | rainy       | 391  | sleet |
| 156  | snowy       | 224  | blizzard |
| 273  | stormy      | 185  | mist |
| 198  | foggy       | 302  | clear |
| 234  | windy       | 167  | hot |
| 291  | partly cloudy | 243 | cold |
| 176  | overcast    | 358  | humid |
| 312  | drizzle     | 129  | dry |

## Development

This project was built using MMDD (Micromanaged Driven Development) methodology. See `dev_log/` for the complete development history and unit breakdown.
