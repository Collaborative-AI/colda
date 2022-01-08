<template>
<div>
  <!-- {{backend_log}} -->



  <div class="btn-group btn-group-toggle" data-toggle="buttons">
    <label class="btn btn-secondary">
    <input type="radio" name="options" id="option2" value="chart" v-model="page"> Chart
  </label>
  <label class="btn btn-secondary">
    <input type="radio" name="options" id="option1" value="log" v-model="page"> Log
  </label>
  <label class="btn btn-secondary">
    <input type="radio" name="options" id="option3" value="log2" v-model="page"> Log2
  </label>
</div>
  <!-- 历史私信列表 -->
  <div v-if="page=='log'" class="card border-0 g-mb-15 my-5">
    
    <!-- End Panel Header -->
    <div class="form-group">
      <router-link v-bind:to="{ name: 'FindTestAssistorHelper', query: { from: task_id, from_task_name: task_name, from_test_id: test_id } }">
        <button v-show="isSponsor" class="btn btn-success float-right">Call For Test</button>
      </router-link>
      
                
    </div>



    <!-- Panel Body -->
    <div class="card-block g-pa-0" >
      <!-- Chat. Message Area. Messages. -->
      <div class="g-brd-around g-brd-gray-light-v4 g-pa-20">
        <div v-for="(message, index) in messages" v-bind:key="index">
          <!-- Chat. Message Area. Message (From). -->
          <section class="g-mb-30">
            <div class="media g-mb-12">
              
              <div class="media-body">
                <div class="d-inline-block g-width-300 g-width-auto--sm g-bg-gray-light-v8 g-font-size-12 g-font-size-default--lg g-color-gray-dark-v6 g-rounded-10 g-pa-10-15">
                  <p class="mb-0">
                    {{ message }}
                  </p>
                </div>
              </div>
              <!-- End Chat. Message Area. Message. Body. -->
            </div>

          </section>

        </div>
        
      </div>
      <button @click="getLog($route.query.from); checkSponsor($route.query.from)" class="btn btn-success float-right">Refresh</button>
      <!-- End Chat. Message Area. Messages. -->
    </div>
    <!-- End Panel Body -->
  </div>


    <div v-if="page=='log2'" class="card border-0 g-mb-15 my-5">
    
     <div class="g-brd-around g-brd-gray-light-v4 g-pa-20">
        <div v-for="(message2, index) in messages2" v-bind:key="index">
          <!-- Chat. Message Area. Message (From). -->
          <section class="g-mb-30">
            <div class="media g-mb-12">
              
              <div class="media-body">
                <div class="d-inline-block g-width-300 g-width-auto--sm g-bg-gray-light-v8 g-font-size-12 g-font-size-default--lg g-color-gray-dark-v6 g-rounded-10 g-pa-10-15">
                  <p class="mb-0">
                    {{ message2 }}
                  </p>
                </div>
              </div>
              <!-- End Chat. Message Area. Message. Body. -->
            </div>

          </section>

        </div>
        
      </div>
 
  </div>

  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
<div v-if="page=='chart'" class="container my-5">
<div class="row">
<!-- mad -->
  <div v-if="task_mode == 'regression'" class="col-md-6">
    <div class="box box-aqua" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData3"
          :options="lineChartOptions3"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div> 

<!-- rmse  -->
  <div v-if="task_mode == 'regression'"  class="col-md-6">
    <div class="box box-green" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData"
          :options="lineChartOptions"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div> 
<!-- r2 -->
  <div v-if="task_mode == 'regression'" class="col-md-6">
    <div class="box box-aqua" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData4"
          :options="lineChartOptions4"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div> 

  <!-- <div v-if="test_num == '1'" class="col-md-6">
    <div class="box box-aqua" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData2"
          :options="lineChartOptions2"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div>  -->
  
 <!-- alpha -->
  <div v-if="task_mode == 'regression'" class="col-md-6">
    <div class="box box-green" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData1"
          :options="lineChartOptions1"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div>   


  <div v-if="task_mode == 'classification'" class="col-md-6">
    <div class="box box-green" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData5"
          :options="lineChartOptions5"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div>   

  <div v-if="task_mode == 'classification'" class="col-md-6">
    <div class="box box-green" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData6"
          :options="lineChartOptions6"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div>   

  <div v-if="task_mode == 'classification'" class="col-md-6">
    <div class="box box-green" id="chart-parent">
      <mdb-container style='height: auto; width: 100%; object-fit: contain' id="line-chart" v-cloak>
        <mdb-line-chart id="chart"
          :data="lineChartData7"
          :options="lineChartOptions7"
        ></mdb-line-chart>
      </mdb-container>
    </div>
  </div>   


