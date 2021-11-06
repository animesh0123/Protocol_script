def code_function():
    #function begin############################################
    global code
    code="""
`include "{0}_seq_item.sv"
`include "{0}_sequencer.sv"
`include "{0}_sequence.sv"
`include "{0}_driver.sv"
`include "{0}_monitor.sv"

class {0}_agent extends uvm_agent;

  //---------------------------------------
  // component instances
  //---------------------------------------
  {0}_driver    driver;
  {0}_sequencer sequencer;
  {0}_monitor   monitor;

  `uvm_component_utils({0}_agent)
  
  //---------------------------------------
  // constructor
  //---------------------------------------
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new

  //---------------------------------------
  // build_phase
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    
    monitor = {0}_monitor::type_id::create("monitor", this);

    //creating driver and sequencer only for ACTIVE agent
    if(get_is_active() == UVM_ACTIVE) begin
      driver    = {0}_driver::type_id::create("driver", this);
      sequencer = {0}_sequencer::type_id::create("sequencer", this);
    end
  endfunction : build_phase
  
  //---------------------------------------  
  // connect_phase - connecting the driver and sequencer port
  //---------------------------------------
  function void connect_phase(uvm_phase phase);
    if(get_is_active() == UVM_ACTIVE) begin
      driver.seq_item_port.connect(sequencer.seq_item_export);
    end
  endfunction : connect_phase

endclass : {0}_agent
""".format(animesh)
        #functionend############################################

fh=open("protocol.csv","r")
for animesh in fh:
   # protocol_name=protocol_name.strip("\n")
    animesh=animesh.strip("\n")
    fph=open('{0}_agent.sv'.format(animesh),"w")
   # code_function()
    fph.write(code)
    print(code)








