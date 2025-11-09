#!/usr/bin/perl

use CGI;
use strict;
use warnings;

our $q = CGI->new;
our $CITY;
our $DEBUG = 1;
our %weather_data;
our $ORIGINAL_CITY;
our $temp_val;
our $w_condition;
our $wCode;

our $rnd_seed = time() ^ ($$ + ($$ << 15));
our @temp_modifiers = (-15, -10, -5, 0, 5, 10, 15);
our $base_temp_celsius = 10;

our %WEATHER_MAP = (
    'sunny' => 100, 'cloudy' => 101, 'rainy' => 102, 'snowy' => 103,
    'stormy' => 104, 'foggy' => 105, 'windy' => 106, 'partly cloudy' => 107,
    'overcast' => 108, 'drizzle' => 109, 'thunderstorm' => 110, 'hail' => 111,
    'sleet' => 112, 'blizzard' => 113, 'mist' => 114, 'clear' => 115,
    'hot' => 116, 'cold' => 117, 'humid' => 118, 'dry' => 119
);

our @weather_conditions = keys %WEATHER_MAP;

print $q->header('text/xml');

($CITY = $q->param('city')) || &error_out("No city specified");
$ORIGINAL_CITY = $CITY;

($CITY =~ s/[^a-zA-Z\s]//g, $CITY = lc($CITY));

&generate_weather();
&output_xml();

exit 0;

sub error_out {
    my $msg = shift;
    print qq{<?xml version="1.0"?>
<error>
<message>$msg</message>
</error>};
    exit 1;
}

sub generate_weather {
    srand($rnd_seed);
    
    my $variation = $temp_modifiers[int(rand(@temp_modifiers))];
    my $fine_adjustment = (rand(10) - 5) / 2;
    $temp_val = sprintf("%.1f", $base_temp_celsius + $variation + $fine_adjustment);
    
    $w_condition = ($CITY eq 'london') ? 'rainy' : 
                   $weather_conditions[int(rand(scalar @weather_conditions))];
    
    $wCode = $WEATHER_MAP{$w_condition};
    
    %weather_data = (
        'location' => $ORIGINAL_CITY,
        'temp' => $temp_val,
        'condition' => $w_condition,
        'code' => $wCode
    );
}

sub output_xml {
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