</div>

</div>
  

</div>
</template>

<script>
const fs = window.fs;
const ex = window.ex;
const os = window.os;
const node_path = window.node_path;
const log = window.log;

import store from '../../../store'
// 导入 vue-markdown 组件解析 markdown 原文为　HTML
// import VueMarkdown from 'vue-markdown'
import Pagination from '../../../components/Pagination'

// const store = require('../../../store').default
// // const VueMarkdown = require('vue-markdown').default
// const Pagination = require('../../../components/Pagination.vue').default
import { mdbLineChart, mdbContainer } from "mdbvue";



var baseline_rmse = []
var training_rmse = []
var test_rmse = []

var training_alpha = []

var baseline_mad = []
var training_mad = []
var test_mad = []

var baseline_r2 = []
var training_r2 = []
var test_r2 = []
// const baseline_rmse = []
// const training_rmse = []
// const training_alpha = []
// const test_rmse = []

var baseline_accuracy = []
var training_accuracy = []
var test_accuracy = []
var baseline_f1 = []
var training_f1 = []
var test_f1 = []
var training_alpha2 = []




export default {
  name: 'History',  //this is the name of the component
  components: {
    // VueMarkdown,
    Pagination,
    mdbLineChart,
    mdbContainer
  },
  
  data () {
    return {
      sharedState: store.state,
      user: '',
      messages: [],
      message2: [],
      displays: [],
      typein_message: '',
      showOnce: true,
      replyMessageForm: {
        body: '',
        errors: 0,  // 发送私信时，表单验证是否有错误
        bodyError: null
      },
      // Log_content_array: null,
      isSponsor: false,
      root: '',
      task_id: '',
      task_name: '',
      test_id: '',
      task_description: '',
      page: 'chart',
      test_num: '2',
      backend_log: "",
      task_mode: "",
      
      // baseline_rmse: [30, 30, 80, 81, 56, 55, 40],
      lineChartData: {
          labels: [
            "0",
            "1",
            "2"
          ],
          datasets: [
            {
              label: "Baseline RMSE",
              // backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: baseline_rmse
            },
            {
              label: "Training RMSE",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_rmse
            },
            {
              label: "Test RMSE",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(3,3,205,1)",
              borderWidth: 0.8,
              data: test_rmse
            },
            
          ]
        },
        
        lineChartOptions: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'RMSE vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'RMSE'
                },
              }
            ]
          }
        },


        lineChartData3: {
          labels: [
            "0",
            "1",
            "2"
          ],
          datasets: [
            {
              label: "Baseline MAD",
              // backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: baseline_mad
            },
            {
              label: "Training MAD",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_mad
            },
            {
              label: "Test MAD",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(3,3,205,1)",
              borderWidth: 0.8,
              data: test_mad
            },
            
          ]
        },
        
        lineChartOptions3: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'MAD vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'MAD'
                },
              }
            ]
          }
        },


        lineChartData4: {
          labels: [
            "0",
            "1",
            "2"
          ],
          datasets: [
            {
              label: "Baseline R2",
              // backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: baseline_r2
            },
            {
              label: "Training R2",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_r2
            },
            {
              label: "Test R2",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(3,3,205,1)",
              borderWidth: 0.8,
              data: test_r2
            },
            
          ]
        },
        
        lineChartOptions4: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'R2 vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'R2'
                },
              }
            ]
          }
        },

        lineChartData5: {
          labels: [
            "0",
            "1",
            "2"
          ],
          datasets: [
            {
              label: "Baseline Accuracy",
              // backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: baseline_accuracy
            },
            {
              label: "Training Accuracy",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_accuracy
            },
            {
              label: "Test Accuracy",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(3,3,205,1)",
              borderWidth: 0.8,
              data: test_accuracy
            },
            
          ]
        },
        
        lineChartOptions5: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'Accuracy vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Accuracy'
                },
              }
            ]
          }
        },

        lineChartData6: {
          labels: [
            "0",
            "1",
            "2"
          ],
          datasets: [
            {
              label: "Baseline F1",
              // backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: baseline_f1
            },
            {
              label: "Training F1",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_f1
            },
            {
              label: "Test F1",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(3,3,205,1)",
              borderWidth: 0.8,
              data: test_f1
            },
            
          ]
        },
        
        lineChartOptions6: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'F1 vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'F1'
                },
              }
            ]
          }
        },

        lineChartData7: {
          labels: [
            "1",
            "2",
          ],
          datasets: [
            // {
            //   label: "Baseline RMSE",
            //   backgroundColor: "rgba(255, 99, 132, 0.1)",
            //   borderColor: "rgba(255, 99, 132, 1)",
            //   borderWidth: 0.7,
            //   data: baseline_rmse
            // },
            {
              label: "Assisted Learning Rate",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_alpha2
            }
          ]
        },
        lineChartOptions7: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'Asisted Learning Rate vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Assisted Learning Rate'
                },
              }
            ]
          }
        },

        



        lineChartData1: {
          labels: [
            "1",
            "2",
          ],
          datasets: [
            // {
            //   label: "Baseline RMSE",
            //   backgroundColor: "rgba(255, 99, 132, 0.1)",
            //   borderColor: "rgba(255, 99, 132, 1)",
            //   borderWidth: 0.7,
            //   data: baseline_rmse
            // },
            {
              label: "Assisted Learning Rate",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_alpha
            }
          ]
        },
        lineChartOptions1: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'Asisted Learning Rate vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Assisted Learning Rate'
                },
              }
            ]
          }
        },
        lineChartData2: {
          labels: [
            "Init",
            "0",
            "1",
            "2"
          ],
          datasets: [
            {
              label: "Baseline RMSE",
              // backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: baseline_rmse
            },
            {
              label: "Training RMSE",
              // backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: training_rmse
            },
            {
              label: "Test RMSE",
              // backgroundColor: "rgba(0,204,0,0.2)",
              borderColor: "rgba(0,204,0,1)",
              borderWidth: 0.8,
              data: test_rmse
            }
          ]
        },
        
        lineChartOptions2: {
          responsive: true,
          maintainAspectRatio: false,
          // bezierCurve: false,
          // elements: {
          //     line: {
          //         tension: 0
          //     }
          // },
          title: {
                display: true,
                text: 'RMSE vs. Round'
            },
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'Round'
                },
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                },
                scaleLabel: {
                  display: true,
                  labelString: 'RMSE'
                },
              }
            ]
          }
        },
    }
  },
  methods: {
    stop_train_task() {
      const payload = {
        task_id: this.task_id,
      }

      this.$axios.post('/stop_train_task/', payload)
        .then((response) => {
          console.log(response.data)
        })
        .catch((error) => {
          // handle error
          console.log(error)
        })

    },

    get_backend_log(task_id){
      let vm = this
      console.log('hshs')
      const payload = {
        task_id: task_id,
      }
      this.$axios.post('/get_backend_log/', payload)
        .then((response) => {
          console.log('backend',response)
          vm.backend_log=response.data
          
        })
        .catch((error) => {
          console.log(error)
        })

    },
    
    getLog(task_id) {
      let vm = this
      const train_log_address = node_path.join(this.root.toString(), this.sharedState.user_id.toString(), "task", task_id.toString(), "train", "log.txt")
      let Log_content = fs.readFileSync(train_log_address, {encoding:'utf8', flag:'r'});
      Log_content = Log_content.split("\n")
      console.log('root address', this.root)
      const train_log_address2 = node_path.join(this.root.toString(),'logs','main.log')
      let Log_content2 = fs.readFileSync(train_log_address2, {encoding:'utf8', flag:'r'});
      Log_content2 = Log_content2.split("\n")
      this.messages = [];
      this.messages2 = []
      
      for (let i = 0; i < Log_content.length; i++){
        this.messages.push(Log_content[i])
        // console.log('dai',Log_content[i])
        if (Log_content[i].search("Train stage done") != -1 && vm.test_id == null){
          console.log('zaina',Log_content[i].search("Train stage done"))
          console.log('cheng')
          break
        }
      }

      // for (let i = 0; i < Log_content2.length; i++){
      //   this.messages2.push(Log_content2[i])
      //   console.log('dai',Log_content[i])
        
      // }


      for (let message of this.messages){        
      if (message.search("RMSE:") != -1){
        this.task_mode = 'regression'
        break
      }
      else if (message.search("F1") != -1)
      {
        this.task_mode = 'classification'
        break
      }
      else{
        continue
      }
    }
    console.log('this.task_mode', this.task_mode)
     
      // if (this.test_id == null){
        
      //   console.log('shitest')
      //   for (let i in this.messages){
      //     if (this.messages[i].search("Train stage done") != -1){
      //       console.log('zhaodao')
      //       // this.messages = this.messages.slice(0,i+1)
      //       this.messages.splice(i+1,this.messages.length-i)
      //       console.log('haha',this.messages)
      //     }
      //   }
      //   for (let i in this.messages){
      //     this.$set( this.messages , i , this.messages[i] )
      //   }
      // }//end if

    
      // const test_log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + response.data.test_id + '/log.txt'
    },
    // get_test_history_id(task_id) {



    // },
    checkSponsor(task_id) {
      let vm = this
      console.log('checksponsor')
      const payload = {
        task_id: task_id,
      }

      this.$axios.post('/check_sponsor/', payload)
        .then((response) => {
          // console.log("response@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", response)
          if (response.data.result == "sponsor"){
            this.isSponsor = true
            // console.log("#############1", this.isSponsor)
          }else{
            this.isSponsor = false
            // console.log("#############2", this.isSponsor)
          }
        })
        .catch((error) => {
          // handle error
          console.log(error)
        })

        this.$axios.post('/get_test_history_id/', payload)
        .then((response) => {

          let test_id_list = response.data.test_id_list;
          for (let i = 0; i < test_id_list.length; i++){
            const test_log_address = this.root + '/' + this.sharedState.user_id + '/task/' + task_id + '/' + 'test/' + test_id_list[i] + '/log.txt'
            let test_log_content = fs.readFileSync(test_log_address, {encoding:'utf8', flag:'r'});
            test_log_content = test_log_content.split("\n")
            for (let i = 0; i < test_log_content.length; i++){
              if (vm.test_id == null){
                break
              }
              this.messages.push(test_log_content[i])
              }
            }
          
          
          vm.draw_chart()
          
          
        })
        .catch((error) => {
          // handle error
          console.log(error)
        })
        // console.log('messages2',this.messages)
    },

    draw_chart(){
      let vm=this

      if (this.task_mode == 'regression'){

      
      console.log('messages2',this.messages)
            const rmse_list=[]
            const alpha_list =[]
            const mad_list = []
            const r2_list = []
            console.log('messages',this.messages)
            for (let message of this.messages){
              // console.log('rmse', message.search("RMSE:"))
              if (message.search("Test") != -1){
                vm.test_num = '1'
                console.log('test_num', vm.test_num)
                break
              }
            }
            // console.log('test_num', vm.test_num)
            for (let message of this.messages){
              // console.log('rmse', message.search("RMSE:"))
              if (message.search("RMSE:") == -1){
                continue
              }
              // console.log('content', message)
              let rmse = message.slice(message.search("RMSE")+6,message.search("RMSE")+11)
              console.log('rmse_num', message.slice(message.search("RMSE")+6,message.search("RMSE")+11))
              rmse_list[rmse_list.length] = rmse
            }
            for (let message of this.messages){
              // console.log('alpha', message.search("alpha:"))
              if (message.search("Alpha:") == -1){
                continue
              }
              // console.log('content', message)
              let alpha = message.slice(message.search("Alpha:")+8,message.search("Alpha:")+13)
              console.log('alpha_num', message.slice(message.search("Alpha:")+8,message.search("Alpha:")+13))
              alpha_list[alpha_list.length] = alpha
            }
            for (let message of this.messages){
              console.log('alpha', message.search("alpha:"))
              if (message.search("MAD") == -1){
                continue
              }
              console.log('content', message)
              console.log('che',message)
              let mad = message.slice(message.search("MAD:")+5,message.search("MAD:")+10)
              console.log('dachu',mad)
              console.log('mad_num', message.slice(message.search("MAD:")+5,message.search("MAD:")+10))
              mad_list[mad_list.length] = mad
            }
            for (let message of this.messages){
              if (message.search("R2") == -1){
                continue
              }
              let r2 = message.slice(message.search("R2:")+4,message.search("R2:")+9)
              r2_list[r2_list.length] = r2
            }
            // console.log('messages',this.messages)
            console.log('rmse_list',rmse_list)
            console.log('alpha_list',alpha_list)
            console.log('mad_list', mad_list )
            console.log('r2_list', r2_list)
            // console.log('mad_list', mad_list)
            // for (let i in baseline_rmse){
            //   baseline_rmse[i] = rmse_list[0]
            // }
            for(let i=0; i<rmse_list.length-1; i++){
              baseline_rmse[i] = rmse_list[0]
              // vm.lineChartData.datasets[0].data[i] = rmse_list[0]
              // vm.lineChartData.datasets[0].data.push(rmse_list[0])
              // console.log('chakan', vm.lineChartData.datasets[0].data)
              // console.log('chakan', vm.lineChartData.datasets[1].data)
              training_rmse[i] = rmse_list[i+1]
              baseline_mad[i] = mad_list[0]
              training_mad[i] = mad_list[i+1]
              baseline_r2[i] = r2_list[0]
              training_r2[i] = r2_list[i+1]

            }
            for(let i=0; i<alpha_list.length; i++){
              training_alpha[i] = alpha_list[i]
            }
            test_rmse = []
            test_mad = []
            test_r2 = []
            if (vm.test_id != null){
            test_rmse = rmse_list.slice(rmse_list.length-2,rmse_list.length)
            console.log('test_rmse',test_rmse)
            test_mad = mad_list.slice(mad_list.length-2,mad_list.length)
            console.log('test_mad',test_mad)
            test_r2 = r2_list.slice(r2_list.length-2,r2_list.length)
            console.log('test_r2',test_r2)
            }

            console.log('training_alpha',training_alpha)
            
            vm.lineChartData.datasets[0].data = baseline_rmse
            vm.lineChartData.datasets[1].data = training_rmse
            vm.lineChartData.datasets[2].data = test_rmse

            vm.lineChartData1.datasets[0].data = training_alpha
            vm.lineChartData2.datasets[2].data = test_rmse

            vm.lineChartData3.datasets[0].data = baseline_mad
            vm.lineChartData3.datasets[1].data = training_mad
            vm.lineChartData3.datasets[2].data = test_mad

            vm.lineChartData4.datasets[0].data = baseline_r2
            vm.lineChartData4.datasets[1].data = training_r2
            vm.lineChartData4.datasets[2].data = test_r2
      }
      else if (this.task_mode == 'classification'){

        console.log('messages2',this.messages)
            const accuracy_list=[]
            const f1_list = []
            const alpha_list =[]
              
            console.log('messages',this.messages)
            for (let message of this.messages){
              // console.log('rmse', message.search("RMSE:"))
              if (message.search("Test") != -1){
                vm.test_num = '1'
                console.log('test_num', vm.test_num)
                break
              }
            }
            // console.log('test_num', vm.test_num)
            for (let message of this.messages){
              // console.log('rmse', message.search("RMSE:"))
              if (message.search("Accuracy:") == -1){
                continue
              }
              // console.log('content', message)
              let accuracy = message.slice(message.search("Accuracy:")+10,message.search("Accuracy:")+15)
              console.log('accuracy_num', message.slice(message.search("Accuracy")+10,message.search("Accuracy")+15))
              accuracy_list[accuracy_list.length] = accuracy
            }
            for (let message of this.messages){
              // console.log('alpha', message.search("alpha:"))
              if (message.search("Alpha:") == -1){
                continue
              }
              // console.log('content', message)
              let alpha = message.slice(message.search("Alpha:")+8,message.search("Alpha:")+13)
              console.log('alpha_num', message.slice(message.search("Alpha:")+8,message.search("Alpha:")+13))
              alpha_list[alpha_list.length] = alpha
            }
            for (let message of this.messages){
              if (message.search("F1:") == -1){
                continue
              }
              console.log('content', message)
              console.log('che',message)
              let f1 = message.slice(message.search("F1:")+4,message.search("F1:")+9)
              console.log('dachu',f1)
              console.log('f1_num', message.slice(message.search("F1:")+4,message.search("F1:")+9))
              f1_list[f1_list.length] = f1
            }
            
            // console.log('messages',this.messages)
            console.log('accuracy_list',accuracy_list)
            console.log('f1_list', f1_list )
            console.log('alpha_list',alpha_list)
            
            // console.log('mad_list', mad_list)
            // for (let i in baseline_rmse){
            //   baseline_rmse[i] = rmse_list[0]
            // }
            for(let i=0; i<accuracy_list.length-1; i++){
              baseline_accuracy[i] = accuracy_list[0]
              // vm.lineChartData.datasets[0].data[i] = rmse_list[0]
              // vm.lineChartData.datasets[0].data.push(rmse_list[0])
              // console.log('chakan', vm.lineChartData.datasets[0].data)
              // console.log('chakan', vm.lineChartData.datasets[1].data)
              training_accuracy[i] = accuracy_list[i+1]
              baseline_f1[i] = f1_list[0]
              training_f1[i] = f1_list[i+1]
             

            }
            for(let i=0; i<alpha_list.length; i++){
              training_alpha2[i] = alpha_list[i]
            }
            test_accuracy = []
            test_f1 = []
            
            if (vm.test_id != null){
            test_accuracy = accuracy_list.slice(accuracy_list.length-2,accuracy_list.length)
            console.log('test_accuracy',test_accuracy)
            test_f1 = f1_list.slice(f1_list.length-2,f1_list.length)
            console.log('test_f1',test_f1)
  
            }

            console.log('training_alpha',training_alpha)
            
            vm.lineChartData5.datasets[0].data = baseline_accuracy
            vm.lineChartData5.datasets[1].data = training_accuracy
            vm.lineChartData5.datasets[2].data = test_accuracy

            vm.lineChartData6.datasets[0].data = baseline_f1
            vm.lineChartData6.datasets[1].data = training_f1
            vm.lineChartData6.datasets[2].data = test_f1


            vm.lineChartData7.datasets[0].data = training_alpha2
            

           
           

      }
      else{
        console.log('doumeijin')
      }

    }


    // getUser (id) {
    //   const path = `/users/${id}`
    //   this.$axios.get(path)
    //     .then((response) => {
    //       // handle success
    //       this.user = response.data
    //     })
    //     .catch((error) => {
    //       // handle error
    //       console.error(error)
    //     })
    // },
    // getUserHistoryMessages (id) {
    //   let page = 1
    //   let per_page = 10
    //   if (typeof this.$route.query.page != 'undefined') {
    //     page = this.$route.query.page
    //   }

    //   if (typeof this.$route.query.per_page != 'undefined') {
    //     per_page = this.$route.query.per_page
    //   }
      
    //   const path = `/users/${id}/history-messages/?from=${this.$route.query.from}&page=${page}&per_page=${per_page}`
    //   this.$axios.get(path)
    //     .then((response) => {
    //       // handle success
    //       this.messages = response.data
    //     })
    //     .catch((error) => {
    //       // handle error
    //       console.error(error)
    //     })
    // },
    // onSubmitReply () {
      // this.replyMessageForm.errors = 0  // 重置

      // if (!this.replyMessageForm.body) {
      //   this.replyMessageForm.errors++
      //   this.replyMessageForm.bodyError = 'Body is required.'
      //   // 给 bootstrap-markdown 编辑器内容添加警示样式，而不是添加到 #post_body 上
      //   $('#replyMessageForm .md-editor').closest('.form-group').addClass('u-has-error-v1')  // Bootstrap 4
      // } else {
      //   this.replyMessageForm.bodyError = null
      //   $('#replyMessageForm .md-editor').closest('.form-group').removeClass('u-has-error-v1')
      // }

      // if (this.replyMessageForm.errors > 0) {
      //   // 表单验证没通过时，不继续往下执行，即不会通过 axios 调用后端API
      //   return false
      // }

    //   const payload = {
    //     assistor_id: this.user.id,
    //     // body: this.replyMessageForm.body
    //     body: this.typein_message
    //   }
    //   this.$axios.post('/messages/', payload)
    //     .then((response) => {
    //       // handle success
    //       this.$toasted.success(`Successed send the private message to ${this.user.name || this.user.username}.`, { icon: 'fingerprint' })
    //       this.onResetReply()
    //       this.getUserHistoryMessages(this.sharedState.user_id)
    //     })
    //     .catch((error) => {
    //       // handle error
    //       console.log(error.response.data)
    //       this.$toasted.error(error.response.data.message, { icon: 'fingerprint' })
    //     })
    // },
    // onResetReply () {
    //   // this.replyMessageForm.body = ''
    //   // this.replyMessageForm.bodyError = null
    //   // $('#replyMessageForm .md-editor').closest('.form-group').removeClass('u-has-error-v1')
    //   this.showOnce = false
    //   this.typein_message = ''
    // },
  },
  // beforeCreate
  created () {
    this.task_id = this.$route.query.from;
    this.task_name = this.$route.query.from_task_name
    this.test_id = this.$route.query.from_test_id
    this.task_description = this.$route.query.from_task_description
    console.log('this.test_id', this.test_id)
    let new_root = store.changeroot()
    this.root = new_root.root;
    this.exe_position = new_root.exe_position
    this.getLog(this.$route.query.from)
    this.checkSponsor(this.$route.query.from)
    this.get_backend_log(this.task_id)
    
    this.$nextTick(this.draw_chart())
    
    // this.$nextTick(this.checkSponsor(this.$route.query.from))
    
    // console.log('chakan', this.lineChartData.datasets[0].label)
    // console.log('lol')
    // this.$forceUpdate();
    // this.$router.go()
    // console.log('chakan1', this.lineChartData.datasets[0].data)
    
        
    
    
    // 初始化 bootstrap-markdown 插件
    // $(document).ready(function() {
    //   $("#replyMessageFormBody").markdown({
    //     autofocus:false,
    //     savable:false,
    //     iconlibrary: 'fa',  // 使用Font Awesome图标
    //     language: 'zh'
    //   })
    // })
  },

  mounted: function () {
      //  this.$nextTick(this.draw_chart())
            
            
  
},
  // 当路由变化后(比如变更查询参数 page 和 per_page)重新加载数据
  beforeRouteUpdate (to, from, next) {
    next()
    // this.getLog(this.$route.query.from)
    // this.checkSponsor(this.$route.query.from)
  }
}



