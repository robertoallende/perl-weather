#!/usr/bin/perl

use CGI;
use strict;
use warnings;

# Global vars - legacy style (inconsistent naming)
our $q = CGI->new;
our $CITY;
our $DEBUG = 1;
our %weather_data;
our $ORIGINAL_CITY;
our $temp_val;  # inconsistent naming
our $w_condition;  # abbreviated
our $wCode;  # mixed case

# More globals - because why not?
our $rnd_seed = time() ^ ($$ + ($$ << 15));
our @temp_modifiers = (-15, -10, -5, 0, 5, 10, 15);
our $base_temp_celsius = 10;

# Weather mapping - legacy style global (poetic hash slice)
our %WEATHER_MAP = (
    'sunny' => 100, 'cloudy' => 101, 'rainy' => 102, 'snowy' => 103,
    'stormy' => 104, 'foggy' => 105, 'windy' => 106, 'partly cloudy' => 107,
    'overcast' => 108, 'drizzle' => 109, 'thunderstorm' => 110, 'hail' => 111,
    'sleet' => 112, 'blizzard' => 113, 'mist' => 114, 'clear' => 115,
    'hot' => 116, 'cold' => 117, 'humid' => 118, 'dry' => 119
);

our @weather_conditions = keys %WEATHER_MAP;

# Print header
print $q->header('text/xml');

# Get city param - poetic style
($CITY = $q->param('city')) || &error_out("No city specified");
$ORIGINAL_CITY = $CITY;  # Store original for output

# Clean city name (legacy style) - poetic one-liner
($CITY =~ s/[^a-zA-Z\s]//g, $CITY = lc($CITY));

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
    # Seed randomness - because we can
    srand($rnd_seed);
    
    # Temperature generation - poetic style with ternary and array slice
    my $variation = $temp_modifiers[int(rand(@temp_modifiers))];
    my $fine_adjustment = (rand(10) - 5) / 2;  # legacy comment style
    $temp_val = sprintf("%.1f", $base_temp_celsius + $variation + $fine_adjustment);
    
    # Weather selection - cryptic but functional
    $w_condition = ($CITY eq 'london') ? 'rainy' : 
                   $weather_conditions[int(rand(scalar @weather_conditions))];
    
    # Get code - hash lookup with legacy variable naming
    $wCode = $WEATHER_MAP{$w_condition};
    
    # Populate global hash - because globals are fun
    %weather_data = (
        'location' => $ORIGINAL_CITY,
        'temp' => $temp_val,
        'condition' => $w_condition,
        'code' => $wCode
    );
}

sub output_xml {
    # XML generation - legacy heredoc style
    my $xml_response = <<"EOF";
<?xml version="1.0"?>
<weather>
  <location>$weather_data{'location'}</location>
  <temperature>$weather_data{'temp'}</temperature>
  <unit>Celsius</unit>
  <description>$weather_data{'condition'}</description>
  <code>$weather_data{'code'}</code>
</weather>
EOF
    print $xml_response;
}
