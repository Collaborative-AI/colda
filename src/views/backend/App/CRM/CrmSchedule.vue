<template>
     <div class="container-fluid crm3">
         <b-row>
            <b-col lg="12" >
               <card class=" card-block card-stretch card-height">
                 <template v-slot:headerTitle>
                     <ul class="list-unstyled calender-box mb-0">
                        <li class="text-center">
                           <h4 class="mb-1">New</h4>
                           <span class="mb-0 mt-1 text-success"><i class="ri-arrow-right-up-line"></i>$ 500</span>
                           <span> <i class="fa fa-circle pro-font line-height" aria-hidden="true"></i> 5 Deals</span>
                        </li>
                        <li class="text-center">
                           <h4 class="mb-1">Follow up</h4>
                           <span class="mb-0 mt-1 text-danger"><i class="ri-arrow-left-down-line"></i>$ 1500</span>
                           <span> <i class="fa fa-circle pro-font line-height" aria-hidden="true"></i> 2 Deals</span>
                        </li>
                        <li class="text-center">
                           <h4 class="mb-1">Under review</h4>
                           <span class="mb-0 mt-1 text-warning"><i class="ri-arrow-right-up-line"></i>$6000</span>
                           <span> <i class="fa fa-circle pro-font line-height" aria-hidden="true"></i> 5 Deals</span>
                        </li>
                        <li class="text-center">
                           <h4 class="mb-1">Demo</h4>
                           <span class="mb-0 mt-1 text-primary"><i class="ri-arrow-right-up-line"></i>$3000</span>
                           <span> <i class="fa fa-circle pro-font line-height" aria-hidden="true"></i> 5 Deals</span>
                        </li>
                        <li class="text-center">
                           <h4 class="mb-1">Negotiation</h4>
                           <span class="mb-0 mt-1 text-info"><i class="ri-arrow-left-down-line"></i>$8000</span>
                           <span> <i class="fa fa-circle pro-font line-height" aria-hidden="true"></i> 5 Deals</span>
                        </li>
                        <li class="text-center">
                           <h4 class="mb-1">Won</h4>
                           <span class="mb-0 mt-1 text-warning"><i class="ri-arrow-right-up-line"></i>$9000</span>
                           <span> <i class="fa fa-circle pro-font line-height" aria-hidden="true"></i> 5 Deals</span>
                        </li>
                     </ul>
                 </template>
                   <template v-slot:body>
                   <VueFullCalendar defaultView="dayGridMonth"
                   :header="header"
                   :plugins="calendarPlugins"
                   :events="calendarEvents"
                   time-zone="UTC"
  />
                   </template>
               </card>
            </b-col>
         </b-row>
      </div>
</template>
<script>
import VueFullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import listPlugin from '@fullcalendar/list'
export default {
    name:'CrmSchedule',
    props: {
    // eslint-disable-next-line vue/require-valid-default-prop
    calendarEvents: { type: Array },
    header: { type: Object,
      // eslint-disable-next-line vue/require-valid-default-prop
      default () {
        return {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
        }
      }
    }
  },
  data () {
    return {
      calendarPlugins: [
        dayGridPlugin,
        timeGridPlugin,
        interactionPlugin,
        listPlugin
      ]
    }},
    components: {
    VueFullCalendar // make the <VueFullCalendar> tag available
  },
  mounted () {
  },
  computed: {
  },
  methods: {
  }
}
</script>
<style lang='scss'>
  .fc-event, .fc-event:hover{
    color: #ffffff !important;
  }
  @import '~@fullcalendar/core/main.css';
  @import '~@fullcalendar/daygrid/main.css';
  @import '~@fullcalendar/timegrid/main.css';
  @import '~@fullcalendar/list/main.min.css';
</style>
