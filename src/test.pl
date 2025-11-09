#!/usr/bin/perl

# Simple test without CGI environment
use strict;
use warnings;

# Simulate the core logic
my $city = $ARGV[0] || '';

if (!$city) {
    print "<?xml version=\"1.0\"?>\n<error>\n<message>No city specified</message>\n</error>\n";
    exit 1;
}

# Clean city name (legacy style)
$city =~ s/[^a-zA-Z\s]//g;
$city = lc($city);

print "City processed: $city\n";
print "Weather generation would happen here...\n";
