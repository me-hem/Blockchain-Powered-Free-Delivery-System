# TPC-H : A Decision Support Benchmark

The TPC-H is a decision support benchmark. It consists of a suite of business oriented ad-hoc queries and concurrent data modifications. The queries and the data populating the database have been chosen to have broad industry-wide relevance. This benchmark illustrates decision support systems that examine large volumes of data, execute queries with a high degree of complexity, and give answers to critical business questions. The performance metric reported by TPC-H is called the TPC-H Composite Query-per-Hour Performance Metric (QphH@Size), and reflects multiple aspects of the capability of the system to process queries. These aspects include the selected database size against which the queries are executed, the query processing power when queries are submitted by a single stream, and the query throughput when queries are submitted by multiple concurrent users. 


## Instructions to generate dataset.

Open terminal and clone the project,
  `git clone https://github.com/electrum/tpch-dbgen`

Move makefile.suite to makefile,
  `mv makefile.suite makefile` 

Open makefile and update the fields as follows:
- cc= gcc
- DATABASE=  SQLSERVER
- MACHINE =  LINUX
- WORKLOAD =  TPCH

Open tpcd.h file `nano tpcd.h` and Update SQL Server Macro (for SQLSERVER compatible dataset) as follows:
- GEN_QUERY_PLAN from "set showplan on\nset noexec on\ngo\n" to  "explain;"
- START_TRAN from "begin transaction\ngo\n" to "start transaction;"
- END_TRAN from "commit transaction\ngo\n" to "commit;"
- SET_ROWCOUNT from "set rowcount %d\ngo\n\n" to "limit %d;"

Run the following command to genereate dbgen and qgen file,
`make`

To generate data,
`./dbgen -s <size of dataset in Gb>`

**Now you can find the data in .tbl files.**
