def code_function():
    #function begin############################################
    global code
    code="""

`include "{0}_env.sv"
class {0}_model_base_test extends uvm_test;

  `uvm_component_utils({0}_model_base_test)
  
  //---------------------------------------
  // env instance 
  //--------------------------------------- 
  {0}_model_env env;

  //---------------------------------------
  // constructor
  //---------------------------------------
  function new(string name = "{0}_model_base_test",uvm_component parent=null);
    super.new(name,parent);
  endfunction : new

  //---------------------------------------
  // build_phase
  //---------------------------------------
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);

    // Create the env
    env = {0}_model_env::type_id::create("env", this);
  endfunction : build_phase
  
  //---------------------------------------
  // end_of_elobaration phase
  //---------------------------------------  
  virtual function void end_of_elaboration();
    //print's the topology
    print();
  endfunction

  //---------------------------------------
  // end_of_elobaration phase
  //---------------------------------------   
 function void report_phase(uvm_phase phase);
   uvm_report_server svr;
   super.report_phase(phase);
   
   svr = uvm_report_server::get_server();
   if(svr.get_severity_count(UVM_FATAL)+svr.get_severity_count(UVM_ERROR)>0) begin
     `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
     `uvm_info(get_type_name(), "----            TEST FAIL          ----", UVM_NONE)
     `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
    end
    else begin
     `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
     `uvm_info(get_type_name(), "----           TEST PASS           ----", UVM_NONE)
     `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
    end
  endfunction 

endclass : {0}_model_base_test
""".format(protocol_name)
    print(code)
    #function end############################################

fh=open("protocol.csv","r")
for protocol_name in fh:
    protocol_name=protocol_name.strip("\n")
    fph=open('{0}_test.sv'.format(protocol_name),"w")
    code_function()
    fph.write(code)







