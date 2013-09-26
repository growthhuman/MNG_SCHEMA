#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use Carp;
use Data::Dumper;

my @user;
my @direct;
my @search;
my @account;
my @isa;

my @user_ut;
my @direct_ut;
my @search_ut;
my @account_ut;
my @isa_ut;

my @user_y;
my @direct_y;
my @search_y;
my @account_y;
my @isa_y;

my @user_y_ut;
my @direct_y_ut;
my @search_y_ut;
my @account_y_ut;
my @isa_y_ut;

my $q = new CGI;
$q->charset('utf-8');
print $q->header;

open (my $search_file,   '<','./search.txt'   );
while (my $line = <$search_file>){ push(@search,$line); }
open (my $direct_file,   '<','./direct.txt'   );
while (my $line = <$direct_file>){ push(@direct,$line); }
open (my $account_file,   '<','./account.txt'   );
while (my $line = <$account_file>){ push(@account,$line); }
open (my $isa_file,   '<','./isa.txt'   );
while (my $line = <$isa_file>){ push(@isa,$line); }

open (my $search_ut_file,   '<','./search_ut.txt'   );
while (my $line = <$search_ut_file>){ push(@search_ut,$line); }
open (my $direct_ut_file,   '<','./direct_ut.txt'   );
while (my $line = <$direct_ut_file>){ push(@direct_ut,$line); }
open (my $account_ut_file,   '<','./account_ut.txt'   );
while (my $line = <$account_ut_file>){ push(@account_ut,$line); }
open (my $isa_ut_file,   '<','./isa_ut.txt'   );
while (my $line = <$isa_ut_file>){ push(@isa_ut,$line); }

open (my $search_y_file,   '<','./search_y.txt'   );
while (my $line = <$search_y_file>){ push(@search_y,$line); }
open (my $direct_y_file,   '<','./direct_y.txt'   );
while (my $line = <$direct_y_file>){ push(@direct_y,$line); }
open (my $account_y_file,   '<','./account_y.txt'   );
while (my $line = <$account_y_file>){ push(@account_y,$line); }
open (my $isa_y_file,   '<','./isa_y.txt'   );
while (my $line = <$isa_y_file>){ push(@isa_y,$line); }

open (my $search_y_ut_file,   '<','./search_y_ut.txt'   );
while (my $line = <$search_y_ut_file>){ push(@search_y_ut,$line); }
open (my $direct_y_ut_file,   '<','./direct_y_ut.txt'   );
while (my $line = <$direct_y_ut_file>){ push(@direct_y_ut,$line); }
open (my $account_y_ut_file,   '<','./account_y_ut.txt'   );
while (my $line = <$account_y_ut_file>){ push(@account_y_ut,$line); }
open (my $isa_y_ut_file,   '<','./isa_y_ut.txt'   );
while (my $line = <$isa_y_ut_file>){ push(@isa_y_ut,$line); }
#################### H T M L 出 力 開 始 #######################
print '<center>';
print '<hr>';
print 'LT/STスキーマ';
print '<hr>';
#---------------------------------------------------------#
print '<table>';
print '<tr>';
print qq{<td align="center" width="150" bgcolor="#0066FF"  >Monitor/Search</td align="center" width="150">};
print qq{<td align="center" width="150" bgcolor="#FF9900">Direct</td align="center" width="150">};
print qq{<td align="center" width="150" bgcolor="#FF3333"   >Account</td align="center" width="150">};
print qq{<td align="center" width="150" bgcolor="#339933" >ISA</td align="center" width="150">};
print '</tr>';
for (my $i=0;$i <= $#search;$i++){
    print '<tr>';
    print qq{<td align="center" width="150" bgcolor="#ccffff">$search[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffcc99">$direct[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffccff">$account[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ccffcc">$isa[$i]</td align="center" width="150">};
    print '</tr>';
}
print '</table>';
#---------------------------------------------------------#
print '<hr>';
print 'UTスキーマ';
print '<hr>';
print '<table>';
for (my $i=0;$i <= $#search_ut;$i++){
    print '<tr>';
    print qq{<td align="center" width="150" bgcolor="#ccffff">$search_ut[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffcc99">$direct_ut[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffccff">$account_ut[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ccffcc">$isa_ut[$i]</td align="center" width="150">};
    print '</tr>';
}
print '</table>';
#---------------------------------------------------------#
print '<hr>';
print 'LT/STスキーマ';
print '<hr>';
print '<table>';
for (my $i=0;$i <= $#search_y;$i++){
    print '<tr>';
    print qq{<td align="center" width="150" bgcolor="#ccffff">$search_y[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffcc99">$direct_y[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffccff">$account_y[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ccffcc">$isa_y[$i]</td align="center" width="150">};
    print '</tr>';
}
print '</table>';
#---------------------------------------------------------#
print '<hr>';
print 'UTスキーマ';
print '<hr>';
print '<table>';
for (my $i=0;$i <= $#search_y_ut;$i++){
    print '<tr>';
    print qq{<td align="center" width="150" bgcolor="#ccffff">$search_y_ut[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffcc99">$direct_y_ut[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ffccff">$account_y_ut[$i]</td align="center" width="150">};
    print qq{<td align="center" width="150" bgcolor="#ccffcc">$isa_y_ut[$i]</td align="center" width="150">};
    print '</tr>';
}
print '</table>';
#---------------------------------------------------------#
print '</center>';
