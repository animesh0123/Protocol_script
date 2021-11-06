def code_function():
    #function begin############################################
    global code
    code="""
`include "{0}_agent.sv"
`include "{0}_scoreboard.sv"

class {0}_model_env extends uvm_env;
  
  //---------------------------------------
  // agent and scoreboard instance
  //---------------------------------------
  {0}_agent      {0}_agnt;
  {0}_scoreboard {0}_scb;
  
  `uvm_component_utils({0}_model_env)
  
  //--------------------------------------- 
  // constructor
  //---------------------------------------
  function new(string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new

  //---------------------------------------
  // build_phase - crate the components
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);

    {0}_agnt = {0}_agent::type_id::create("{0}_agnt", this);
    {0}_scb  = {0}_scoreboard::type_id::create("{0}_scb", this);
  endfunction : build_phase
  
  //---------------------------------------
  // connect_phase - connecting monitor and scoreboard port
  //---------------------------------------
  function void connect_phase(uvm_phase phase);
    {0}_agnt.monitor.item_collected_port.connect({0}_scb.item_collected_export);
  endfunction : connect_phase

endclass : {0}_model_env
""".format(protocol_name)
    print(code)
    #function end############################################

fh=open("protocol.csv","r")
for protocol_name in fh:
    protocol_name=protocol_name.strip("\n")
    fph=open('{0}_env.sv'.format(protocol_name),"w")
    code_function()
    fph.write(code)








