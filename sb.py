def code_function():
    #function begin############################################
    global code
    code="""
class {0}_scoreboard extends uvm_scoreboard;
  
  //---------------------------------------
  // declaring pkt_qu to store the pkt's recived from monitor
  //---------------------------------------
  {0}_seq_item pkt_qu[$];
  
  //---------------------------------------
  // sc_{0} 
  //---------------------------------------
  bit [7:0] sc_{0} [4];

  //---------------------------------------
  //port to recive packets from monitor
  //---------------------------------------
  uvm_analysis_imp#({0}_seq_item, {0}_scoreboard) item_collected_export;
  `uvm_component_utils({0}_scoreboard)

  //---------------------------------------
  // new - constructor
  //---------------------------------------
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new
  //---------------------------------------
  // build_phase - create port and initialize local {0}ory
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      item_collected_export = new("item_collected_export", this);
      foreach(sc_{0}[i]) sc_{0}[i] = 8'hFF;
  endfunction: build_phase
  
  //---------------------------------------
  // write task - recives the pkt from monitor and pushes into queue
  //---------------------------------------
  virtual function void write({0}_seq_item pkt);
    //pkt.print();
    pkt_qu.push_back(pkt);
  endfunction : write

  //---------------------------------------
  // run_phase - compare's the read data with the expected data(stored in local {0}ory)
  // local {0}ory will be updated on the write operation.
  //---------------------------------------
  virtual task run_phase(uvm_phase phase);
    {0}_seq_item {0}_pkt;
    
    forever begin
      wait(pkt_qu.size() > 0);
      {0}_pkt = pkt_qu.pop_front();
      
      if({0}_pkt.wr_en) begin
        sc_{0}[{0}_pkt.addr] = {0}_pkt.wdata;
        `uvm_info(get_type_name(),$sformatf("------ :: WRITE DATA       :: ------"),UVM_LOW)
        `uvm_info(get_type_name(),$sformatf("Addr: %0h",{0}_pkt.addr),UVM_LOW)
        `uvm_info(get_type_name(),$sformatf("Data: %0h",{0}_pkt.wdata),UVM_LOW)
        `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)        
      end
      else if({0}_pkt.rd_en) begin
        if(sc_{0}[{0}_pkt.addr] == {0}_pkt.rdata) begin
          `uvm_info(get_type_name(),$sformatf("------ :: READ DATA Match :: ------"),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Addr: %0h",{0}_pkt.addr),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Expected Data: %0h Actual Data: %0h",sc_{0}[{0}_pkt.addr],{0}_pkt.rdata),UVM_LOW)
          `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)
        end
        else begin
          `uvm_error(get_type_name(),"------ :: READ DATA MisMatch :: ------")
          `uvm_info(get_type_name(),$sformatf("Addr: %0h",{0}_pkt.addr),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Expected Data: %0h Actual Data: %0h",sc_{0}[{0}_pkt.addr],{0}_pkt.rdata),UVM_LOW)
          `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)
        end
      end
    end
  endtask : run_phase
endclass : {0}_scoreboard
""".format(protocol_name)
    print(code)
    #function end############################################

fh=open("protocol.csv","r")
for protocol_name in fh:
    protocol_name=protocol_name.strip("\n")
    fph=open('{0}_sb.sv'.format(protocol_name),"w")
    code_function()
    fph.write(code)








