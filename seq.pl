sub code_function()
{
$deli =<<"EOF";
class $protocol_name animesh_sequencer extends uvm_sequencer#($protocol_name animesh_seq_item);

  `uvm_component_utils($protocol_name animesh_sequencer) 

  //---------------------------------------
  //constructor
  //---------------------------------------
  function new(string name, uvm_component parent);
    super.new(name,parent);
  endfunction
  
endclass
EOF
return $deli


#print ($deli);
}
open(fh,"<protocol.csv");
foreach $protocol_name (<fh>)
{
	chomp($protocol_name );
	open(fp,">".$protocol_name."_seq.sv");
	$code=code_function();
	
	$code=~s/ animesh//g;
	print(fp $code);

	#print (fp $deli);
}