</script>

<style>
  .card-block {
    overflow: auto;
}
body{
    margin-top:20px;
    background:#eee;
}
.box.box-aqua {
    border-top-color: #00c0ef !important;
}
.box.box-green {
    border-top-color: #00a65a !important;
}
.box.box-success {
    border-top-color: #3c8dbc;
}
.box {
    position: relative;
    border-radius: 3px;
    background: #ffffff;
    border-top: 3px solid #d2d6de;
    margin-bottom: 20px;
    width: 100%;
    box-shadow: 0 1px 1px rgba(0,0,0,0.1);
}
.box-header {
    color: #444;
    display: block;
    padding: 10px;
    position: relative;
}
.box-header>.ion {
    margin-right: 5px;
}
.box-header .box-title {
    display: inline-block;
    font-size: 18px;
    margin: 0;
    line-height: 1;
}
.box-header>.box-tools {
    position: absolute;
    right: 10px;
    top: 5px;
}
.inline {
    display: inline;
}
.box-body {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-right-radius: 3px;
    border-bottom-left-radius: 3px;
    padding: 10px;
}
.todo-list {
    margin: 0;
    padding: 0;
    list-style: none;
    overflow: auto;
}
.todo-list>li {
    border-radius: 2px;
    padding: 10px;
    background: #f4f4f4;
    margin-bottom: 2px;
    border-left: 2px solid #e6e7e8;
    color: #444;
}
.todo-list>li .label {
    margin-left: 10px;
    font-size: 9px;
}
.todo-list>li .tools {
    display: none;
    float: right;
    color: #dd4b39;
}
.todo-list>li:hover .tools{
    display: block;  
}
.no-border {
    border: 0 !important;
}
.box-footer {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-right-radius: 3px;
    border-bottom-left-radius: 3px;
    border-top: 1px solid #f4f4f4;
    padding: 10px;
    background-color: #fff;
}
.btn-default {
    background-color: #f4f4f4;
    color: #444;
    border-color: #ddd;
}
.btn {
    border-radius: 3px;
    -webkit-box-shadow: none;
    box-shadow: none;
    border: 1px solid transparent;
}
mdb-container {
    max-width: 100% ;
    max-height: auto;
}
mdb-line-chart {
    max-width: 100% ;
    max-height: auto;
}

[v-cloak] {
  display: none;
}
</style>

