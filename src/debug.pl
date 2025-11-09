#!/usr/bin/perl
use strict;
use warnings;

our %WEATHER_MAP = (
    'sunny' => 100, 'cloudy' => 101, 'rainy' => 102, 'snowy' => 103,
    'stormy' => 104, 'foggy' => 105, 'windy' => 106, 'partly cloudy' => 107,
    'overcast' => 108, 'drizzle' => 109, 'thunderstorm' => 110, 'hail' => 111,
    'sleet' => 112, 'blizzard' => 113, 'mist' => 114, 'clear' => 115,
    'hot' => 116, 'cold' => 117, 'humid' => 118, 'dry' => 119
);

our @weather_conditions = keys %WEATHER_MAP;

print "Weather conditions: " . scalar(@weather_conditions) . "\n";
print "First few: " . join(", ", @weather_conditions[0..4]) . "\n";

my $idx = int(rand(scalar @weather_conditions));
my $condition = $weather_conditions[$idx];
my $code = $WEATHER_MAP{$condition};

print "Selected: $condition -> $code\n";
