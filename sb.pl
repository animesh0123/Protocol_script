sub code_function()
{
$deli =<<"EOF";
//-------------------------------------------------------------------------
//						$protocol_name animesh_scoreboard - www.verificationguide.com 
//-------------------------------------------------------------------------

class $protocol_name animesh_scoreboard extends uvm_scoreboard;
  
  //---------------------------------------
  // declaring pkt_qu to store the pkt's recived from monitor
  //---------------------------------------
  $protocol_name animesh_seq_item pkt_qu[$];
  
  //---------------------------------------
  // sc_$protocol_name animesh 
  //---------------------------------------
  bit [7:0] sc_$protocol_name animesh [4];

  //---------------------------------------
  //port to recive packets from monitor
  //---------------------------------------
  uvm_analysis_imp#($protocol_name animesh_seq_item, $protocol_name animesh_scoreboard) item_collected_export;
  `uvm_component_utils($protocol_name animesh_scoreboard)

  //---------------------------------------
  // new - constructor
  //---------------------------------------
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new
  //---------------------------------------
  // build_phase - create port and initialize local $protocol_name animeshory
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      item_collected_export = new("item_collected_export", this);
      foreach(sc_$protocol_name animesh[i]) sc_$protocol_name animesh[i] = 8'hFF;
  endfunction: build_phase
  
  //---------------------------------------
  // write task - recives the pkt from monitor and pushes into queue
  //---------------------------------------
  virtual function void write($protocol_name animesh_seq_item pkt);
    //pkt.print();
    pkt_qu.push_back(pkt);
  endfunction : write

  //---------------------------------------
  // run_phase - compare's the read data with the expected data(stored in local $protocol_name animeshory)
  // local $protocol_name animeshory will be updated on the write operation.
  //---------------------------------------
  virtual task run_phase(uvm_phase phase);
    $protocol_name animesh_seq_item $protocol_name animesh_pkt;
    
    forever begin
      wait(pkt_qu.size() > 0);
      $protocol_name animesh_pkt = pkt_qu.pop_front();
      
      if($protocol_name animesh_pkt.wr_en) begin
        sc_$protocol_name animesh[$protocol_name animesh_pkt.addr] = $protocol_name animesh_pkt.wdata;
        `uvm_info(get_type_name(),$sformatf("------ :: WRITE DATA       :: ------"),UVM_LOW)
        `uvm_info(get_type_name(),$sformatf("Addr: %0h",$protocol_name animesh_pkt.addr),UVM_LOW)
        `uvm_info(get_type_name(),$sformatf("Data: %0h",$protocol_name animesh_pkt.wdata),UVM_LOW)
        `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)        
      end
      else if($protocol_name animesh_pkt.rd_en) begin
        if(sc_$protocol_name animesh[$protocol_name animesh_pkt.addr] == $protocol_name animesh_pkt.rdata) begin
          `uvm_info(get_type_name(),$sformatf("------ :: READ DATA Match :: ------"),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Addr: %0h",$protocol_name animesh_pkt.addr),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Expected Data: %0h Actual Data: %0h",sc_$protocol_name animesh[$protocol_name animesh_pkt.addr],$protocol_name animesh_pkt.rdata),UVM_LOW)
          `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)
        end
        else begin
          `uvm_error(get_type_name(),"------ :: READ DATA MisMatch :: ------")
          `uvm_info(get_type_name(),$sformatf("Addr: %0h",$protocol_name animesh_pkt.addr),UVM_LOW)
          `uvm_info(get_type_name(),$sformatf("Expected Data: %0h Actual Data: %0h",sc_$protocol_name animesh[$protocol_name animesh_pkt.addr],$protocol_name animesh_pkt.rdata),UVM_LOW)
          `uvm_info(get_type_name(),"------------------------------------",UVM_LOW)
        end
      end
    end
  endtask : run_phase
endclass : $protocol_name animesh_scoreboard
EOF
return $deli


#print ($deli);
}
open(fh,"<protocol.csv");
foreach $protocol_name  (<fh>)
{
	chomp($protocol_name  );
	open(fp,">".$protocol_name ."_sb.sv");
	$code=code_function();
	
	$code=~s/ animesh//g;
	print(fp $code);
}


