#!/usr/bin/perl

use CGI;
use strict;
use warnings;

# Global vars - legacy style
our $q = CGI->new;
our $CITY;
our $DEBUG = 1;
our %weather_data;

# Weather mapping - legacy style global
our %WEATHER_MAP = (
    'sunny' => 100, 'cloudy' => 101, 'rainy' => 102, 'snowy' => 103,
    'stormy' => 104, 'foggy' => 105, 'windy' => 106, 'partly cloudy' => 107,
    'overcast' => 108, 'drizzle' => 109, 'thunderstorm' => 110, 'hail' => 111,
    'sleet' => 112, 'blizzard' => 113, 'mist' => 114, 'clear' => 115,
    'hot' => 116, 'cold' => 117, 'humid' => 118, 'dry' => 119
);

our @weather_conditions = keys %WEATHER_MAP;
our ($temp, $condition, $weather_code);

# Print header
print $q->header('text/xml');

# Get city param
$CITY = $q->param('city') || '';
our $ORIGINAL_CITY = $CITY;  # Store original for output

# Basic validation
if (!$CITY) {
    &error_out("No city specified");
}

# Clean city name (legacy style) - for processing only
$CITY =~ s/[^a-zA-Z\s]//g;
$CITY = lc($CITY);

# Generate weather and output XML
&generate_weather();
&output_xml();

exit 0;

# Error handler - legacy style
sub error_out {
    my $msg = shift;
    print qq{<?xml version="1.0"?>
<error>
<message>$msg</message>
</error>};
    exit 1;
}

sub generate_weather {
    # Temperature around 10C with randomness - legacy style
    srand();
    my $base_temp = 10;
    my $variation = int(rand(30)) - 15; # -15 to +15
    my $fine_tune = (rand(10) - 5) / 2; # -2.5 to +2.5
    $temp = $base_temp + $variation + $fine_tune;
    $temp = sprintf("%.1f", $temp);
    
    # Pick random weather condition - fix array access
    if ($CITY eq 'london') {
        $condition = 'rainy';
    } else {
        my $idx = int(rand(scalar @weather_conditions));
        $condition = $weather_conditions[$idx];
    }
    $weather_code = $WEATHER_MAP{$condition};
    
    # Store in global hash - legacy pattern
    %weather_data = (
        'location' => $ORIGINAL_CITY,
        'temp' => $temp,
        'condition' => $condition,
        'code' => $weather_code
    );
}

sub output_xml {
    print qq{<?xml version="1.0"?>
<weather>
  <location>$weather_data{'location'}</location>
  <temperature>$weather_data{'temp'}</temperature>
  <unit>Celsius</unit>
  <description>$weather_data{'condition'}</description>
  <code>$weather_data{'code'}</code>
</weather>};
}
