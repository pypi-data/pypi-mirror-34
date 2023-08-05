package TSV;

#** @file
# Main file for processing tsv formatted files
# given some list of required column names, goes through the rows and builds a
# hash for each row by column names
# note the hash will only store information for column names that we pass in
# via the required columns list
#*

use strict;
use warnings;
use POSIX qw(strftime);

my $_warnings_off = 0;

sub import
{
    my $class = shift;
    my $_warnings_off = shift if $#_ >= 0;
}

sub _build_header_hash
{
    #** @function private _build_header_hash($required_column_names)
    # @param $required_column_names [required] the list of expected column names
    # @return a reference to a hash of the required column names
    #*
    my $required_column_names = shift;
    my $header_index_hash = {};
    for my $col (@$required_column_names)
    {
        $header_index_hash->{$col} = -1; #default
    }
    return $header_index_hash;
}

sub generate_header_comments
{
    #** @function header_comments($inputfile, $outputfile)
    # @param $program the program used to generate the results
    # @param $version the version of the above program
    # @param %args a hash representing the parameters that the above program was run with
    # @return the string that will be put at the top of the output file
    #*
    my $program = shift;
    my $version = shift;
    my %args = @_;
    my $time = strftime("%Y-%m-%d %H:%M:%S", localtime);
    my @result = (
        "## Generated by $program version $version at $time",
        "## Running Parameters: ",
    );
    while((my $option, my $setting) = each %args)
    {
        push(@result, sprintf(
                "##\t%s\t%s", $option,
                defined $setting? $setting : 'undef'
            )
        );
    }
    push(@result, "##");
    return join("\n", @result) . "\n";
}

sub _parse_input_line
{
    #** @function private parse_input_line($header_index, $line)
    # builds a hash of a row from the input file using expected column identifiers
    # @param $header_index the hash of column names with their index positions in a line
    # @param $line the row we are parsing
    # @retval {} the row hash
    #*
    my ($header_index, $line) = @_;

    my @fields = split("\t", $line, -1);
    if(scalar @fields < scalar keys %$header_index)
    {
        my $err = ("[ERROR] in row $line\n"
            . "[ERROR] found "
            . scalar @fields 
            . " but expected " 
            . (scalar keys %{$header_index} ) 
            . " fields\n"
            . "Error reading the input file. The number of fields"
            . " in the input row is less than the number of required"
            . " columns. Please check that the input file is"
            . " tab-delimited and has the correct number of fields");
        die $err;
    }

    my $record = {};
    while((my $column_name, my $index) = each %$header_index)
    {
        $record->{$column_name} = $fields[$index];
    }
    return $record;
}

sub _parse_header_line
{
    #** @function private undef parse_header_line($header_index_ref, $header)
    # fills the header_index hash with the column names (keys) and their positions (values) in the line
    # @warning throws an exception if it is passed a column header (in the hash) that is not found
    # @param $header_index_ref reference to the hash indices by required column names
    # @param $header header string from the input file
    # @return none
    #*
    my ($header_index_ref, $header) = @_;
    
    my @column_names = split("\t", $header, -1);
    my $counter = 0;
    my %dup_counter = ();
    while(my $col = shift @column_names) # store the positions of the column names that we are looking for
    {
        if(exists $dup_counter{$col})
        {
            die "[ERROR] duplicate column names $col in header\n";
        }
        $dup_counter{$col} = undef;
        $header_index_ref->{$col} = $counter;
        $counter++;
    }
    while((my $column, my $index_position) = each %$header_index_ref) # check to ensure we have valid index positions for each of the required columns
    {
        if($index_position < 0)
        {
            die "[ERROR] in parsing the header of the inputfile. Did not find the required column $column";
        }
    }
}

sub parse_input
{
    #** @function public () parse_input($filename, $req_columns)
    # reads a tab-delimited file
    # creates an array of the rows (excluding comments and the header)
    # each row is turned into a hash (by header column names)
    # @param $filename the input file
    # @param $req_columns an array of expected column names
    # @retval () an array of the input file rows
    #*
    my ($filename, $req_columns) = @_;
    my $header_index = _build_header_hash($req_columns);
    die unless defined $header_index;
    open(my $fh, "<", $filename)
        or die "Could not open inputfile $filename\n";
    my $line;

    while($line = <$fh>)
    {
        last if(not ($line =~ m/^##/)); # skip comments, defined by double hash line
    }
    # the next line is the header
    chomp($line);
    $line =~ s/^#//; # remove the header starting hash if present

    _parse_header_line($header_index, $line);
    
    my @header = sort { $header_index->{$a} <=> $header_index->{$b} } keys(%$header_index);
    my @catalog = ();
    while($line = <$fh>)
    {
        chomp($line); # remove leading and trailing whitespace
        next if $line eq "";
        my $record = _parse_input_line($header_index, $line);
        die if !defined $record;
        push(@catalog, $record);
    }
    return (\@header, \@catalog);
}


sub string_line
{
    #** @method public static $ string_line($header, $line, $delim)
    # @param $header [required] (type: array ref)
    # @param $line [required] (type: hash ref)
    # @param $delim [optional] (type: string)
    # puts a line back together in the same order as the input header given some
    # delimiter
    # @return (type: string) the string of the input line
    #*
    my $header = shift;
    my $line = shift;
    my $delim = shift;
    $delim = ! defined $delim ? "\t" : $delim;
    
    my @new_line = ();
    for my $col (@$header)
    {
        if (! exists $line->{$col})
        {
            die "[ERROR] column '$col' not in row";
        }
        push(@new_line, $line->{$col});
    }
    return join($delim, @new_line);
}


1; # this makes the module usable from another perl script
