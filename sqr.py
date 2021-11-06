def code_function():
    #function begin############################################
    global code
    code="""

class {0}_sequencer extends uvm_sequencer#({0}_seq_item);

  `uvm_component_utils({0}_sequencer) 

  //---------------------------------------
  //constructor
  //---------------------------------------
  function new(string name, uvm_component parent);
    super.new(name,parent);
  endfunction
  
endclass""".format(protocol_name)
    print(code)
    #function end############################################

fh=open("protocol.csv","r")
for protocol_name in fh:
    protocol_name=protocol_name.strip("\n")
    fph=open('{0}_sqr.sv'.format(protocol_name),"w")
    code_function()
    fph.write(code)










