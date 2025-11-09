#!/usr/bin/perl

use CGI;
use strict;
use warnings;

# Global vars - legacy style
our $q = CGI->new;
our $CITY;
our $DEBUG = 1;
our %weather_data;

# Print header
print $q->header('text/xml');

# Get city param
$CITY = $q->param('city') || '';

# Basic validation
if (!$CITY) {
    &error_out("No city specified");
}

# Clean city name (legacy style)
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

# Placeholder subs
sub generate_weather {
    # TODO: Implement weather algorithm
}

sub output_xml {
    # TODO: Implement XML output
}
