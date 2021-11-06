def code_function():
    #function begin############################################
    global code
    code="""
`define DRIV_IF vif.DRIVER.driver_cb

class {0}_driver extends uvm_driver #({0}_seq_item);

  //--------------------------------------- 
  // Virtual Interface
  //--------------------------------------- 
  virtual {0}_if vif;
  `uvm_component_utils({0}_driver)
    
  //--------------------------------------- 
  // Constructor
  //--------------------------------------- 
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new

  //--------------------------------------- 
  // build phase
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
     if(!uvm_config_db#(virtual {0}_if)::get(this, "", "vif", vif))
       `uvm_fatal("NO_VIF","virtual interface must be set for: ",get_full_name(),".vif");
  endfunction: build_phase

  //---------------------------------------  
  // run phase
  //---------------------------------------  
  virtual task run_phase(uvm_phase phase);
    forever begin
      seq_item_port.get_next_item(req);
      drive();
      seq_item_port.item_done();
    end
  endtask : run_phase
  
  //---------------------------------------
  // drive - transaction level to signal level
  // drives the value's from seq_item to interface signals
  //---------------------------------------
  virtual task drive();
    `DRIV_IF.wr_en <= 0;
    `DRIV_IF.rd_en <= 0;
    @(posedge vif.DRIVER.clk);
    
    `DRIV_IF.addr <= req.addr;
    
    if(req.wr_en) begin // write operation
      `DRIV_IF.wr_en <= req.wr_en;
      `DRIV_IF.wdata <= req.wdata;
      @(posedge vif.DRIVER.clk);
    end
    else if(req.rd_en) begin //read operation
      `DRIV_IF.rd_en <= req.rd_en;
      @(posedge vif.DRIVER.clk);
      `DRIV_IF.rd_en <= 0;
      @(posedge vif.DRIVER.clk);
      req.rdata = `DRIV_IF.rdata;
    end
    
  endtask : drive
endclass : {0}_driver
""".format(protocol_name)
    print(code)
    #function end############################################

fh=open("protocol.csv","r")
for protocol_name in fh:
    protocol_name=protocol_name.strip("\n")
    fph=open('{0}_drv.sv'.format(protocol_name),"w")
    code_function()
    fph.write(code)











